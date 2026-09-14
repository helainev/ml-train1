import streamlit as st 
import requests
import json
from requests.exceptions import ConnectionError, Timeout, RequestException, JSONDecodeError
from fastapi import HTTPException

ip_api = "127.0.0.1"
port_api = "5000"

# Заголовок приложения
st.title("Titanic Survival Prediction")

# Ввод данных
st.write("Enter the passenger details:")

# Выпадающее меню для выбора класса билета
pclass = st.selectbox("Ticket Class (Pclass)", [1, 2, 3])

# Текстовое поле для ввода возраста с проверкой на число
age = st.text_input("Age", value=10)
try:
    age_float = float(age)
    if age_float < 0 or age_float > 120:
        st.error("Age must be between 0 and 120.")
except ValueError:
    st.error("Please enter a valid number for Age.")

# Текстовое поле для ввода стоимости билета с проверкой на число
fare = st.text_input("Fare", value=100)
try:
    fare_float = float(fare)
    if fare_float < 0:
        st.error("Fare cannot be negative.")
except ValueError:
    st.error("Please enter a valid number for Fare.")

# Кнопка для отправки запроса
if st.button("Predict"):
    # Проверка, что все поля заполнены
    if age.isdigit() and fare.isdigit():
        # Подготовка данных для отправки
        data = {
            "Pclass": int(pclass),
            "Age": float(age),
            "Fare": float(fare)
        }

        # Проверка статуса API перед отправкой данных
        try:
            health_response = requests.get(f"http://{ip_api}:{port_api}/health", timeout=2)
            if health_response.status_code != 200:
                st.error(f"API is not responding. Status: {health_response.status_code}")
                st.stop()
        except RequestException as e:
            st.error(f"Cannot connect to the API server: {str(e)}")
            st.stop()

        try:
            # Отправка запроса к Flask API
            response = requests.post(f"http://{ip_api}:{port_api}/predict_model", json=data)

            # Проверка статуса ответа
            if response.status_code == 200:
                try:
                    prediction = response.json()["prediction"]
                    st.success(f"Prediction: {prediction}")
                except (json.JSONDecodeError, KeyError):
                    st.error("Server returned invalid JSON response")
            else:
                st.error(f"Request failed with status code {response.status_code}")
        except (ConnectionError, Timeout) as e:
            st.error(f"Connection error: {str(e)}")
        except RequestException as e:
            st.error(f"Request error: {str(e)}")
        except json.JSONDecodeError:
            st.error("Server returned invalid JSON response")
    else:
        st.error("Please fill in all fields with valid numbers.")

# Информация о статусе API
st.sidebar.header("API Status")
try:
    health = requests.get(f"http://{ip_api}:{port_api}/health", timeout=2)
    st.sidebar.success(f"API is running: {health.status_code == 200}")
except RequestException:
    st.sidebar.error("API is not responding")
