import json
import streamlit as st

questions_and_options = [
    {
        "question": "Welcome to our car insurance service! What type of car insurance are you interested in?",
        "options": ["Comprehensive", "Third Party", "Third Party, Fire and Theft"]
    },
    {
        "question": "Great choice! What is the make of your car?",
        "options": ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "BMW", "Mercedes-Benz", "Other"]
    },
    {
        "question": "How old is your car?",
        "options": ["Less than 1 year", "1-3 years", "4-6 years", "7-10 years", "More than 10 years"]
    },
    {
        "question": "Do you use your car for commuting to work?",
        "options": ["Yes", "No"]
    },
    {
        "question": "Where do you primarily park your car overnight?",
        "options": ["Garage", "Driveway", "Street", "Parking Lot", "Other"]
    },
    {
        "question": "Thank you for providing your information. One moment please while I review your details.",
        "options": ["Continue"]
    },
    {
        "question": "Based on the information provided, you qualify for the following insurance options: Comprehensive, Third Party, and Third Party, Fire and Theft. Please select your preferred option.",
        "options": ["Comprehensive", "Third Party", "Third Party, Fire and Theft"]
    },
    {
        "question": "Thank you for choosing your preferred insurance option. What is the estimated value of your car?",
        "options": ["$0 - $10,000", "$10,001 - $20,000", "$20,001 - $30,000", "More than $30,000"]
    },
    {
        "question": "Thank you for providing your estimated car value. I will now calculate your premium. Please wait for a moment.",
        "options": ["Continue"]
    },
    {
        "question": "Your estimated premium for the selected insurance option is $XXX. Would you like to proceed with this quote?",
        "options": ["Yes", "No"]
    },
    {
        "question": "Thank you for considering our insurance quote. Let me check if you are eligible for this option based on the information provided.",
        "options": ["Continue"]
    },
    {
        "question": "Congratulations! You are eligible for the selected insurance option. A manager will review your application and contact you shortly to discuss further details.",
        "options": ["Continue"]
    },
    {
        "question": "I'm sorry, but based on the information provided, you are not eligible for the selected insurance option. Would you like to explore other options?",
        "options": ["Yes", "No"]
    },
    {
        "question": "Thank you for considering other options. A manager will review your application and contact you shortly to discuss further details.",
        "options": ["Continue"]
    }
]

with open('car_insurance_dataset.json', 'w') as json_file:
    json.dump(questions_and_options, json_file, indent=4)

with open('car_insurance_dataset.json', 'r') as file:
    dataset = json.load(file)

def display_question(question_data):
    st.write(question_data['question'])
    for i, option in enumerate(question_data['options']):
        st.write(f"{i + 1}. {option}")

def check_eligibility_for_option(option, user_responses):
    # Placeholder function for eligibility checks
    return True

def app():
    st.title("Car Insurance claim")

    user_responses = {}

    current_question_index = st.session_state.get('current_question_index', 0)

    if current_question_index >= len(dataset):
        st.write("Thank you for providing your information. Let me check if you are eligible...\n")
        eligibility_per_option = {}
        for question_data in dataset:
            option = user_responses[question_data['question']]
            eligibility_per_option[option] = check_eligibility_for_option(option, user_responses)

        for option, eligible in eligibility_per_option.items():
            if eligible:
                st.write(f"You are eligible for the {option} insurance option.")
            else:
                st.write(f"You are not eligible for the {option} insurance option.")

    else:
        question_data = dataset[current_question_index]
        display_question(question_data)
        user_input = st.text_input("Your choice (enter option number):")

        if st.button("Submit"):
            if user_input.isdigit() and 1 <= int(user_input) <= len(question_data['options']):
                user_responses[question_data['question']] = question_data['options'][int(user_input) - 1]
                current_question_index += 1
                st.session_state['current_question_index'] = current_question_index
            else:
                st.write("Invalid input. Please enter a valid option number.")

    if current_question_index >= len(dataset):
        st.session_state.pop('current_question_index', None)

if __name__ == '__main__':
    app()