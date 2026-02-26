# Loan Approval Prediction System

## 🚀 Project Overview
This project predicts loan approval status using a Machine Learning model.
The model is deployed using FastAPI and integrated with a Streamlit frontend and at last containerized using Docker for production-ready deployment.

## 🧠 Tech Stack
- Python
- Scikit-learn
- FastAPI
- Streamlit
- Uvicorn
- Docker

## 🏗 Architecture
Streamlit (Frontend) → FastAPI (Backend API) → ML Pipeline Model → Docker

## ▶️ How to Run

### 1️⃣ Install dependencies
pip install -r requirements.txt

### 2️⃣ Run FastAPI
uvicorn api:app --reload

### 3️⃣ Run Streamlit
streamlit run frontend.py

## 🐳 Run Using Docker

## 1️⃣ Build Docker Image
docker build -t adnan78630/minorproject_ml:supervised_updated .

## 2️⃣ Run Docker Container
docker run -p 8000:8000 adnan78630/minorproject_ml:supervised_updated

## API will be available at:
http://localhost:8000

## 📊 Features
- Real-time prediction
- Pipeline-based preprocessing
- REST API deployment
- Interactive UI
- Docker containerization for scalable deployment
