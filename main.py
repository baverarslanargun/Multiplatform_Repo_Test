from fastapi import FastAPI
from pydantic import BaseModel

class MoodEntry(BaseModel):
    score: int
    note: str

app = FastAPI(title="Mood API", description="A simple mood tracking API")
mood_entries = []

@app.get("/health")
def health_check():
    """Check if the API is running."""
    return {"status": "healthy"}

@app.post("/mood")
def create_mood(entry: MoodEntry):
    """Record a new mood entry."""
    mood_entries.append(entry)
    return entry

@app.get("/moods")
def get_moods():
    """Retrieve all mood entries."""
    return mood_entries

@app.get("/moods/average")
def avg_mood():
    """Get AVG"""
    sums=0
    j=0
    if not mood_entries:
        return {"avg" : 0}
    for i in mood_entries:
        sums = sums+i.score
        j=j+1
    return {"avg" : sums/j}