# Car_Price-prediction

1. The Goal: Predict Used Car Prices 💰
The main objective is to build a reliable machine learning model that can estimate the resale value of a car. This is useful for both buyers and sellers in the used car market.

2. The Data: Real-World Listings (quikr_car.csv) 📊
The project is fueled by a real-world dataset scraped from Quikr, a popular online classifieds platform. This dataset contains information about used cars, including:
name: The full name of the car model. 
company: The car's manufacturer (e.g., Maruti, Hyundai).
year: The year the car was manufactured.
Price: The selling price listed on the website.
kms_driven: The total distance the car has been driven.
fuel_type: The type of fuel the car uses (e.g., Petrol, Diesel).
A significant part of the project involves cleaning this raw data, as it contains inconsistencies like non-numeric values and missing entries that need to be fixed before it can be used for training.

3. The "Brain": Building the Model (car_price.ipynb) 🧠
This Jupyter Notebook is the core of the project where all the data science happens:
Data Cleaning and Exploration: The raw CSV data is loaded, analyzed, and cleaned to prepare it for modeling.
Feature Engineering: The notebook creates the features (inputs) and the target (output, which is the price) for the model.
Model Training: A Linear Regression model is trained on the cleaned data. This model learns the mathematical relationship between a car's features (like its age, company, and kilometers driven) and its selling price.

Model Saving: After training, the entire processing and modeling pipeline is saved into a single file called car_price_pipe.pkl using pickle. This captures all the steps needed to make a prediction and allows for easy reuse.

4. The User Interface: An Interactive Web App (app.py) 🖥️
This Python script creates a user-friendly web application using the Streamlit library.
Load the Brain: The app starts by loading the saved car_price_pipe.pkl model.


User Input: It provides simple input fields where a user can enter the details of their car, such as the company, model name, year, fuel type, and kilometers driven.
Instant Predictions: When the user clicks the "Predict Price" button, the app feeds their input to the loaded model, which instantly calculates and displays the estimated price of the car.
