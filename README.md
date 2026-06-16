# Spam Email Detection

## Overview

This project is a simple spam email detection app built with two services:

- a **Python Flask API** that loads a trained machine learning model and returns predictions
- a **Node.js (Express) API** that receives requests from the client and forwards them to the Python service

The model is trained using a Naive Bayes classifier with TF-IDF vectorization and saved as a local `.pkl` file.

## Project Structure

- [API/](API/) - Node.js Express server that exposes the `/check` endpoint
- [ML_Model/](ML_Model/) - Python model training and Flask prediction service
- [README.md](README.md) - Project overview and setup guide

## How It Works

1. A request is sent to the Node.js API at `/check`.
2. The Node.js server forwards the text to the Flask service at `/predict`.
3. The Flask app loads the `spam_model.pkl` and returns a `spam` or `not spam` prediction.

## Tech Stack

- **ML Model:** Python, Scikit-learn, Pandas, Joblib, Flask
- **API:** Node.js, Express, Axios

## Setup

### Prerequisites

- Python 3.x
- Node.js & npm

### 1. Train the model

From the [ML_Model/](ML_Model/) folder, install dependencies (if any) and run:

```bash
python train.py
```

This creates `spam_model.pkl` in the same folder and prints the model accuracy.

### 2. Start the Python API

From the [ML_Model/](ML_Model/) folder, run:

```bash
python app.py
```

The Flask service runs on port `5000`.

### 3. Start the Node.js API

From the [API/](API/) folder, install dependencies and start the server:

```bash
npm install
npm start
```

The Node server runs on port `3000`.

## API Endpoint

### `POST /check`

**Request body:**

```json
{
  "text": "Get a free thousand dollar gift card now!"
}
```

**Response:**

```json
{
  "prediction": "spam"
}
```

## Notes

- The dataset `spam_mail_dataset.csv` is used for training the model.
- For better accuracy, train the model on a larger dataset or use more advanced techniques.
