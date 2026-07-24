# ============================================================
# Cats vs Dogs Prediction Module
# ============================================================

import os
import random

import cv2
import joblib
import numpy as np

from skimage.feature import hog


# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "svm_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")
IMAGE_FOLDER = os.path.join(BASE_DIR, "evaluation_images")


# ------------------------------------------------------------
# Load Model
# ------------------------------------------------------------

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


# ------------------------------------------------------------
# Image Size
# ------------------------------------------------------------

IMAGE_SIZE = (64, 64)


# ------------------------------------------------------------
# Prediction Function
# ------------------------------------------------------------

def predict_random_image():

    image_name = random.choice(os.listdir(IMAGE_FOLDER))

    image_path = os.path.join(IMAGE_FOLDER, image_name)

    original_image = cv2.imread(image_path)

    image = cv2.resize(original_image, IMAGE_SIZE)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = image / 255.0

    feature = hog(
        image,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm="L2-Hys"
    )

    feature = scaler.transform([feature])

    prediction = model.predict(feature)[0]

    predicted_label = "Cat" if prediction == 0 else "Dog"

    actual_label = "Cat" if image_name.startswith("cat") else "Dog"

    return {
        "filename": image_name,
        "prediction": predicted_label,
        "actual": actual_label,
        "correct": predicted_label == actual_label
    }