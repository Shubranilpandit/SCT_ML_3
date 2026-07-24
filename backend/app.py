# ============================================================
# Cats vs Dogs Flask Backend
# ============================================================

import os

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

from predict import predict_random_image

# ============================================================
# Flask App
# ============================================================

app = Flask(__name__)

# Enable CORS
CORS(app)

# ============================================================
# Paths
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGE_FOLDER = os.path.join(BASE_DIR, "evaluation_images")

# ============================================================
# Home Route
# ============================================================

@app.route("/")
def home():

    return jsonify({
        "message": "Cats vs Dogs Backend Running Successfully!"
    })

# ============================================================
# Prediction Route
# ============================================================

@app.route("/predict", methods=["GET"])
def predict():

    result = predict_random_image()

    result["image_url"] = f"http://127.0.0.1:5000/images/{result['filename']}"

    return jsonify(result)

# ============================================================
# Serve Images
# ============================================================

@app.route("/images/<filename>")
def get_image(filename):

    return send_from_directory(
        IMAGE_FOLDER,
        filename
    )

# ============================================================
# Run App
# ============================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )