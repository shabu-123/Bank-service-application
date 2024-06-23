import streamlit as st
import pandas as pd
from joblib import load

# Load the trained model
loaded_gb_clf = load('C:/Users/HP/OneDrive/Desktop/chools/fraud/gbclassifier.joblib')

# Function to make predictions
def predict(input_data):
    prediction = loaded_gb_clf.predict(input_data)
    return prediction

# Streamlit app
def app():
    st.title("Fraud Detection App")

    # Get input data from the user
    account_no = st.number_input("Account Number", value=0)
    amount = st.number_input("Amount", value=0.0)
    before_transaction = st.number_input("Balance Before Transaction", value=0.0)
    after_transaction = st.number_input("Balance After Transaction", value=0.0)
    card_type = st.selectbox("Card Type", options=[1, 2, 3])
    gender = st.selectbox("Gender", options=["F", "M"])

    # Subheadings for expense types and card types
    st.subheader("Expense Types")
    bills = st.number_input("Bills", value=0)
    entertainment = st.number_input("Entertainment", value=0)
    food = st.number_input("Food", value=0)
    fuel = st.number_input("Fuel", value=0)
    grocery = st.number_input("Grocery", value=0)
    health_fitness = st.number_input("Health_Fitness", value=0)
    home = st.number_input("Home", value=0)
    personal_care = st.number_input("Personal_Care", value=0)
    travel = st.number_input("Travel", value=0)

    st.subheader("Types of Transactions")
    cash_in = st.number_input("CASH_IN", value=0)
    cash_out = st.number_input("CASH_OUT", value=0)
    debit = st.number_input("DEBIT", value=0)
    payment = st.number_input("PAYMENT", value=0)
    transfer = st.number_input("TRANSFER", value=0)

    # Date input
    st.subheader("Transaction Date")
    day = st.number_input("Day", value=0)
    month = st.number_input("Month", value=0)
    year = st.number_input("Year", value=0)

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        "Account_no": [account_no],
        "amount": [amount],
        "before_transaction": [before_transaction],
        "after_transaction": [after_transaction],
        "Card Type": [card_type],
        "F": [1 if gender == "F" else 0],
        "M": [1 if gender == "M" else 0],
        "Bills": [bills],
        "Entertainment": [entertainment],
        "Food": [food],
        "Fuel": [fuel],
        "Grocery": [grocery],
        "Health_Fitness": [health_fitness],
        "Home": [home],
        "Personal_Care": [personal_care],
        "Travel": [travel],
        "CASH_IN": [cash_in],
        "CASH_OUT": [cash_out],
        "DEBIT": [debit],
        "PAYMENT": [payment],
        "TRANSFER": [transfer],
        "Day": [day],
        "Month": [month],
        "Year": [year]
    })

    # Make predictions
    if st.button("Predict"):
        prediction = predict(input_data)
        if prediction[0] == 1:
            st.error("The transaction is likely to be fraudulent.")
        else:
            st.success("The transaction is not likely to be fraudulent.")

if __name__ == '__main__':
    app()
