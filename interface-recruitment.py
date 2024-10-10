import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression

# Function for encoding categorical columns
def encode_inputs(gender, education_level):
    # Encode gender
    gender_map = {'Male': 0, 'Female': 1}
    gender_encoded = gender_map[gender]

    # Encode education level
    education_map = {
        "Diploma's": 1,
        "Bachelor's": 2,
        "Master's": 3,
        "PhD": 4
    }
    education_encoded = education_map[education_level]

    return gender_encoded, education_encoded

# Load the pre-trained logistic regression model
def load_model(model_path='recuirement_model.sav'):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Streamlit app
st.title('Logistic Regression Model Interface: HR Recruitment')

# Input fields for continuous variables
age = st.number_input('Age', min_value=20, max_value=100, value=25, help='Masukkan umur kandidat dalam tahun.')
experience_years = st.number_input('Experience Years', min_value=0, max_value=15, value=5, help='Masukkan jumlah tahun pengalaman kerja kandidat.')
previous_companies = st.number_input('Previous Companies', min_value=0, max_value=5, value=2, help='Jumlah perusahaan tempat kandidat bekerja sebelumnya.')
distance_from_company = st.number_input('Distance From Company', min_value=0.0, max_value=100.0, value=10.0, help='Jarak antara tempat tinggal kandidat dan lokasi perusahaan (dalam kilometer).')
skill_score = st.slider('Skill Score', min_value=0, max_value=100, value=70, help='Penilaian keterampilan teknis kandidat dalam skala 0-100.')
personality_score = st.slider('Personality Score', min_value=0, max_value=100, value=80, help='Penilaian ciri-ciri kepribadian kandidat dalam skala 0-100.')

# Dropdown for categorical variables
gender = st.selectbox('Gender', options=['Male', 'Female'], help='Pilih jenis kelamin kandidat.')
education_level = st.selectbox('Education Level', options=["Diploma's", "Bachelor's", "Master's", "PhD"], help='Pilih tingkat pendidikan tertinggi yang dicapai oleh kandidat.')

# Encode categorical inputs
gender_encoded, education_encoded = encode_inputs(gender, education_level)

# Prepare data for prediction
input_data = np.array([[age, gender_encoded, education_encoded, experience_years, 
                        previous_companies, distance_from_company, skill_score, personality_score]])

# Load the logistic regression model
model = load_model()

# Predict on user input
if st.button('Prediksi Keputusan Rekrutmen'):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success('Kandidat dinyatakan lolos rekrutmen')
    else:
        st.error('Kandidat dinyatakan tidak lolos rekrutmen')
    