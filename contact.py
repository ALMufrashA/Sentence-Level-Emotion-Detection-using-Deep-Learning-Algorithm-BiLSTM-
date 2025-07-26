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
    
    st.title("Contact Us")

    # Contact Info Section
    st.markdown("""
        Have any questions / query or feedback?, Please Contact Us!. We would love to hear from you
        - 🧑‍💻 **Developer**: AL MUFRASH A  
        - 📧 **Email**: [mufrashajmal2001@gmail.com](mailto:mufrashajmal2001@gmail.com)  
        - 📞 **Phone**: +91 93444 25922  
        - 🏠 **Address**: Nagercoil, Tamil Nadu, India  
        - 🌐 **GitHub**: [AL Mufrash A](https://github.com/)  
        - 💼 **LinkedIn**: [AL Mufrash A](https://www.linkedin.com/in/al-mufrash-a-a08846267?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
    """)

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
