# Titanic Survival Prediction API 🚢🤖

A production-ready machine learning microservice built with **Python**, **FastAPI**, and **Scikit-Learn**. The service deploys a Decision Tree model to predict passenger survival on the Titanic, tracks request analytics, and features modern dependency management via **uv** alongside complete **Docker** containerization.

---

## 🛠️ Tech Stack & Architecture

- **Core:** Python 3.12+
- **Machine Learning:** Scikit-Learn, Pandas
- **API Framework:** FastAPI, Pydantic, Uvicorn
- **Package Management:** `uv` (modern, ultra-fast Python bundling)
- **Containerization:** Docker

---

## 🚀 Getting Started & Installation

  ```bash
 docker compose up -d

#если ранее был уже запущен такой контейнер, его можно остановить
   docker stop titanic-ml-backend
   docker stop titanic-ml-frontend
# если ранее был уже создан такой контейнер, его можно удалить
   docker rm -f titanic-ml-backend
   docker rm -f titanic-ml-frontend
# остановить все контейнеры
   docker compose down  
# удалить образы с очиской кэша   
   docker compose down --rmi local -v
# можно проверить наличие контейнеров
   docker ps -a
  ```
