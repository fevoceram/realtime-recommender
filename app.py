from fastapi import FastAPI
from model import Recommender

app = FastAPI()
model = Recommender()

@app.get("/")
def home():
    return {"message": "Recommender API Running"}

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int):
    recs = model.recommend(user_id)
    return {"user_id": user_id, "recommendations": recs.tolist()}
