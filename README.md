Sentiment AI Analyzer

A simple and lightweight AI-powered tool that analyzes the sentiment of any given text using Python and HuggingFace Transformers.

🚀 Features

Detects Positive, Negative, or Neutral sentiment

Uses state-of-the-art Transformer models

Easy to run in any environment

Perfect for demonstrating AI project experience

🧠 How It Works

This tool uses a pre-trained natural language processing model to understand emotions in text.

🛠️ Installation
pip install transformers torch

▶️ Usage Example
from transformers import pipeline

sentiment = pipeline("sentiment-analysis")
result = sentiment("I am excited to apply for the GTV!")
print(result)

📄 Output Example
[{'label': 'POSITIVE', 'score': 0.99}]

👩‍💻 Author

Mrudula Billa
AI Enthusiast | Mental Health Technology Innovator
