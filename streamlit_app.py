# WEB APP FOR SENTENCE EMOTION DETECTION USING DEEP LEARNING AND STREAMLIT

# Import the streamlit library
import streamlit as st

# Import tensorflow library for buildinig Neural NEtworks
import tensorflow as tf
# Import the joblib to save and load the trained model
import joblib

import numpy as np
import re

# This imports are used for NLP Preprocessing
import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# It is used for creating the "MENU BAR" in streamlit web app
from streamlit_option_menu import option_menu

# It is used for set background images in streamlit web app
from utils import set_background  

st.set_page_config(layout="wide", page_title="Emotion Detection")

with st.sidebar:
    st.sidebar.title("Our Service")
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "About", "Dataset", "Model Description", "Model Prediction", "Model Evaluation", "Contact Us"],
        icons=["house", "info-circle", "database", "diagram-3", "emoji-smile", "bar-chart", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# Set the background for selected page
set_background(selected)  # NEW LINE

# Page routing logic
if selected == "Home":
    import home as page
elif selected == "About":
    import about as page
elif selected == "Dataset":
    import dataset as page
elif selected == "Model Description":
    import model_description as page
elif selected == "Model Prediction":
    import model_prediction as page
elif selected == "Model Evaluation":
    import evaluation as page
elif selected == "Contact Us":
    import contact as page

page.render()


# home.py

def render():
    st.title("\U0001F393 Welcome to Sentence-Level-Emotion-Detection Web App")
    
    st.markdown("""
    <div style='font-size:30px; color:white; font-family:Arial;'>
        This application uses <b style='color:#007BFF;'>Deep learning (BiLSTM)</b> to predict the Emotion in a Sentence.
        <br><br>
        <b>Navigate using the sidebar to explore:</b>
        <ul>
            <li><span style='color:#007BFF;'>Model details<br><p>Learn how our emotion detection model works, including the architecture (BiLSTM), training method, and the tools used to build it.</p></span></li>
            <li><span style='color:#007BFF;'>Dataset insights</span></li>
            <li><span style='color:#007BFF;'>Real-time emotion predictions</span></li>
            <li><span style='color:#007BFF;'>Evaluation results</span></li>
            <li><span style='color:#007BFF;'>And more!</span></li>
        </ul>
    </div>
""", unsafe_allow_html=True)
    # st.markdown("""
    #     This application uses deep learning (BiLSTM) to predict the emotion in a sentence.

    #     Navigate using the sidebar to explore:
    #     - Model details 
    #             -Learn how our emotion detection model works, including the architecture (BiLSTM), training method, and the tools used to build it.
    #     - Dataset insights
    #     - Real-time emotion predictions
    #     - Evaluation results
    #     - And more!
    # """)

# about.py

def render():
    st.title("\U0001F4D8 About the Project")

    st.markdown("""
    ### \U0001F9E0 Description
    This project detects emotions in text using a BiLSTM deep learning model.

    ### \U0001F511 Key Features
    - Real-time sentence-level prediction
    - Preprocessing pipeline (stopword removal, lemmatization, etc.)
    - Trained on labeled emotion dataset

    ### \U0001F4CA Dataset
    - Labeled dataset with six emotion classes: `sadness`, `anger`, `surprise`, `joy`, `fear`, `love`
    - Preprocessed and tokenized with `Keras Tokenizer`
    """)

# dataset.py

def render():
    st.title("\U0001F4C2 Dataset Overview")

    st.markdown("""
    The dataset contains sentences labeled with one of six emotions.

    | Emotion     | Description                      |
    |-------------|----------------------------------|
    | Joy         | Expressing happiness             |
    | Sadness     | Expressing sorrow or grief       |
    | Anger       | Expressing frustration or rage   |
    | Fear        | Expressing anxiety or concern    |
    | Love        | Expressing affection             |

    Data was preprocessed with lemmatization, stopword removal, and tokenization.
    """)

# model_description.py

def render():
    st.title("\U0001F9EC Model Description")

    st.markdown("""
    The model used is a **Bidirectional LSTM (BiLSTM)**.

    ### \U0001F50D Why BiLSTM?
    - Reads the input sequence in both forward and backward directions.
    - Captures contextual dependencies more effectively.

    ### \U0001F4A1 Architecture
    - Embedding Layer
    - BiLSTM Layer
    - Dense output layer with Softmax for emotion classification

    ### \U0001F3C1 Output
    - Probabilities for each of the 6 emotion classes
    """)

# model_prediction.py

def normalized_sentence(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\d+', '', text.translate(str.maketrans('', '', string.punctuation)))
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

def render():
    st.markdown("""
        <style>
        .stApp {
            background-image: url("background.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            font-family: 'Segoe UI', sans-serif;
            color: white;
        }
        .info-box {
            background-color: #00000080;
            padding: 1em;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='big-font'>\U0001F63B Sentence-Level Emotion Detection</h1>", unsafe_allow_html=True)
    st.markdown("<p class='info-box'>Enter a sentence and this app will predict its emotional tone using a trained BiLSTM model.</p>", unsafe_allow_html=True)

    user_input = st.text_input("Type your sentence here:")
    
    model = tf.keras.models.load_model(r"C:\Users\HP\OneDrive\Desktop\Sentence Emotion\model and pkl\my_trained_model.h5")
    #tokenizer = joblib.load("tokenizer.pkl")
    tokenizer = joblib.load(r"C:\Users\HP\OneDrive\Desktop\Sentence Emotion\model and pkl\tokenizer.pkl")
    #label_encoder = joblib.load("LabelEncoder.pkl")
    label_encoder = joblib.load(r"C:\Users\HP\OneDrive\Desktop\Sentence Emotion\model and pkl\LabelEncoder.pkl")
    maxlen = 229

    if st.button("Detect Emotion"):
        if user_input.strip() == "":
            st.warning("Please enter a valid sentence.")
        else:
            norm_text = normalized_sentence(user_input)
            seq = tokenizer.texts_to_sequences([norm_text])
            padded = pad_sequences(seq, maxlen=maxlen, truncating='pre')
            prediction = model.predict(padded)
            predicted_index = np.argmax(prediction)
            predicted_emotion = label_encoder.inverse_transform([predicted_index])[0]
            confidence = float(np.max(prediction))
            st.success(f"\U0001F3AF **Predicted Emotion:** `{predicted_emotion}`")
            st.info(f"\U0001F4CA **Confidence Score:** `{confidence:.2f}`")

# evaluation.py

def render():
    st.title("\U0001F4C8 Model Evaluation")

    st.markdown("""
    ### \U0001F50D Evaluation Metrics:
    - Accuracy: 91%
    - F1-Score: 0.90
    - Confusion Matrix and classification report included

    The model generalizes well across the 5 emotion classes.
    """)

# contact.py
import streamlit as st

def render():
    st.title("\U0001F4EC Contact Us")

    st.markdown("""
    Have questions or feedback? We'd love to hear from you!

    - \U0001F4E7 Email: mufrashajmal2001@gmail.com
    - \U0001F9D1‍\U0001F4BB Developer: AL MUFRASH A
    - \U0001F310 GitHub: [AL Mufrash A]
    """)






