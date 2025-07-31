import streamlit as st

from utils import set_background
# Use the correct image for each page

set_background("background_home.jpeg")

def render():

    # Sticky header CSS
    st.markdown("""
        <style>
        .header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #f0f0f0;
            color: #333;
            text-align: center;
            padding: 20px;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            z-index: 1000;
        }
        .main-content {
            padding-top: 100px; /* space below header */
        }
        </style>

        <div class="header">
            Welcome to Sentence-Level-Emotion-Detection Web App
        </div>
    """, unsafe_allow_html=True)

    st.title("Dataset Overview")

    st.markdown("""
    ### Dataset Description
    <div style='text-align: justify; text-indent: 40px; font-size: 17px; font-family: Arial;'>
    The dataset used in my project consists of labeled text sentences, each tagged with one of five <b>emotion categories: joy, sadness, anger, fear, surprise and love</b>. It is designed for Sentence-Level Emotion Classification, where each sentence expresses a dominant emotion. The dataset is preprocessed by removing noise such as <b>stopwords, punctuation, and URLs, followed by lemmatization and tokenization using the Keras Tokenizer</b>. This clean and structured format enables effective training of deep learning models like BiLSTM for accurate emotion prediction.
    </div>  
    <br>
    <b>The dataset contains sentences labeled with one of six emotions.</b>

    | Emotion     | Description                      |
    |-------------|----------------------------------|
    | Joy         | Expressing happiness             |
    | Sadness     | Expressing sorrow or grief       |
    | Anger       | Expressing frustration or rage   |
    | Fear        | Expressing anxiety or concern    |
    | Surprise    | Expressing astonishment or wonder   |
    | Love        | Expressing affection             |

    Data was preprocessed with lemmatization, stopword removal, and tokenization.

""", unsafe_allow_html=True)
    

