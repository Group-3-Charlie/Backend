# Aictron is a web app that allows its users to get predictive data analysis by inserting any csv dataset. The app will use artificial intelligence, and more precisely machine learning with SKlearn Python library. The main advantage is a lightweight application, as machine-learning algorithms are resource-efficient, making it particularly useful for anyone needing to make predictions based on specific data. The app is designed to be user-friendly, with a simple and intuitive interface. The user will be able to upload a dataset, select the target column and then get the prediction.

# This file is the main file of the app. It contains the routes and the main logic of the app. The app is built with Flask, a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

import json
import html
import os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return ("<h1>Welcome to Aictron!</h1>"
            "This is the main page of the API. "
            "<br>"
            "Please use the <a href='/get_routes'>/get_routes</a> route to get a list of all available routes."
            "<br>"
            "For more information about Aictron, please visit the <a href='/about'>/about</a> route.")


@app.route('/about')
def about():
    return ("<h1>About Aictron</h1>"
            "Aictron is a web app that allows its users to get predictive data analysis by inserting any csv dataset. "
            "The app will use artificial intelligence, and more precisely machine learning with SKlearn Python library. "
            "The main advantage is a lightweight application, as machine-learning algorithms are resource-efficient, making it particularly useful for anyone needing to make predictions based on specific data. "
            "The app is designed to be user-friendly, with a simple and intuitive interface. "
            "The user will be able to upload a dataset, select the target column and then get the prediction.")

@app.route('/upload', methods=['POST'])
def upload_dataset():
    # Handle file upload and save the dataset
    # Perform data processing if necessary
    return jsonify({'message': 'Dataset uploaded successfully'})

@app.route('/select-target', methods=['POST'])
def select_target():
    # Parse request to get the target column
    # Store the target column information
    return jsonify({'message': 'Target column selected successfully'})

@app.route('/predict', methods=['POST'])
def predict():
    # Parse request to get data for prediction
    # Call predict function from your ML module
    # Format and return prediction results
    return jsonify({'prediction': 'Prediction results'})

@app.route('/get_routes', methods=['GET'])
def get_routes():
    res = {
        "routes": [
            {
                "id": 1,
                "name": "Get Routes",
                "description": "This route returns a list of all available routes",
                "method": "GET",
                "path": "/get_routes",
                "args": "None",
                "response": "HTML",
                "status_code": "200"
            },
            {
                "id": 2,
                "name": "Upload Dataset",
                "description": "This route handles file upload and saves the dataset",
                "method": "POST",
                "path": "/upload",
                "args": "Dataset file -> CSV file",
                "response": "JSON",
                "status_code": "200 or 400"
            },
            {
                "id": 3,
                "name": "Select Target Column",
                "description": "This route handles the selection of the target column",
                "method": "POST",
                "path": "/select-target",
                "args": "Column name -> String",
                "response": "JSON",
                "status_code": "200 or 400"
            },
            {
                "id": 4,
                "name": "Predict",
                "description": "This route handles the prediction of results",
                "method": "POST",
                "path": "/predict",
                "args": "Data for prediction -> CSV file",
                "response": "JSON",
                "status_code": "200 or 400"
            },
            {
                "id": 5,
                "name": "About",
                "description": "This route returns information about Aictron",
                "method": "GET",
                "path": "/about",
                "args": "None",
                "response": "HTML",
                "status_code": "200"
            }
        ]
    }

    html_str = "<html><body><h1>Routes</h1><ul>"
    for route in res["routes"]:
        html_str += (f"<li><strong>{route['name']}</strong>: "
                        f"{route['description']}<br>"
                        f"&emsp; Method: {route['method']}<br>"
                        f"&emsp; Path: <strong>{route['path']}</strong><br>"
                        f"&emsp; Args: {route['args']}<br>"
                        f"&emsp; Response: {route['response']}<br>"
                        f"&emsp; Status Code: {route['status_code']}</li>")
    html_str += "</ul></body></html>"

    return html_str

if __name__ == '__main__':
    app.run(host="localhost", port=4567, debug=True)
