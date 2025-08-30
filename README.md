Recall Prediction App 🚗⚠️

📌 Project Overview

The Recall Prediction App uses machine learning to predict whether a product recall is likely to occur based on manufacturer details, recall descriptions, and other key features. This helps improve quality control, safety monitoring, and proactive decision-making.

⚙️ Features

Interactive Streamlit web app

Predicts recall classification (High Impact / Medium Impact \ Low Impact)

User-friendly inputs for Manufacturer, Component, Recall Type, Recall Description, Year, Month, etc.

Displays predictions in real-time

Easy integration with saved ML model (recall_model.pkl)

## 🛠️ Installation & Setup

### Initialize a new Git repository

git init

git remote add origin https://github.com/Gpriyanka31/Recall_prediction_app.git

git pull origin main

## Install dependencies

pip install -r requirements.txt

## ▶️ Run the App
streamlit run app.py

## The app will open in your browser at:

👉 http://localhost:8501

📂 Project Structure

Recall_prediction_app/
│── app.py                # Streamlit app  
│── model.pkl             # Trained ML model  
│── cleaned_Recall.csv    # Cleaned dataset  
│── requirements.txt      # Dependencies  
│── README.md             # Project documentation  

🚀 Future Improvements

Add more ML models and compare performance

Deploy app on Streamlit Cloud / Heroku / AWS

Enhance recall description processing with NLP (TF-IDF, BERT)

👩‍💻 Author

Priyanka Gupta

📧 contactpriyankagupta31@gmail.com

🔗[Linkedin URL](https://www.linkedin.com/in/priyanka-gupta-50988199/)

🔗[App URL](https://gpriyanka31-recall-prediction-app-app-46hj3r.streamlit.app/)


