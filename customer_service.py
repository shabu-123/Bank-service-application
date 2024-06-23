import streamlit as st
import random
import json
import pickle
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer
from keras.models import load_model

# Load NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Load the trained model and other required data
lemmatizer = WordNetLemmatizer()
intents_path = r"C:/Users/HP/OneDrive/Desktop/chools/customer_service/intents.json"
with open(intents_path, encoding="utf-8") as file:
    intents = json.load(file)

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


# Define text preprocessing functions
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Define functions for predicting intents and getting responses
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

# Define function to run Streamlit app
def app():
    # Streamlit UI
    st.title('customer service Chatbot')

    # Initialize chat history
    chat_history = []

    user_input = st.text_input("You: ", "")

    if st.button('Send'):
        if user_input.strip() != "":
            # Append user input to chat history
            chat_history.append(("You", user_input))

            # Predict response and append to chat history
            ints = predict_class(user_input)
            res = get_response(ints, intents)
            chat_history.append(("Bot", res))

            # Display chat history
            for sender, message in chat_history:
                st.write(f"{sender}: {message}")

# Run Streamlit app
if __name__ == '__main__':
    app()

            