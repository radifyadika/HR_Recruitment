# 🤖 Specura: Integrated AI System for Optimizing Employee Recruitment & Selection

Welcome to **Specura**, an AI-powered recruitment solution designed to streamline hiring processes, minimize bias, and build superior human resources through machine learning. Built as part of a scientific paper for IESTF 2024 by Universitas Singaperbangsa Karawang.

---

## 🧠 Research Flow

Flowchart for Developing a Machine Learning Model for Employee Recruitment

![Research Flow](./assets/Research%20flow.png)

---
## 📌 Problem Statement

In the digital era, manual recruitment is no longer efficient—it's slow, biased, and costly. With hundreds of applicants per job posting, HR departments face difficulty filtering candidates objectively and effectively. The challenge is to design a system that:

- Reduces the time and cost required in recruitment,
- Minimizes human bias during candidate evaluation,
- Ensures alignment with business needs and dynamic industry standards.

---

## 🎯 Objective

The objectives of Specura are:

- ⏱️ **Enhance Efficiency**: Automate recruitment and selection processes with AI.
- 🎯 **Increase Accuracy**: Select the most suitable candidates based on data-driven insights.
- ⚖️ **Minimize Bias**: Reduce subjective judgment from HR decisions.
- 💸 **Reduce Costs**: Save operational expenses in recruitment efforts.

---

## 🧠 Dataset & Features

The dataset used was sourced from Kaggle: [ML for HR: Employee Recruitment Modeling](https://www.kaggle.com/datasets/rabieelkharoua/predicting-hiring-decisions-in-recruitment-data)

Total records: **1,500 samples**  
Target variable: `Decision` (0 = Not Potential, 1 = Potential)

| Feature Name           | Description                                      | Data Type  |
|------------------------|--------------------------------------------------|------------|
| Age                   | Age of the candidate                              | Numeric    |
| Gender                | Gender (Male/Female)                              | Categorical|
| EducationLevel        | Highest education attained                        | Ordinal    |
| ExperienceYears       | Years of professional experience                  | Numeric    |
| PreviousCompanies     | Number of previously worked companies             | Numeric    |
| DistanceFromCompany   | Distance between candidate's home and workplace  | Numeric    |
| SkillScore            | Scored rating of technical skills                 | Numeric    |
| PersonalityScore      | Scored rating of personality assessment           | Numeric    |
| RecruitmentStrategy   | Strategy used to recruit candidate                | Categorical|
| Decision              | Final hiring decision                             | Binary     |

📝 *Note: “RecruitmentStrategy” was excluded from modeling due to low relevance.*

---

## 🏗️ Modelling

- **Algorithm**: Logistic Regression
- **Preprocessing**:
  - Handling missing values
  - Encoding categorical variables
  - Feature selection via correlation analysis
- **Evaluation**:
  - Confusion Matrix
  - Classification Report
  - 5-Fold Cross Validation

| Fold | Accuracy (%) |
|------|--------------|
| 1    | 82.62        |
| 2    | 83.23        |
| 3    | 82.01        |
| 4    | 81.09        |
| 5    | 85.36        |

✅ **Best Accuracy** after tuning: **81%**

---


- **Key Insight**:
  - Model is very strong in identifying **non-potential** candidates (94% precision on class 0)
  - Needs improvement in **precision** for potential candidates (62%)

📈 *Model deployed via Streamlit with a user-friendly interface to input candidate profiles and display predictions.*

---

## ✅ Conclusion

Specura successfully achieves its goal to:
- Optimize recruitment workflow
- Reduce subjective decision-making
- Recommend best-fit candidates based on ML insights

With 81% model accuracy, Specura is a promising step toward **fairer, faster, and smarter** hiring.

---

## ⚠️ Disclaimer

This project is a prototype built for academic purposes. The data and model performance are subject to further development. For real-world deployment, additional validation, larger datasets, and fairness auditing are recommended.

---

## 🚀 Live Demo

🖥️ [Streamlit Application (Insert Link Here)](https://your-streamlit-app-link)

---

## 📬 Contact Me

- 📧 Email: 2110631140106@student.unsika.ac.id  
- 💼 LinkedIn: [Radif Ramadan](https://www.linkedin.com/in/your-link)  
- 📸 Instagram: [@radif.ramadan](https://instagram.com/your-handle)

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## 📁 Repository Structure


