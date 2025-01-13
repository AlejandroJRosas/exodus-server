from fastapi import FastAPI
from pydantic import BaseModel
from analizer import infer_feeling

app = FastAPI(title="Exodus Análisis de Sentimientos API", version="0.1.0")

class Item(BaseModel):
    text: str

@app.get("/")
def read_root():
  return {"detail": "Exodus Server Running!😍"}

@app.post("/analize")
async def analize_sentiment(item: Item):
  return infer_feeling(item.text)
