# home.py
import streamlit as st
from utils import set_background

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

    set_background("C:/Users/HP/OneDrive/Desktop/Sentence Emotion/background_home.jpeg")  # ✅ Now inside render

    st.title("Welcome to Sentence-Level-Emotion-Detection Web App")
    st.markdown("""
    <div style='font-size:30px; color:white; font-family:Arial;'>
        My application uses <b style='color:red;'>Deep learning (BiLSTM)</b> to predict the Emotion in a Sentence.
        <br><br>
        <b>Navigate using the sidebar to explore:</b>
        <ul style='font-size:22px;'>
            <li>
                <span style='color:red;'><b>Model details</b></span>
                <p style='color:#D5D8DC; font-size:18px;'>Learn how our <b>Emotion Detection Model</b> works, including the architecture <b>(BiLSTM)</b>, <b>Training Method</b>, and the <b>Tools</b> used to build it.</p>
            </li>
            <li>
                <span style='color:red;'><b>Dataset Insights</b></span>
                <p style='color:#D5D8DC; font-size:18px;'>Explore the dataset with the <b>Emotion Labels, Text Descriptions</b>, and <b>Preprocessing Details</b>.</p>
            </li>
            <li>
                <span style='color:red;'><b>Real-Time Emotion Predictions</b></span>
                <p style='color:#D5D8DC; font-size:18px;'>Try your <b>Own Sentences</b> and see the <b>Predicted Emotion</b> instantly.</p>
            </li>
            <li>
                <span style='color:red;'><b>Evaluation Results</b></span>
                <p style='color:#D5D8DC; font-size:18px;'>Check performance metrics like <b>Accuracy, Confusion Matrix</b>, and more.</p>
            </li>
            <li>
                <span style='color:red;'><b>And More!</b></span>
                <p style='color:#D5D8DC; font-size:18px;'>Discover extra tools, visualizations, and future improvements.</p>
            </li>
        </ul>
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

