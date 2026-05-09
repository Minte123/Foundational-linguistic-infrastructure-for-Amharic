from fastapi import FastAPI
from transformers.inference_engine import TransformerInferenceEngine

app = FastAPI()

engine = TransformerInferenceEngine()

@app.get("/predict")
def predict(text: str):

    return engine.predict(text)