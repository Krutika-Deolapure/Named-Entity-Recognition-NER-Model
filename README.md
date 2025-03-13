# Named-Entity-Recognition-NER-Model
This project aims to build a Named Entity Recognition (NER) model using SpaCy and deploy it using a Flask API and a Streamlit-based frontend for interactive usage. The project includes data preprocessing, model training, optimization, and deployment strategies.

## Steps Taken for Data Preprocessing and Feature Engineering
1. **Data Loading**:
   - The data is loaded from text files containing tagged sentences.
   - Each file is read and split into sentences.
   
2. **Preprocessing**:
   - Text is lowercased and tokenized using SpaCy.
   - Stop words and non-alphabetic tokens are removed.
   
3. **Data Formatting**:
   - Data is converted into a format suitable for SpaCy's training.
   - Each sentence is represented with tokens and their respective entity labels.
   
## Approach for Model Selection and Optimization
1. **Model Creation**:
   - A blank SpaCy model is created and a Named Entity Recognizer (NER) pipeline is added.
   
2. **Adding Labels**:
   - Labels are added to the NER pipeline based on the training data.
   
3. **Training**:
   - The model is trained for multiple iterations to optimize the weights.
   
4. **Evaluation**:
   - The model is evaluated using classification metrics to ensure accuracy.
   
5. **Hyperparameter Tuning**:
   - Hyperparameters such as batch size and the number of iterations are tuned for optimal performance.
   
6. **Saving the Model**:
   - The trained model is saved using Joblib and Pickle for deployment.
  
## Deployment Strategy
1. **Flask API**:
- A Flask application is used to create an endpoint (`/predict`) for model predictions.
- Basic authentication is implemented to secure the API.
- The API expects a JSON payload with the text to be analyzed and returns the recognized entities.

2. **Streamlit Frontend**:
- A Streamlit app is developed to provide an interactive user interface for the NER model.
- Users can enter text and view the recognized entities in a user-friendly format.
- Basic authentication is also implemented for the Streamlit app.

## API Usage Guide
## Endpoint
- **URL**: `/predict`
- **Method**: `POST`
- **Authentication**: Basic Auth (Username: `admin`, Password: `password`)

## Request
- **Content-Type**: `application/json`
- **Body**:
  ```json
  {
    "text": "Barack Obama was the 44th President of the United States."
  }
  ```

## Response
- **Content-Type**: `application/json`
- **Body**:
  ```json
  {
    "entities": [
        {"text": "Barack Obama", "label": "PERSON"},
        {"text": "44th", "label": "ORDINAL"},
        {"text": "President", "label": "TITLE"},
        {"text": "United States", "label": "GPE"}
    ]
  }
  ```

## PowerShell Script for Testing the API
```powershell
# Encode the credentials in Base64
$username = "admin"
$password = "password"
$pair = "$($username):$($password)"
$encodedCredentials = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes($pair))

# Define the headers with the Basic Auth
$headers = @{
    "Content-Type" = "application/json"
    "Authorization" = "Basic $encodedCredentials"
}

# Define the body
$body = @{
    text = "Barack Obama was the 44th President of the United States."
} | ConvertTo-Json

# Send the POST request
$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/predict" -Method Post -Headers $headers -Body $body

# Convert the response to JSON string and output the response
$response | ConvertTo-Json -Depth 10
```

## Streamlit Frontend
## Features
- **Login**: Users must log in with the username `admin` and password `password`.
- **Text Input**: Users can enter text to analyze.
- **Entity Recognition**: The recognized entities are displayed interactively.

## How to Run the Project
## Prerequisites
- Python 3.6 or higher
- Virtual Environment (recommended)
  
## Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd ner_project
   ```
   
2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask API**:
   ```bash
   python flask_app.py
   ```

5. **Run the Streamlit App**:
   ```bash
   streamlit run streamlit_app.py
   ```

6. **Access the Applications**:
   - **Flask API**: Open your browser and go to `http://127.0.0.1:5000/predict`
   - **Streamlit App**: Open your browser and go to the URL provided by Streamlit

By following these instructions, you should be able to run the NER model using both the Flask API and the Streamlit frontend.
