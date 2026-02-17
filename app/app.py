"""
AI-PhishDetect 2026 - Gradio Web Interface
Author: Your Name
"""

import gradio as gr
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.classifier import PhishingClassifier

# Initialize classifier
classifier = PhishingClassifier()

def analyze_email(email, threshold=0.60):
    """Analyze email and return results."""
    if not email or len(email.strip()) < 10:
        return "⚠️ Please paste an email", "0%", "No recommendation"
    
    result = classifier.classify(email, threshold)
    
    return result['verdict'], f"{result['phishing_confidence']}%", result['recommendation']

# Create Gradio interface
with gr.Blocks(title="AI-PhishDetect 2026", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🛡️ AI-PhishDetect 2026
    ## Zero-Shot LLM Phishing Detection
    
    Built in **Beirut, Lebanon** for the global 2026 threat landscape.
    """)
    
    with gr.Row():
        email_input = gr.Textbox(
            label="📧 Email Content",
            placeholder="Paste email content here...",
            lines=8
        )
    
    with gr.Row():
        threshold = gr.Slider(
            minimum=0.3,
            maximum=0.9,
            value=0.6,
            step=0.05,
            label="Detection Sensitivity"
        )
        analyze_btn = gr.Button("🔍 Analyze Email", variant="primary")
    
    with gr.Row():
        verdict = gr.Textbox(label="Verdict", lines=2)
    
    with gr.Row():
        confidence = gr.Label(label="Confidence Score")
        recommendation = gr.Textbox(label="Recommendation", lines=2)
    
    # Examples
    gr.Examples(
        examples=[
            ["Your PayPal account has been limited. Click here: http://fake-paypal.com"],
            ["Your Amazon order #12345 has shipped. Track: https://amazon.com/track"],
            ["URGENT: Your password expires in 24 hours. Verify now."]
        ],
        inputs=email_input
    )
    
    # Connect button
    analyze_btn.click(
        fn=analyze_email,
        inputs=[email_input, threshold],
        outputs=[verdict, confidence, recommendation]
    )
    
    gr.Markdown("""
    ---
    ### 📁 GitHub Repository
    [github.com/YOUR_USERNAME/AI-PhishDetect-2026](https://github.com/YOUR_USERNAME/AI-PhishDetect-2026)
    """)

if __name__ == "__main__":
    demo.launch()
