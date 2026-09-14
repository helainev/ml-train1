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

You can run this microservice either locally using the `uv` package manager or inside an isolated Docker container.

### Option 1: Local Deployment with `uv`

Make sure you have `uv` installed. If not, install it via: `pip install uv` or `curl -LsSf https://astral.sh | sh`.

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd ml-train1
   ```

2. **Create a virtual environment and sync dependencies:**
   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```

3. **Run the API server:**
   ```bash
   uv run uvicorn app_api:app --host 0.0.0.0 --port 8000 --reload
   ```
   *The server will be available at `http://localhost:8000`*

### Option 2: Run with Docker 🐳

1. **Build the Docker image:**
   ```bash
   docker build -t titanic-ml-api .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 8000:8000 --name titanic-service titanic-ml-api
   ```

---

## 📡 API Documentation & Endpoints

Once the application is running, you can access the interactive Swagger UI documentation at:
🔗 **`http://localhost:8000/docs`**

### 1. Health Check
Verifies that the API and the ML model are properly loaded and working.

- **Method:** `GET`
- **Endpoint:** `/health`
- **Response Example (`200 OK`):**
  ```json
  {
    "status": "healthy",
    "model_loaded": true
  }
  ```

### 2. Predict Passenger Survival
Submits passenger features to the Decision Tree model to get a survival prediction.

- **Method:** `POST`
- **Endpoint:** `/predict`
- **Payload Example:**
  ```json
  {
    "Pclass": 3,
    "Sex": "male",
    "Age": 22.0,
    "SibSp": 1,
    "Parch": 0,
    "Fare": 7.25
  }
  ```
- **Response Example (`200 OK`):**
  ```json
  {
    "passenger_id": "optional_id",
    "survived": 0,
    "probability": 0.125
  }
  ```

### 3. Service Statistics
Returns runtime analytics showcasing the usage metrics of the microservice.

- **Method:** `GET`
- **Endpoint:** `/stats`
- **Response Example (`200 OK`):**
  ```json
  {
    "total_predictions_served": 142,
    "uptime_seconds": 3600
  }
  ```

---

## 📈 Model Training Info
The underlying model is a **Decision Tree Classifier** trained on the classic `titanic.csv` dataset. The training pipeline handles missing data imputation, categorical feature encoding (`Sex`, etc.), and exports the final binary model artifact into a deployment-ready serialized format (`model.pkl`).

*To re-run the training pipeline locally, check out the `train.ipynb` Jupyter Notebook.*
