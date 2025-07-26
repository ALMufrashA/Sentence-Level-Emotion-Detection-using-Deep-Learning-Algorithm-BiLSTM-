import streamlit as st

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
    
    st.title("Model Description")

    st.markdown("""
    The model used is a **Bidirectional LSTM (BiLSTM)**.

    ### Why BiLSTM?
    <div style='text-align: justify; text-indent: 40px; font-size: 17px; font-family: Arial;'>
    <b>BiLSTM (Bidirectional Long Short-Term Memory)</b> is used in my project because it effectively captures the context of a sentence from <b>both directions—past and future</b>—allowing the model to better understand the full meaning and emotional tone of a sentence. Unlike traditional <b>LSTMs that read sequences in only one direction, BiLSTM processes input in both forward and backward directions</b>, making it especially useful for emotion detection where word order and context play a crucial role in interpreting sentiment.
    </div>
                
    ### Architecture
    - <b>Embedding Layer :</b> The Embedding layer converts words into dense vector representations of the text.
    - <b>BiLSTM Layer :</b>  The BiLSTM layer captures contextual meaning from both past and future word sequences.
    - <b>Dense output layer with Softmax :</b> It generates probabilities for each emotion class to classify the sentence accurately.

    ### Work Flow
                
    <div style='text-align: justify; text-indent: 40px; font-size: 17px; font-family: Arial;'>
    <b>Sentence-Level Emotion Detection</b> project starts by <b>loading and preprocessing</b> a labeled dataset of emotional sentences. Text is <b>cleaned, lemmatized, tokenized, and converted into padded sequences</b>. A BiLSTM-based deep learning model is then trained to <b>classify emotions like joy, sadness, anger, fear, surprise and love</b>. The model is deployed using Streamlit to <b>allow users to predict emotions in real time through a simple web interface.</b>
    </div>      

    ### Output
    <div style='text-align: justify; text-indent: 40px; font-size: 17px; font-family: Arial;'>
    <b>The model outputs the predicted emotion label for a given sentence entered by the user</b>. After processing the input through the text preprocessing pipeline and passing it through the trained BiLSTM model, the system returns one of the six emotion classes—Joy, Sadness, Anger, Fear, surprise and Love—along with its probability score, indicating the model's confidence in the prediction.
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