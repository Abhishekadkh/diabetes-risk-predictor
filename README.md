# Diabetes Risk Predictor 🩺

A machine learning–based web application that predicts the **risk of diabetes** using patient health indicators.
The application is built with **Python, scikit-learn, and Streamlit**, and is intended for **educational and academic demonstration purposes**.

---

## 📌 Project Overview

This project uses a trained machine learning pipeline to predict whether a person is at **high or low risk of diabetes** based on standard medical features such as glucose level, BMI, age, insulin level, and more.

The application provides:

* A clean Streamlit web interface
* Risk prediction with probability score
* Simple and reproducible setup

---

## ⚠️ Disclaimer

> **This application is for educational and learning purposes only.**
> It is **not a medical diagnostic tool** and **must not** be used for real medical decision-making or treatment.
> Always consult a qualified healthcare professional for medical advice.

---

## 🧠 Features

* Interactive Streamlit UI
* Machine Learning pipeline inference
* Probability-based prediction output
* Lightweight and easy to deploy
* No external APIs or sensitive data usage

---

## 📂 Repository Structure

```
diabetes-risk-predictor/
│
├── app.py                     # Streamlit application
├── requirements.txt           # Python dependencies
├── artifacts/
│   └── diabetes_pipeline.pkl  # Trained ML pipeline
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Abhishekadkh/diabetes-risk-predictor.git
cd diabetes-risk-predictor
```

---

### 2️⃣ Create a Virtual Environment (Recommended)

#### ▶ Linux / macOS

```bash
python3 -m venv venv
```

#### ▶ Windows

```powershell
python -m venv venv
```

---

### 3️⃣ Activate the Virtual Environment

#### ▶ Linux / macOS

```bash
source venv/bin/activate
```

#### ▶ Windows (PowerShell)

```powershell
venv\Scripts\Activate
```

> You should see `(venv)` in your terminal once activated.

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

The application will open automatically in your browser, typically at:

```
http://localhost:8501
```

---

## 📊 Model Details

* Dataset: Pima Indians Diabetes Dataset

* Algorithm: scikit-learn pipeline

* Input Features:

  * Pregnancies
  * Glucose
  * Blood Pressure
  * Skin Thickness
  * Insulin
  * BMI
  * Diabetes Pedigree Function
  * Age

* Output:

  * Risk classification (High / Low)
  * Prediction probability

---

## 🔐 Security & Privacy

* No user data is stored
* No authentication or API keys
* No external network calls
* Safe to run locally and safe to make public

---

## 📜 License

This project is released for **educational and academic use**.
Feel free to fork, learn, and improve upon it.

---

## 👤 Author

**Abhishek Adhikari**
---
