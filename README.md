**Loan Approval Prediction System**

This model uses a Random Forest classifier trained on features like Gender, Married status, Dependents, Education, Self-Employment, Applicant Income, Coapplicant Income, Loan Amount, Loan Term, Credit History, and Property Area.


Overview
This project includes a loan approval prediction system with three main components:

**Model Training**: Script to train a Random Forest model.


**Backend API**: Flask application to serve the model for predictions.


**Frontend Application**: Streamlit app for user interaction.



![diagram-export-9-11-2024-1_48_56-AM](https://github.com/user-attachments/assets/d14dcdd3-3be0-4f48-9b7c-7d484316e61c)



    
Setup
1. **Model Training**
This script trains a Random Forest model on the provided dataset.

Training Script (Notebook/main.ipynb)
Navigate to the model directory:


cd model
Install the required dependencies:


pip install -r requirements.txt
Run the training script:


python main.ipynb
This will process the dataset train.csv, train a Random Forest model, and save it as loan_approval_rf_model.pkl.

2. **Backend API**
The Flask API provides endpoints for loan approval predictions.

Flask API (backend/main.py)
Navigate to the backend directory:



cd backend
Install the required dependencies:


Copy code
pip install -r requirements.txt
requirements.txt content:


Flask==2.2.4
numpy==1.24.3
scikit-learn==1.3.0
gunicorn==20.2.0

Start the Flask server:
The API will be available at (http://127.0.0.1:5000/predict)

3. **Frontend Application**
The Streamlit app allows users to input loan details and get predictions.

Streamlit App (frontend/app.py)
Navigate to the frontend directory:

cd frontend
Install the required dependencies:

pip install streamlit requests numpy
Start the Streamlit app:

streamlit run main.py


How to Use
Train the Model: Run the training script to generate the model file.
Start the Backend API: Run the Flask server to provide prediction services.
Run the Frontend App: Use Streamlit to create a user interface for interacting with the backend API.
