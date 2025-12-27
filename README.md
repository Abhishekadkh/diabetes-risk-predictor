# Diabetes Risk Predictor 💉

A **Streamlit web application** that predicts the **risk of diabetes** based on user health metrics using a pre-trained **machine learning pipeline**. This project demonstrates data preprocessing, model training, and a fully interactive web interface for easy predictions.

---

## 🔗 Repository

[GitHub Repository](https://github.com/Abhishekadkh/diabetes-risk-predictor.git)

---

## 🧰 Features

* Interactive **Streamlit interface** for inputting health metrics.
* Predicts **high or low diabetes risk** with **probability score**.
* **Pre-trained Logistic Regression model** for reliable predictions.
* **Neat two-column layout** and **progress bar** for probability visualization.
* Fully self-contained, runs locally using `streamlit run app.py`.

---

## 📦 Project Structure

```
diabetes-risk-predictor/
├── app.py                     # Streamlit application
├── artifacts/
│   └── diabetes_pipeline.pkl  # Pre-trained ML pipeline
├── assets/
│   └── img.jpg                # Optional image/logo for app
├── requirements.txt           # Python dependencies
└── README.md                  # Project description
```

---

## ⚡ Quick Start

Follow these steps to run the application locally:

1. **Clone the repository**

```bash
git clone https://github.com/Abhishekadkh/diabetes-risk-predictor.git
cd diabetes-risk-predictor
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

4. **Open in browser**

Streamlit will open a local web server (usually at `http://localhost:8501`) where you can enter your health information and check your diabetes risk.

---

## 🩺 Input Parameters

The app requires the following metrics:

* **Pregnancies** – Number of times pregnant
* **Glucose** – Plasma glucose level
* **Blood Pressure** – Diastolic blood pressure (mm Hg)
* **Skin Thickness** – Triceps skinfold thickness (mm)
* **Insulin** – 2-Hour serum insulin (mu U/ml)
* **BMI** – Body Mass Index (weight in kg/(height in m)^2)
* **Diabetes Pedigree Function (DPF)** – Genetic diabetes risk factor
* **Age** – Age in years

---

## 📊 How It Works

1. The app collects user input through **number input fields** in a **two-column layout**.
2. Data is **passed to the pre-trained ML pipeline** (`diabetes_pipeline.pkl`) for prediction.
3. Displays:

   * **Risk category**: High or Low
   * **Probability**: Numeric percentage
   * **Visual feedback**: Progress bar for intuitive understanding

---

## 🛠️ Dependencies

Key Python libraries:

* `streamlit`
* `numpy`
* `pandas`
* `scikit-learn`
* `joblib`

All dependencies are listed in `requirements.txt`.

---

## ⚡ Contribution

This project is maintained by **Abhishek Adhikari**.
Feel free to **fork the repository**, **open issues**, or **submit pull requests** for improvements.

---

## 📄 License

This repository is **open-source** and free to use for educational and personal projects.
