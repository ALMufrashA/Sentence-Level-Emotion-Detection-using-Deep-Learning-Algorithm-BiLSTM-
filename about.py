
import streamlit as st

from utils import set_background
# Use the correct image for each page

set_background("background_about.png")

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

    st.title("About the Project")
    st.markdown("""
    ### Description
    <div style='text-align: justify; text-indent: 40px; font-size: 17px; font-family: Arial;'>
    <b>Sentence-Level Emotion Detection using Deep Learning (BiLSTM)</b> is a web-based application that predicts emotions from user-input sentences using <b>Natural Language Processing (NLP)</b> techniques and a <b>Bidirectional LSTM (BiLSTM) model</b>. The system can accurately classify emotions such as <b>Joy, Sadness, Anger, Fear, Surprise and Love</b>. Built with <b>Streamlit</b>, the app offers an interactive interface for real-time predictions, text description of the dataset, model architecture overview, and evaluation metrics. My project demonstrates the practical application of deep learning in understanding and classifying human emotions from textual data.
    </div>

    ### Key Features
    -  <b>Emotion Classification:</b> Accurately predicts emotions like Joy, Sadness, Anger, Fear, Surprise and Love from sentences.
    -  <b>Deep Learning Model:</b> Built using a BiLSTM (Bidirectional Long Short-Term Memory) network for sequential text understanding.
    -  <b>NLP Preprocessing of Text:</b> Includes tokenization, stopword removal, lemmatization, and text cleaning for high-quality input.
    -  <b>Model Evaluation:</b> Displays accuracy, F1-score, confusion matrix, and classification report for performance insights.
    -  <b>Real-time Prediction:</b> Users can input custom text and instantly see predicted emotions.

    ### BiLSTM Description
    <div style='text-align: justify; text-indent: 40px; font-size: 17px; font-family: Arial;'>
    <b>Bidirectional Long Short-Term Memory (BiLSTM)</b> is an advanced type of <b>Recurrent Neural Network (RNN)</b> that processes data in <b>both forward and backward directions</b>. Unlike regular LSTMs that learn from past <b>(left to right)</b>, BiLSTMs also learn from future context <b>(right to left)</b>. It works dual perspective helps the model better understand the meaning and structure of sentences, making it highly effective for tasks like <b>sentiment analysis, emotion detection, and language translation</b>.
    </div>

""", unsafe_allow_html=True)

    # Sticky footer CSS
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