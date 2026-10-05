FROM python:3.12-slim

WORKDIR /app

RUN apt-get update

# Сначала копируем только requirements.txt и устанавливаем зависимости
COPY ./03_frontend/requirements.txt /app
RUN pip3 install -r requirements.txt

# Затем копируем остальной код
COPY /03_frontend /app

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]