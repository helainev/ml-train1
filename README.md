# Titanic Survival Prediction API 🚢🤖

A production-ready machine learning microservice built with **Python**, **FastAPI**, and **Scikit-Learn**. The service deploys a Decision Tree model to predict passenger survival on the Titanic, tracks request analytics, and features modern dependency management via **uv** alongside complete **Docker** containerization.

---

## 🛠️ Tech Stack & Architecture

- **Core:** Python 3.14+
- **Machine Learning:** Scikit-Learn, Pandas
- **API Framework:** FastAPI, Pydantic, Uvicorn
- **Package Management:** `uv` (modern, ultra-fast Python bundling)
- **Containerization:** Docker

---

## 🚀 Getting Started & Installation

  ```bash  
 docker compose up -d

# остановить все контейнеры
   docker compose down  
# остановить и удалить образы с очиской кэша   
   docker compose down --rmi local -v
# можно проверить наличие контейнеров
   docker ps -a
  ```
## 📡 Api Endpoints

Once the application is running, you can access the interactive 
🔗 **`http://127.0.0.1:8501`**