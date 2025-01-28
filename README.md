# House Price Prediction Model

This project implements a machine learning model to predict house prices based on various features such as area, number of bedrooms, bathrooms, and other property-related characteristics. The model uses a Random Forest Regressor and is deployed with a user interface built using Streamlit.

## Project Overview

The goal of this project is to predict the price of a house based on user-input features. The model is trained using historical data and can be used by potential buyers or real estate professionals to estimate house prices.

### Features of the Model:
- Predicts house prices based on features like area, number of bedrooms, bathrooms, and more.
- Provides an intuitive user interface built with Streamlit for easy input and real-time price predictions.

### Technologies Used:
- **Machine Learning**: Random Forest Regressor
- **Web Framework**: Streamlit
- **Libraries**:
  - Pandas
  - NumPy
  - Scikit-Learn
  - SHAP (for model interpretability)
  - Joblib (for saving/loading models)
  - Streamlit (for building the UI)

## Project Setup

### Prerequisites

Make sure you have Python 3.6+ installed on your machine. You can create a virtual environment for this project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### Installation

Clone this repository:

```bash
git clone https://github.com/maqeel019/HousePricePredictionModel.git
cd HousePricePredictionModel
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

**Run the Streamlit UI**:
   To launch the user interface where you can input data and get price predictions, run:

   ```bash
   streamlit run app.py
   ```

   This will open a web browser where you can enter house details like area, number of bedrooms, and more to predict the price.

### Example Input:
In the Streamlit UI, you can enter inputs such as:
- Area of the house
- Number of bedrooms
- Number of bathrooms
- Parking spaces
- And other features like whether the house has a basement, air conditioning, etc.

The model will return a predicted price for the house.

## Model Evaluation

The model is evaluated using metrics such as:
- **RMSE (Root Mean Squared Error)**
- **R² (Coefficient of Determination)**

The model's performance has been tested on a test dataset to ensure its prediction accuracy.

## SHAP for Model Interpretation

The project includes SHAP (Shapley Additive Explanations) for model interpretability. SHAP values are calculated to understand the impact of each feature on the predicted price.

### SHAP Summary Plot

SHAP summary plots show the importance of each feature in predicting the target variable (house price). This helps identify which features have the greatest influence on the model’s predictions.

## Contributing

Feel free to fork the repository, submit issues, or contribute improvements. Contributions are always welcome!

