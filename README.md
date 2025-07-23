# 🤖 Specura: Integrated AI System for Optimizing Employee Recruitment & Selection

Welcome to **Specura**, an AI-powered recruitment solution designed to streamline hiring processes, minimize bias, and build superior human resources through machine learning. Built as part of a scientific paper for IESTF 2024 by Universitas Singaperbangsa Karawang.

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

The dataset used was sourced from Kaggle: [ML for HR: Employee Recruitment Modeling](https://www.kaggle.com)  
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

## 📊 Result & Evaluation

- **Recall (Class 1 / Potential Candidate)**: 87%
- **Precision (Class 1)**: 62%
- **Confusion Matrix**:

