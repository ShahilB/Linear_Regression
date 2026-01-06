# Linear Regression:  Height-Weight Prediction Model 📊

A machine learning project that uses Linear Regression to predict weight based on height, complete with a Flask web application for easy interaction.

## 🎯 Project Overview

This project demonstrates the implementation of a Linear Regression model that predicts a person's weight given their height. The model is trained on a dataset containing height-weight measurements and achieves an R² score of approximately 0.858, indicating a strong correlation between height and weight.

## 🚀 Features

- **Machine Learning Model**: Linear Regression implementation using scikit-learn
- **Web Application**: Flask-based interface for real-time predictions
- **Model Persistence**: Saved model using pickle for quick deployment
- **Interactive Interface**: User-friendly HTML forms for input and results display

## 📁 Project Structure

```
Linear_Regression/
├── LR_model.ipynb              # Jupyter notebook with model training
├── app.py                      # Flask web application
├── height_weight_model.pkl     # Trained model (pickled)
├── weight-height.csv           # Training dataset
├── template/                   # HTML templates for web app
│   ├── index.html             # Input form
│   └── results. html           # Prediction results
└── README.md                   # Project documentation
```

## 🛠️ Technologies Used

- **Python 3.13**
- **Libraries**:
  - pandas - Data manipulation and analysis
  - numpy - Numerical computing
  - scikit-learn - Machine learning (LinearRegression, train_test_split, metrics)
  - Flask - Web framework
  - pickle - Model serialization

## 📊 Model Performance

- **R² Score**: 0.858 (85.8% variance explained)
- **RMSE**: ~12.21
- **Train-Test Split**: 80-20

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ShahilB/Linear_Regression.git
   cd Linear_Regression
   ```

2. **Install required dependencies**:
   ```bash
   pip install pandas numpy scikit-learn flask
   ```

## 💻 Usage

### Running the Jupyter Notebook

Open `LR_model.ipynb` to see the model training process: 
```bash
jupyter notebook LR_model. ipynb
```

### Running the Flask Web App

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to: 
   ```
   http://127.0.0.1:5000/
   ```

3. Enter a height value and get the predicted weight! 

## 📈 Model Training Process

1. **Data Loading**: Load height-weight dataset from CSV
2. **Feature Selection**: Use Height as independent variable (X) and Weight as target (y)
3. **Train-Test Split**: 80% training, 20% testing
4. **Model Training**:  Fit Linear Regression model on training data
5. **Evaluation**: Calculate RMSE and R² score
6. **Model Serialization**: Save model using pickle for deployment

## 🌐 API Endpoints

- `GET /` - Home page with input form
- `POST /predict` - Accepts height value and returns predicted weight

## 📝 Example

**Input**:  Height = 70 inches  
**Output**:  Predicted Weight ≈ 180. 5 lbs

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  Feel free to check the issues page. 

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**ShahilB**
- GitHub: [@ShahilB](https://github.com/ShahilB)

## ⭐ Show your support

Give a ⭐️ if this project helped you learn about Linear Regression!

---

*Built with ❤️ using Python and scikit-learn*
