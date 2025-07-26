import streamlit as st

from utils import set_background
# Use the correct image for each page

set_background("C:/Users/HP/OneDrive/Desktop/Sentence Emotion/background_home.jpeg")
#set_background("background_home.jpeg")

import tensorflow as tf
import numpy as np
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.sequence import pad_sequences



nltk.download('stopwords')
nltk.download('wordnet')

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
    # # Sticky header CSS
    # st.markdown("""
    #     <style>
    #     .header {
    #         position: fixed;
    #         top: 0;
    #         left: 0;
    #         width: 100%;
    #         background-color: #f0f0f0;
    #         color: #333;
    #         text-align: center;
    #         padding: 20px;
    #         font-size: 20px;
    #         font-weight: bold;
    #         box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    #         z-index: 1000;
    #     }
    #     .main-content {
    #         padding-top: 100px; /* space below header */
    #     }
    #     </style>

    #     <div class="header">
    #         Welcome to Sentence-Level-Emotion-Detection Web App
    #     </div>
    # """, unsafe_allow_html=True)

    # Background and font
    st.markdown("""
        <style>
        .stApp {
            background-image: url("C:/Users/HP/OneDrive/Desktop/Sentence Emotion/background_home.jpeg")
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

    st.markdown("<h1 class='big-font'>🎭 Sentence-Level Emotion Detection</h1>", unsafe_allow_html=True)
    st.markdown("<p class='info-box'><b>Enter a sentence and this app will predict its emotional tone using a trained BiLSTM model.</b></p>", unsafe_allow_html=True)

    user_input = st.text_area("Type your sentence here:", height=150)

    # Initialize session state for button status
    if "button_disabled" not in st.session_state:
        st.session_state.button_disabled = False

    maxlen = 229

    # Load model and files only once (outside button for performance)
    @st.cache_resource
    def load_model_and_utils():
        model = tf.keras.models.load_model(r"C:\Users\HP\OneDrive\Desktop\Sentence Emotion\model and pkl\my_trained_model.h5")
        tokenizer = joblib.load(r"C:\Users\HP\OneDrive\Desktop\Sentence Emotion\model and pkl\tokenizer.pkl")
        label_encoder = joblib.load(r"C:\Users\HP\OneDrive\Desktop\Sentence Emotion\model and pkl\LabelEncoder.pkl")
        return model, tokenizer, label_encoder

    model, tokenizer, label_encoder = load_model_and_utils()

    # Detect Button
    if st.button("Detect Emotion", disabled=st.session_state.button_disabled):
        st.session_state.button_disabled = True  # Disable button while processing
        user_input = user_input.strip()

        if user_input == "":
            st.warning("⚠️ Please enter a valid sentence.")
            st.session_state.button_disabled = False  # Re-enable after warning
        else:
            with st.spinner("🔄 Analyzing emotion..."):
                try:
                    norm_text = normalized_sentence(user_input)
                    seq = tokenizer.texts_to_sequences([norm_text])

                    if not any(seq):  # All unknown words
                        st.error("❌ Sorry! Couldn't recognize any known words in the input.")
                    else:
                        padded = pad_sequences(seq, maxlen=maxlen, truncating='pre')
                        prediction = model.predict(padded)
                        predicted_index = np.argmax(prediction)
                        predicted_emotion = label_encoder.inverse_transform([predicted_index])[0]
                        confidence = float(np.max(prediction))

                        st.success(f"🎯 **Predicted Emotion:** `{predicted_emotion}`")
                        #st.info(f"📊 **Confidence Score:** `{confidence:.2f}`")
                except Exception as e:
                    st.error(f"⚠️ Error during prediction: {e}")

            st.session_state.button_disabled = False  # Re-enable after processing

    # Sticky footer
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f0f0f0;
            color: #333;
            text-align: center;
            padding: 20px;
            font-size: 16px;
            box-shadow: 0 -1px 5px rgba(0,0,0,0.1);
        }
        </style>
        <div class="footer">
            &copy; 2025 AL MUFRASH A. All rights reserved.
        </div>
    """, unsafe_allow_html=True)

