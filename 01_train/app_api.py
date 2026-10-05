"""
версия для докера - копия файла 04_app_api _var1.py с измененным хостом

создаем api c тремя ручками: одна для предсказания выживания (/predict),
другая для получения количества сделанных запросов (/stats),
и третья, для проверки работы API (/health)

"""

from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Загрузка модели из файла pickle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Счетчик запросов, сколько раз через обращались к модели, позже нужно сделать через базу данных
request_count = 0

# Модель для валидации входных данных
class PredictionInput(BaseModel):
    Pclass: int
    Age: float 
    Fare: float

@app.get("/stats")
def stats():
    return {"request_count": request_count}

@app.get("/health") # ручка для проверки работы API
def health():
    return {"status": "OK"}

@app.post("/predict_model")
def predict_model(input_data: PredictionInput):
    global request_count  # пока костыль через глобальную переменную, позже нужно прикрутить к базе данных
    request_count += 1


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
    
if __name__ == '__main__':
    import uvicorn
    # для версии программы для докера хост указываем другой "0.0.0.0"
    # поэтому для докера сформируем аналогичный файл и назовем его app_api.py
    uvicorn.run(app, host="0.0.0.0", port=5000) 