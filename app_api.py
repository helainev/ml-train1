import streamlit as st
import requests
import json
from requests.exceptions import ConnectionError, Timeout, RequestException, JSONDecodeError
from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel, Field, ValidationError
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Загрузка модели из файла pickle
if not os.path.exists('model.pkl'):
    raise RuntimeError("model.pkl not found. Please train the model first.")

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Счетчик запросов
request_count = 0

# Модель для валидации входных данных
class PredictionInput(BaseModel):
    Pclass: int = Field(gt=0, le=3, description="Ticket class (1-3)")
    Age: float = Field(gt=0, le=120, description="Age (0-120)")
    Fare: float = Field(gt=0, description="Fare (must be positive)")
@app.get("/stats")
def stats():
    return {"request_count": request_count}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict_model")
def predict_model(input_data: PredictionInput):
    global request_count
    request_count += 1

    try:
    # Создание DataFrame из данных
    new_data = pd.DataFrame({
        'Pclass': [input_data.Pclass],
        'Age': [input_data.Age],
        'Fare': [input_data.Fare]
    })

    # Предсказание
    predictions = model.predict(new_data)

    # Преобразование результата в человеко-читаемый формат
    result = "Survived" if predictions[0] == 1 else "Not Survived"

    return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)