"""
AI-PhishDetect 2026 - Core Classification Engine
Author: Your Name
Date: 2026-02-13
Zero-shot phishing detection using Facebook BART-large-MNLI.
"""

import torch
import re
from transformers import pipeline
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PhishingClassifier:
    """Main classifier for zero-shot phishing detection."""
    
    def __init__(self, use_gpu=True):
        """Initialize the classifier with BART-large-MNLI."""
        logger.info("Loading BART-large-MNLI model...")
        
        # Determine device (GPU if available)
        self.device = 0 if use_gpu and torch.cuda.is_available() else -1
        if self.device == 0:
            logger.info("✅ GPU detected - acceleration enabled")
        else:
            logger.warning("⚠️ CPU mode - inference will be slower")
        
        # Load the zero-shot classification pipeline
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=self.device
        )
        
        # Define phishing indicators (semantic labels)
        self.phishing_labels = [
            "urgent account action required",
            "verify your identity immediately",
            "suspicious login attempt detected",
            "unauthorized transaction alert",
            "click here to secure your account",
            "password expiration notification",
            "limited time security update",
            "blocked account restoration",
            "unusual activity verification",
            "payment confirmation required",
            "invoice past due",
            "legal notice served",
            "compromised password alert"
        ]
        
        logger.info(f"✅ Model loaded with {len(self.phishing_labels)} phishing patterns")
    
    def preprocess(self, email_text):
        """
        Clean email text while preserving semantic meaning.
        """
        if not isinstance(email_text, str):
            return "", 0
        
        # Store original for URL counting
        original = email_text
        
        # Convert to lowercase
        processed = email_text.lower()
        
        # Remove excessive whitespace
        processed = re.sub(r'\s+', ' ', processed)
        
        # Count URLs (strong phishing signal)
        url_pattern = r'https?://[^\s]+'
        url_count = len(re.findall(url_pattern, original))
        
        # Normalize URLs for analysis
        processed = re.sub(url_pattern, ' [URL] ', processed)
        
        # Clean up extra spaces
        processed = re.sub(r'\s+', ' ', processed).strip()
        
        return processed, url_count
    
    def classify(self, email_text, confidence_threshold=0.65):
        """
        Classify email as phishing or legitimate.
        """
        # Preprocess
        cleaned_text, url_count = self.preprocess(email_text)
        
        # Validate input
        if len(cleaned_text) < 20:
            return {
                "phishing_confidence": 0.0,
                "legitimate_confidence": 0.0,
                "verdict": "INCONCLUSIVE - Email too short",
                "recommendation": "Manual review required",
                "primary_threat": "Insufficient text",
                "urls_detected": url_count
            }
        
        # SIMPLE FIX: Direct phishing classification
        result = self.classifier(
            cleaned_text,
            candidate_labels=["phishing", "legitimate"],
            hypothesis_template="This email is {}."
        )
        
        # Get phishing score
        phishing_score = result['scores'][result['labels'].index('phishing')]
        
        # URL boost (phishing emails almost always have URLs)
        if url_count > 0:
            phishing_score = min(phishing_score + 0.2, 1.0)
        
        # Generate verdict
        if phishing_score >= confidence_threshold:
            verdict = "⚠️ HIGH RISK - PHISHING DETECTED"
            recommendation = "DO NOT CLICK LINKS. Report to security team."
        elif phishing_score >= 0.4:
            verdict = "⚠️ SUSPICIOUS - Manual review required"
            recommendation = "Verify sender through alternate channel."
        else:
            verdict = "✅ LOW RISK - Appears legitimate"
            recommendation = "No action required."
        
        # Get threat type for high confidence emails
        primary_threat = "No threat detected"
        threat_confidence = 0.0
        
        if phishing_score > 0.6:
            threat_result = self.classifier(
                cleaned_text,
                candidate_labels=self.phishing_labels[:5],
                hypothesis_template="This email is trying to {}."
            )
            primary_threat = threat_result['labels'][0]
            threat_confidence = threat_result['scores'][0]
        
        return {
            "phishing_confidence": round(phishing_score * 100, 2),
            "legitimate_confidence": round((1 - phishing_score) * 100, 2),
            "verdict": verdict,
            "recommendation": recommendation,
            "primary_threat": primary_threat,
            "threat_confidence": round(threat_confidence * 100, 2),
            "urls_detected": url_count
        }


# Quick test
if __name__ == "__main__":
    print("⏳ Testing classifier...")
    clf = PhishingClassifier()
    
    test_emails = [
        "Your PayPal account has been limited. Click here: http://fake-paypal.com",
        "Your Amazon order #12345 has shipped. Track: https://amazon.com/track",
        "URGENT: Your password expires in 24 hours. Verify now at http://secure-verify.com"
    ]
    
    for email in test_emails:
        print(f"\n{'='*50}")
        print(f"📧 Email: {email[:80]}...")
        result = clf.classify(email)
        print(f"   Phishing: {result['phishing_confidence']}%")
        print(f"   Verdict: {result['verdict']}")
