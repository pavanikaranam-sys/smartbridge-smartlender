# 🏦 Smart Lender - Loan Approval Prediction System


## 🖇️ App link - https://smartlender-smartbridge.onrender.com

---

## 📌 Overview

Smart Lender is a Machine Learning-powered web application that predicts whether a loan application is likely to be approved based on applicant details. The system helps banks and financial institutions make faster, data-driven loan approval decisions by analyzing applicant information using a trained machine learning model.

The application is built using **Python**, **Flask**, and **Scikit-learn**, with a simple and user-friendly web interface for real-time predictions.

---

## ✨ Key Features

- Predicts loan approval instantly
- Interactive web application using Flask
- User-friendly interface for data entry
- Data preprocessing and feature engineering
- Multiple machine learning models comparison
- Real-time prediction using the best-performing model
- Deployable on cloud platforms like Render or IBM Cloud

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML5
- CSS3
- Bootstrap

---

## 🤖 Machine Learning Models Evaluated

The following classification algorithms were trained and evaluated:

- Decision Tree
- Random Forest ⭐ (Selected Model)
- K-Nearest Neighbors (KNN)
- XGBoost

After comparing model performance, **Random Forest** was selected for deployment due to its balanced training and testing accuracy.

---

## 📊 Model Performance

| Model | Training Accuracy | Testing Accuracy |
|--------|------------------:|-----------------:|
| Random Forest | 70.88% | 70.60% |
| Decision Tree | 100.00% | 57.50% |
| K-Nearest Neighbors | 73.40% | 63.40% |
| XGBoost | 94.00% | 63.90% |

---

## 📁 Project Structure

```
Smart-Lender/
│
├── app.py
├── loan_prediction_model.pkl
├── requirements.txt
├── smart_lender.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## ▶️ Installation & Execution

### 1️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Flask Application

```bash
python app.py
```

### 3️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📋 Input Features

The application accepts the following applicant details:

- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Gender
- Marital Status
- Number of Dependents
- Education
- Self Employment Status
- Property Area

---

## 🎯 Prediction Output

Based on the provided information, the application predicts:

- ✅ Loan Approved
- ❌ Loan Rejected

---

## 🌐 Deployment

The application is deployed using:

- Render

---

## 📸 Application Screens

- Loan Prediction Form
- Prediction Result

---

## 👩‍💻 Developed By

**Pavani Karanam**

Machine Learning Project – Smart Lender Loan Approval Prediction System
