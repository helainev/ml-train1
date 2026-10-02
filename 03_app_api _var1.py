"""
создаем api c тремя ручками: одна для предсказания выживания (/predict),
другая для получения количества сделанных запросов (/stats),
и третья, для проверки работы API (/health)

Перед выполнением нужно проверить установлены ли библиотеки (позже занесем их в файл requirements.txt):
    uv pip show pydantic
    uv pip show pandas
    uv pip show scikit-learn
    uv pip show uvicorn
    uv pip show fastapi
Если библиотека установлена, увидим информацию о ней (версию, автора, расположение), если не установлена, утилита вернет ошибку WARNING
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
    # пока для проверки запускаем на локальном компьютере, поэтому
    # host указываем локальный, у всем он один 127.0.0.1, порт может быть любой, какой зададим
    uvicorn.run(app, host="127.0.0.1", port=5000) 

"""

Проверка работы API через curl  (Test1), в новом терминале запускаем:
curl -X GET http:/127.0.0.1:5000/health  
      получаем результат {"status":"OK"}
curl -X GET http:/127.0.0.1:5000/stats
      получаем результат {"request_count":0}
curl -X POST http:/127.0.0.1:5000/predict_model -H "Content-Type: application/json" -d "{\"Pclass\": 3, \"Age\": 22.0, \"Fare\": 7.2500}"
      получаем результат {"prediction":"Not Survived"}
      затем уменьшаем возраст 2 года - ребенок
curl -X POST http:/127.0.0.1:5000/predict_model -H "Content-Type: application/json" -d "{\"Pclass\": 3, \"Age\": 2.0, \"Fare\": 7.2500}"
      получаем результат {"prediction":"Survived"}   
curl -X GET http:/127.0.0.1:5000/stats
      получаем результат {"request_count":2}
"""