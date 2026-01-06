from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("height_weight_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')  # Serves the input form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        height = float(request.form['height'])  # Get height input
        weight_pred = model.predict(np.array([[height]]))[0]  # Predict weight
        return render_template('results.html', height=height, weight=round(weight_pred, 2))
    except:
        return "Invalid Input. Please enter a numeric height."

if __name__ == '__main__':
    app.run(debug=True)
