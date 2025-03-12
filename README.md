# California Housing dataset
## Data Set Characteristics:

Number of Instances:20640

Number of Attributes:8 numeric, predictive attributes and the target

## Attribute Information:
"MedInc": median income in block group

"HouseAge": median house age in block group

"AveRooms": average number of rooms per household

"AveBedrms": average number of bedrooms per household

"Population": block group population

"AveOccup": average number of household members

"Latitude": block group latitude

"Longitude": block group longitude

Missing Attribute Values: None

The target variable is the median house value for California districts, expressed in hundreds of thousands of dollars ($100,000).

It can be downloaded/loaded using the sklearn.datasets.fetch_california_housing function.

# House Price Prediction API
## Project Overview
This project involves building a machine learning model to predict house prices based on various features. The model is deployed as a REST API using Flask, allowing users to input house attributes and receive price predictions.

## Features
-Data preprocessing and feature engineering
-Model training and hyperparameter tuning
-API deployment using Flask
-User-friendly web interface for predictions

## Installation

### Prerequisites
Ensure you have Python installed along with the required libraries:

    pip install flask joblib scikit-learn pandas numpy

## Running the Application
1. Navigate to the project directory in PowerShell:
    
    cd "C:\path\to\your\project"

2. Start the Flask API:

    python app.py

3. Access the Web Interface:

    Open your browser and go to http://127.0.0.1:5000

    Input house details and get price predictions

4. Using the API via Postman or CURL:

    -Send a POST request to http://127.0.0.1:5000/predict with JSON data:

    {
     "MedInc": 3.5,
     "HouseAge": 20,
     "AveBedrms": 1.2,
     "Population": 300,
     "AveOccup": 2.5,
     "Latitude": 37.5,
    "Longitude": -122.2
    }

    -Response example:
    {"prediction": 250000}

## Model Details

Dataset: California Housing Dataset

Model: Decision Tree Regressor (Optimized with GridSearchCV)

Performance Metrics: MAE, RMSE, R²

Model saved as "best_tree_model.pkl".

## Contributors
Reezwan Parvez

Contact: reezwan1994@gmail.com

## License
This project is open-source and available for use and modification.