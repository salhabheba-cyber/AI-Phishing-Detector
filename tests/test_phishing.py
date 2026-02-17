"""
Test suite for AI-PhishDetect 2026.
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.classifier import PhishingClassifier

def run_tests():
    """Run test cases."""
    print("="*60)
    print("🧪 AI-PhishDetect 2026 - Test Suite")
    print("="*60)
    
    clf = PhishingClassifier()
    
    test_cases = [
        {
            "email": "Your PayPal account has been limited. Click here: http://fake.com",
            "expected": "phishing",
            "desc": "Classic PayPal phishing"
        },
        {
            "email": "Your Amazon order #12345 has shipped. Track: https://amazon.com",
            "expected": "legitimate",
            "desc": "Amazon shipping notification"
        },
        {
            "email": "URGENT: Your password expires in 24 hours. Verify now.",
            "expected": "phishing",
            "desc": "Password expiration scam"
        }
    ]
    
    print("\n📋 Running tests...\n")
    
    passed = 0
    for i, test in enumerate(test_cases, 1):
        result = clf.classify(test["email"])
        is_phishing = result['phishing_confidence'] > 50
        expected_phishing = (test["expected"] == "phishing")
        
        if is_phishing == expected_phishing:
            status = "✅ PASS"
            passed += 1
        else:
            status = "❌ FAIL"
        
        print(f"{status} Test {i}: {test['desc']}")
        print(f"   Score: {result['phishing_confidence']}%")
        print(f"   Verdict: {result['verdict']}")
        print()
    
    print(f"📊 Results: {passed}/{len(test_cases)} passed")
    print("="*60)

if __name__ == "__main__":
    run_tests()
