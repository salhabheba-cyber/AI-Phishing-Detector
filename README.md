#  AI-PhishDetect 2026

<div align="center">
  
  [![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
  [![HuggingFace](https://img.shields.io/badge/🤗-Transformers-yellow?style=for-the-badge)](https://huggingface.co)
  [![Gradio](https://img.shields.io/badge/Gradio-UI-orange?style=for-the-badge)](https://gradio.app)
  [![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
  
  <h3>Zero-Shot LLM Phishing Detection for the 2026 Threat Landscape</h3>
  <p><i>Built in Beirut, Lebanon for global remote security teams</i></p>
  
</div>

---

##  Overview

**AI-PhishDetect 2026** is a production-ready phishing detection system that uses Large Language Models to identify AI-generated phishing emails. Unlike traditional keyword-based scanners, it understands **semantic intent, urgency manipulation, and deception patterns** in email content.

###  Why This Matters in 2026

Traditional phishing detection relies on keywords like *"Nigerian prince"* or *"verify account"*. Modern AI-generated phishing uses perfect grammar and varied vocabulary, bypassing these scanners. This system detects the **intent behind the words**.

###  Key Features

- ✅ **Zero-shot learning** – No training data required, works immediately
- ✅ **Semantic intent analysis** – Detects psychological manipulation tactics
- ✅ **AI-generated detection** – Catches scams from GPT-4, Claude, Gemini
- ✅ **Explainable results** – Provides reasoning behind every verdict
- ✅ **Interactive UI** – Test any email instantly with Gradio

---

##  Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **LLM Model** | BART-large-MNLI | Zero-shot classification (406M params) |
| **Framework** | Hugging Face Transformers | Model inference |
| **UI** | Gradio | Interactive web interface |
| **Language** | Python 3.11 | Core programming |

---

##  Quick Start

### Option 1: Run in Google Colab (Free GPU)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/AI-PhishDetect-2026/blob/main/AI_PhishDetect_LabA.ipynb)

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/AI-PhishDetect-2026.git
cd AI-PhishDetect-2026

# Install dependencies
pip install -r requirements.txt

# Run the Gradio app
python app/app.py
