"""
Версия 2.01
работа с api c тремя ручками: 
/predict - для предсказания выживания
/stats - для получения количества сделанных запросов,
/health - для проверки работы API 
"""
import streamlit as st 
import requests
from requests.exceptions import ConnectionError

ip_api = "titanic-ml-backend"
port_api = "5000"

# 5000 - порт в бэкенде(app_api.py)
# titanic-ml-backend - имя, указнное в docker-compose.yaml, а именно:
# build:
#      context: .
#      dockerfile: 02_backend/Dockerfile
#    image: titanic-ml-backend:latest
#    container_name: titanic-ml-backend

# Заголовок приложения
st.title("Прогноз выживания пассажиров Титаника")

# Ввод данных
st.write("Ввод информации о пассажире:")

# Выпадающее меню для выбора класса билета
pclass = st.selectbox("Класс билета (Pclass)", [1, 2, 3])

# Текстовое поле для ввода возраста с проверкой на число
age = st.text_input("Возраст", value=10)
if not age.isdigit():
    st.error("Пожайлуста введите корректный возраст")

# Текстовое поле для ввода стоимости билета с проверкой на число
fare = st.text_input("Цена билета", value=100)
if not fare.isdigit():
    st.error("Пожалуста введите корректную цену билета")

# Кнопка для отправки запроса
if st.button("Выполнить прогноз"):
    # Проверка, что все поля заполнены
    if age.isdigit() and fare.isdigit():
        # Подготовка данных для отправки
        data = {
            "Pclass": int(pclass),
            "Age": float(age),
            "Fare": float(fare)
        }

        try:
            # Отправка запроса к Flask API
            response = requests.post(f"http://{ip_api}:{port_api}/predict", json=data)

            # Проверка статуса ответа
            if response.status_code == 200:
                prediction = response.json()["prediction"]
                st.success(f"Прогноз модели: {prediction}")
            else:
                st.error(f"Request failed with status code {response.status_code}")
        except ConnectionError as e:
            st.error(f"Failed to connect to the server")
    else:
        st.error("Please fill in all fields with valid numbers.")