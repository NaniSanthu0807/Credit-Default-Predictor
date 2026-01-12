# Credit Card Default Prediction

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-orange)
![Scikit-learn](https://img.shields.io/badge/Library-Scikit--learn-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

Predicting credit card default risk using customer demographics, credit information, and historical payment behavior.

---

## 📌 Overview
This project aims to predict whether a credit card customer will **default on payment in the next month**.  
It uses real-world financial data and machine learning techniques to support **credit risk assessment**.

The dataset is sourced from the **UCI Machine Learning Repository** and contains data from credit card clients in Taiwan.

---

## 📊 Dataset Information
- **Source:** UCI Machine Learning Repository  
- **Time Period:** April 2005 – September 2005  
- **Total Records:** 30,000  
- **Total Features:** 25  
- **Target Variable:** `default.payment.next.month`  
  - `1` → Default  
  - `0` → No Default  

### Feature Categories
- **Demographic:** Sex, Education, Marital Status, Age  
- **Credit Information:** Credit Limit  
- **Payment History:** `PAY_0` to `PAY_6`  
- **Bill Statements:** `BILL_AMT1` to `BILL_AMT6`  
- **Previous Payments:** `PAY_AMT1` to `PAY_AMT6`  

---

## 🎯 Problem Statement
To build a machine learning model that predicts the probability of credit card default in the next month, with special emphasis on identifying **high-risk customers**.

---

## ⚙️ Tech Stack
- **Language:** Python  
- **Libraries:**  
  - NumPy  
  - Pandas  
  - Scikit-learn  
  - Matplotlib  
  - Seaborn  

---

## 🧠 Methodology
1. Data loading and cleaning  
2. Exploratory Data Analysis (EDA)  
3. Feature selection and preprocessing  
4. Train-test split  
5. Model training  
6. Model evaluation  

---

## 🤖 Model Used
### Decision Tree Classifier
The Decision Tree was chosen as a baseline model due to:
- Interpretability  
- Ability to model non-linear relationships  
- Suitability for structured tabular data  

---

## 📈 Model Performance
Because the dataset is **imbalanced**, multiple metrics were used.

| Metric | Score |
|------|------|
| Accuracy | **83.4%** |
| Precision | Evaluated |
| Recall | Evaluated |
| F1-Score | Evaluated |
| ROC-AUC | Evaluated |

> **Note:** Recall for defaulters (Class = 1) was prioritized, as missing a default can lead to financial loss.

---

## 🔍 Key Insights
- Recent payment behavior (`PAY_0`, `PAY_2`, `PAY_3`) is the strongest predictor of default.
- Customers with higher recent delays are significantly more likely to default.
- Credit limit and recent payment amounts also play an important role.

---

## 📁 Project Structure
