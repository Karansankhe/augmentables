**Loan Approval Prediction System**
Overview
This project includes a loan approval prediction system with three main components:

**Model Training**: Script to train a Random Forest model.
**Backend API**: Flask application to serve the model for predictions.
**Frontend Application**: Streamlit app for user interaction.

Project Structure
bash
Copy code
loan-approval-prediction/
│
├── backend/
│   ├── app.py                 # Flask application for loan prediction
│   ├── loan_approval_rf_model.pkl  # Trained Random Forest model
│   └── requirements.txt        # Dependencies for Flask API
│
├── frontend/
│   └── app.py                 # Streamlit application for user interface
│
└── model/
    ├── train_model.py         # Script to train the Random Forest model
    └── train.csv              # Dataset for training the model
    
Setup
1. **Model Training**
This script trains a Random Forest model on the provided dataset.

Training Script (model/train_model.py)
Navigate to the model directory:

bash
Copy code
cd model
Install the required dependencies:

bash
Copy code
pip install pandas scikit-learn pickle5
Run the training script:

bash
Copy code
python train_model.py
This will process the dataset train.csv, train a Random Forest model, and save it as loan_approval_rf_model.pkl.

2. **Backend API**
The Flask API provides endpoints for loan approval predictions.

Flask API (backend/app.py)
Navigate to the backend directory:

bash
Copy code
cd backend
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
requirements.txt content:

makefile
Copy code
Flask==2.2.4
numpy==1.24.3
scikit-learn==1.3.0
gunicorn==20.2.0
Start the Flask server:

bash
Copy code
gunicorn -b 0.0.0.0:8080 app:app
The API will be available at http://127.0.0.1:8080/predict.

3. Frontend Application
The Streamlit app allows users to input loan details and get predictions.

Streamlit App (frontend/app.py)
Navigate to the frontend directory:

bash
Copy code
cd frontend
Install the required dependencies:

bash
Copy code
pip install streamlit requests numpy
Start the Streamlit app:

bash
Copy code
streamlit run app.py
The app will be accessible in your web browser at the address shown in the terminal, typically http://localhost:8501.

How to Use
Train the Model: Run the training script to generate the model file.
Start the Backend API: Run the Flask server to provide prediction services.
Run the Frontend App: Use Streamlit to create a user interface for interacting with the backend API.
