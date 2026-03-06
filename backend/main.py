from fastapi import FastAPI
from ai.mood_detector import detect_mood

app = FastAPI()

@app.get("/")
def read_root(text: str):
    mood = detect_mood(text)
    return mood
