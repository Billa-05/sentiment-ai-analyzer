from transformers import pipeline

def analyze_sentiment(text):
    sentiment = pipeline("sentiment-analysis")
    result = sentiment(text)
    return result

if __name__ == "__main__":
    sample_text = "I am excited to apply for the GTV!"
    print("Input Text:", sample_text)
    print("Sentiment Result:", analyze_sentiment(sample_text))
