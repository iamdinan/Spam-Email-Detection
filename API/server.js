// server.js
const express = require("express");
const axios = require("axios");

const app = express();
app.use(express.json());

app.post("/check", async (req, res) => {
  const text = req.body.text;

  try {
    const response = await axios.post("http://localhost:5000/predict", {
      text: text,
    });

    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: "Prediction failed" });
  }
});

app.listen(3000, () => {
  console.log("Node server running on http://localhost:3000");
});
