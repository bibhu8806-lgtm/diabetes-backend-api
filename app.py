from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


def is_valid_api_key(req):
    user_key = req.headers.get("X-API-Key")
    return user_key == API_KEY


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Diabetes Risk Predictor Backend API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    if not is_valid_api_key(request):
        return jsonify({
            "error": "Invalid or missing API key"
        }), 401

    data = request.get_json()

    glucose = data.get("glucose")
    blood_pressure = data.get("blood_pressure")
    bmi = data.get("bmi")
    age = data.get("age")

    if glucose is None or blood_pressure is None or bmi is None or age is None:
        return jsonify({
            "error": "Required fields: glucose, blood_pressure, bmi, age"
        }), 400

    risk_score = 0

    if glucose > 140:
        risk_score += 1

    if blood_pressure > 90:
        risk_score += 1

    if bmi > 30:
        risk_score += 1

    if age > 45:
        risk_score += 1

    if risk_score >= 2:
        prediction = "High Diabetes Risk"
    else:
        prediction = "Low Diabetes Risk"

    return jsonify({
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "bmi": bmi,
        "age": age,
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)
