# app.py
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("spam_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["text"]
    result = model.predict([data])[0]
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(port=5000)