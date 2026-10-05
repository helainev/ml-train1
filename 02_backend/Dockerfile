FROM python:3.12-slim

WORKDIR /app

RUN apt-get update

# Сначала копируем только requirements.txt и устанавливаем зависимости
COPY ./02_backend/requirements.txt /app
RUN pip3 install -r requirements.txt

# Затем копируем остальной код
COPY ./02_backend /app

CMD ["python3", "app_api.py"]