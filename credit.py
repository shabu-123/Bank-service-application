import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import load

# Load the saved RandomForestClassifier model
model = load("C:/Users/HP/OneDrive/Desktop/chools/credit/RandomForestClassifier1.joblib")
df = pd.read_csv("C:/Users/HP/OneDrive/Desktop/chools/credit/credit_risk_cleaned.csv")
# Load the scaler used for data preprocessing
scaler = StandardScaler()

# Assuming your entire dataset is stored in a DataFrame called 'df'
# Fit the scaler with the entire dataset
scaler.fit(df[['Age', 'Annual_Income', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate', 'Num_of_Loan', 'Delay_from_due_date', 'Num_of_Delayed_Payment', 'Credit_Mix', 'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Credit_History_Age']])

# Define a function to preprocess the input data
def preprocess_input(input_data):
    input_df = pd.DataFrame([input_data], columns=['Age', 'Annual_Income', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate', 'Num_of_Loan', 'Delay_from_due_date', 'Num_of_Delayed_Payment', 'Credit_Mix', 'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Credit_History_Age'])
    preprocessed_data = scaler.transform(input_df)
    return preprocessed_data

# Define a function to make predictions using the loaded model
def predict_credit_score(input_data):
    preprocessed_data = preprocess_input(input_data)
    prediction = model.predict(preprocessed_data)
    
    return prediction

# Define the Streamlit app
def app():
    st.title('Credit Score Prediction')

    # Get user input
    Age = st.number_input('Age')
    Annual_Income = st.number_input('Annual Income')
    Num_Bank_Accounts = st.number_input('Number of Bank Accounts')
    Num_Credit_Card = st.number_input('Number of Credit Cards')
    Interest_Rate = st.number_input('Interest Rate')
    Num_of_Loan = st.number_input('Number of Loans')
    Delay_from_due_date = st.number_input('Delay from Due Date')
    Num_of_Delayed_Payment = st.number_input('Number of Delayed Payments')
    Credit_Mix = st.number_input('Credit Mix')
    Outstanding_Debt = st.number_input('Outstanding Debt')
    Credit_Utilization_Ratio = st.number_input('Credit Utilization Ratio')
    Credit_History_Age = st.number_input('Credit History Age')

    if st.button('Predict Credit Score'):
        input_data = [Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Num_of_Loan, Delay_from_due_date, Num_of_Delayed_Payment, Credit_Mix, Outstanding_Debt, Credit_Utilization_Ratio, Credit_History_Age]
        prediction = predict_credit_score(input_data)

        # Map the predicted credit score to appropriate messages
        credit_score_message = ""
        if prediction[0] == 1:
            credit_score_message = "Credit Score is Poor"
        elif prediction[0] == 2:
            credit_score_message = "Credit Score is Average"
        elif prediction[0] == 3:
            credit_score_message = "Credit Score is Good"

        st.write(credit_score_message)

if __name__ == '__main__':
    app()
