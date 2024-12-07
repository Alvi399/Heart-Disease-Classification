from tensorflow.keras.models import load_model
import streamlit as st
import pandas as pd
import numpy as np

# Judul aplikasi
st.title('Heart Disease Prediction')
st.write('''
This app predicts the **Heart Disease**!
''')

# Sidebar untuk input pengguna
st.sidebar.header('User Input Parameters')
def user_input_features():
    age = st.sidebar.slider('Age', 29, 77, 37)
    sex = st.sidebar.selectbox('Sex', (0, 1))
    cp = st.sidebar.slider('Chest Pain Type', 0, 3, 1)
    trestbps = st.sidebar.slider('Resting Blood Pressure', 94, 200, 120)
    chol = st.sidebar.slider('Serum Cholesterol', 126, 564, 200)
    fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', (0, 1))
    restecg = st.sidebar.selectbox('Resting Electrocardiographic Results', (0, 1, 2))
    thalach = st.sidebar.slider('Maximum Heart Rate Achieved', 71, 202, 150)
    exang = st.sidebar.selectbox('Exercise Induced Angina', (0, 1))
    oldpeak = st.sidebar.slider('ST Depression Induced by Exercise', 0.0, 6.2, 1.0)
    slope = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', (0, 1, 2))
    ca = st.sidebar.slider('Number of Major Vessels Colored by Fluoroscopy', 0, 4, 0)
    thal = st.sidebar.selectbox('Thalassemia', (0, 1, 2, 3))

    data = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input Parameters')
st.write(df)

# Load model
model = load_model('./model_heart_disease_classification.keras')

# Predict
prediction_proba = model.predict(df)
prediction = (prediction_proba > 0.5).astype(int)  # Threshold 0.5 for binary classification

# Output prediction and probabilities
st.subheader('Prediction')
heart_disease = np.array(['No Heart Disease', 'Heart Disease'])
st.write(heart_disease[prediction[0][0]])  # Output as label

st.subheader('Prediction Probability')
st.write(prediction_proba[0][0])  # Show the probability
