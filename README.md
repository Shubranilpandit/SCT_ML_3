# 🐱🐶 Cats vs Dogs Image Classification using Support Vector Machine (SVM)

## 📌 Task 3 - SkillCraft Technology Machine Learning Internship

This project is developed as part of the **SkillCraft Technology Machine Learning Internship**.

The objective of this task is to build an **Image Classification Model** that classifies images as either **Cat** or **Dog** using **Histogram of Oriented Gradients (HOG)** for feature extraction and a **Support Vector Machine (SVM)** classifier. The trained model is deployed through a **Flask Web Application** with an interactive frontend.

---

# 📖 Project Overview

Image classification is one of the fundamental applications of Machine Learning and Computer Vision.

In this project:

- Images are preprocessed and resized.
- HOG (Histogram of Oriented Gradients) extracts important edge and shape features.
- A Support Vector Machine (SVM) classifier learns the differences between cats and dogs.
- The trained model is deployed using Flask.
- A modern frontend allows users to generate random evaluation images and instantly view predictions.

---

# 🎯 Objective

Build an image classifier capable of distinguishing between cats and dogs by applying classical Machine Learning techniques instead of Deep Learning.

---

# ✨ Features

- Dataset preprocessing
- Exploratory Data Analysis (EDA)
- Balanced training dataset
- Image preprocessing
- HOG Feature Extraction
- Support Vector Machine (SVM) Classification
- Model Evaluation
- Confusion Matrix
- Classification Report
- Model Serialization using Joblib
- Flask Backend API
- Interactive Frontend
- Random Image Prediction
- Responsive User Interface

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- OpenCV
- NumPy
- Pandas
- Scikit-image

## Backend

- Flask

## Frontend

- HTML
- CSS
- JavaScript

## Model Saving

- Joblib

---

# 📂 Project Structure

```text
TASK-3
│
├── backend
│   ├── app.py
│   ├── predict.py
│   ├── requirements.txt
│   │
│   ├── evaluation_images
│   ├── models
│   │   ├── svm_model.pkl
│   │   └── scaler.pkl
│   │
│   ├── notebooks
│   │   └── svm_cat_dog.ipynb
│   │
│   └── uploads
│
├── frontend
│   ├── css
│   │   └── style.css
│   │
│   ├── js
│   │   └── script.js
│   │
│   └── index.html
│
├── screenshot
│   ├── home.png
│   ├── prediction1.png
│   └── prediction2.png
│
├── README.md
└── LICENSE
```

---

# 📊 Machine Learning Workflow

```
Dataset
     │
     ▼
Data Exploration
     │
     ▼
Image Preprocessing
     │
     ▼
Resize Images (64×64)
     │
     ▼
Grayscale Conversion
     │
     ▼
Normalization
     │
     ▼
HOG Feature Extraction
     │
     ▼
Train-Test Split
     │
     ▼
Feature Scaling
     │
     ▼
Support Vector Machine
     │
     ▼
Model Evaluation
     │
     ▼
Save Model
     │
     ▼
Flask Deployment
```

---

# 🧠 Feature Extraction

This project uses **Histogram of Oriented Gradients (HOG)** to extract meaningful image features.

HOG captures:

- Edge information
- Shape information
- Object structure

These features are then used by the Support Vector Machine for classification.

---

# 🤖 Machine Learning Model

**Algorithm**

Support Vector Machine (SVM)

**Kernel Used**

- Radial Basis Function (RBF)

**Feature Extraction**

- Histogram of Oriented Gradients (HOG)

---

# 📈 Model Evaluation

The trained model is evaluated using:

- Accuracy Score
- Classification Report
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 🌐 Web Application

The Flask application provides an interactive interface where users can:

- Generate a random evaluation image
- View the predicted class
- Compare predicted and actual labels
- Check prediction correctness
- Visualize the selected image

---

# 📸 Project Screenshots

## Home Page
<img width="1920" height="1080" alt="home" src="https://github.com/user-attachments/assets/ab416a02-c668-440c-a0e0-fd97c4ffcd04" />

---

## Prediction Example 1
<img width="1920" height="1080" alt="prediction1" src="https://github.com/user-attachments/assets/20d64b1a-6431-4458-82eb-8ec2506258b9" />

---

## Prediction Example 2
<img width="1920" height="1080" alt="prediction2" src="https://github.com/user-attachments/assets/150f17f6-2fc8-460d-aee6-a6a876fea6de" />

---

## Run Flask Backend

```bash
cd backend

python app.py
```

---

## Open Frontend

Open

```
frontend/index.html
```

using Live Server or your preferred local server.

---

# 📚 Libraries Used

- NumPy
- Pandas
- OpenCV
- Matplotlib
- Scikit-learn
- Scikit-image
- Flask
- Joblib

---

# ⭐ Acknowledgements

- SkillCraft Technology
- Kaggle Dogs vs Cats Dataset
- Scikit-learn
- Flask
- OpenCV

---

If you found this project helpful, consider giving this repository a ⭐ on GitHub.
