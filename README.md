# Spam Email Detection

## Overview

This project is a simple spam email detection app built with two services:

- a Python Flask API that loads a trained machine learning model and returns predictions
- a Node.js API that receives requests from the client and forwards them to the Python service

The model is trained on a small sample dataset and saved as a local `.pkl` file.

## Project Structure

- `API/` - Node.js server that exposes the `/check` endpoint
- `ML_Model/` - Python model training and prediction service
- `README.md` - project overview and setup guide

## How It Works

1. A request is sent to the Node.js API at `/check`.
2. The Node.js server forwards the text to the Flask service at `/predict`.
3. The Flask app loads the trained model and returns a spam or not spam prediction.

## Setup

### 1. Train the model

From the `ML_Model/` folder, run:

```bash
python train.py
```

This creates `spam_model.pkl` in the same folder.

### 2. Start the Python API

From the `ML_Model/` folder, run:

```bash
python app.py
```

The Flask service runs on port `5000`.

### 3. Start the Node.js API

From the `API/` folder, run:

```bash
npm start
```

The Node server runs on port `3000`.

## API Endpoint

### `POST /check`

Request body:

```json
{
  "text": "free money now"
}
```

Response:

```json
{
  "prediction": "spam"
}
```

## Notes

- The dataset in this project is very small and meant for learning and testing.
- For better accuracy, train the model on a larger spam dataset.
