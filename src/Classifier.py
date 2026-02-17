"""
AI-PhishDetect 2026 - Core Classification Engine
Author: Your Name
Date: 2026-02-13
Zero-shot phishing detection using LLMs.
"""

import torch
import re
from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PhishingClassifier:
    """Main classifier for zero-shot phishing detection."""
    
    def __init__(self, use_gpu=True):
        """Initialize the classifier."""
        logger.info("Loading model...")
        
        self.device = 0 if use_gpu and torch.cuda.is_available() else -1
        if self.device == 0:
            logger.info("✅ GPU detected")
        else:
            logger.warning("⚠️ CPU mode")
        
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=self.device
        )
        logger.info("✅ Model loaded")
    
    def preprocess(self, email_text):
        """Clean email text and count URLs."""
        if not isinstance(email_text, str):
            return "", 0
        
        original = email_text
        processed = email_text.lower()
        processed = re.sub(r'\s+', ' ', processed)
        
        # Count URLs
        url_pattern = r'https?://[^\s]+'
        url_count = len(re.findall(url_pattern, original))
        
        # Normalize
        processed = re.sub(url_pattern, ' [URL] ', processed)
        processed = re.sub(r'\S+@\S+', ' [EMAIL] ', processed)
        processed = re.sub(r'\s+', ' ', processed).strip()
        
        return processed, url_count
    
    def classify(self, email_text, threshold=0.60):
        """Classify email as phishing or legitimate."""
        cleaned_text, url_count = self.preprocess(email_text)
        
        if len(cleaned_text) < 20:
            return {
                "phishing_confidence": 0.0,
                "verdict": "INCONCLUSIVE - Too short",
                "recommendation": "Manual review required",
                "urls_detected": url_count
            }
        
        # Get classification
        result = self.classifier(
            cleaned_text,
            candidate_labels=["phishing", "legitimate"],
            hypothesis_template="This email is {}."
        )
        
        phishing_score = result['scores'][result['labels'].index('phishing')]
        
        # URL boost
        if url_count > 0:
            phishing_score = min(phishing_score + 0.15, 1.0)
        
        # Determine verdict
        if phishing_score >= 0.70:
            verdict = "🔴 HIGH RISK - PHISHING DETECTED"
            recommendation = "BLOCK IMMEDIATELY. Do not click links."
        elif phishing_score >= 0.45:
            verdict = "🟡 SUSPICIOUS - Manual review required"
            recommendation = "Verify sender before responding."
        else:
            verdict = "🟢 LOW RISK - Appears legitimate"
            recommendation = "No action needed."
        
        return {
            "phishing_confidence": round(phishing_score * 100, 2),
            "verdict": verdict,
            "recommendation": recommendation,
            "urls_detected": url_count
        }


# Quick test
if __name__ == "__main__":
    clf = PhishingClassifier()
    test_email = "Your PayPal account has been limited. Click here: http://fake.com"
    result = clf.classify(test_email)
    print(f"Score: {result['phishing_confidence']}%")
    print(f"Verdict: {result['verdict']}")
