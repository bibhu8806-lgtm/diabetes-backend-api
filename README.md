# Diabetes Risk Predictor Backend API

This is a simple Flask backend API project for predicting diabetes risk based on health parameters.

## Features

- REST API using Flask
- API key authentication
- Predicts High or Low Diabetes Risk
- Uses environment variable for API key security

## Tech Used

- Python
- Flask
- python-dotenv

## API Endpoint

### Home

GET /

### Predict

POST /predict

Headers:

X-API-Key: your_api_key

Body:

{
  "glucose": 150,
  "blood_pressure": 95,
  "bmi": 32,
  "age": 50
}

Response:

{
  "prediction": "High Diabetes Risk"
}

## Setup

Install dependencies:

pip install -r requirements.txt

Create .env file:

API_KEY=your_api_key_here

Run project:

python app.py
