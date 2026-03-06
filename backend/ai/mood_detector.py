from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def detect_mood(text):
    result = classifier(text)
    return result
