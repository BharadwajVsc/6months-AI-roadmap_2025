import streamlit as st
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import base64


# adding image for background
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# calling the function to set the image as background
set_background(
    r"C:\Users\bhara\OneDrive\Pictures\Screenshots\Screenshot 2025-09-17 123413.png"
)


# loading the BERT tokenizer and model
@st.cache_resource
def load_bert_model():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")
    return tokenizer, model


tokenizer, model = load_bert_model()

# Pre-defining questions with their responses
qa_pairs = {
    "Hi": "Hello there! 👋",
    "How are you?": "I’m doing great, thanks for asking! How about you?",
    "What is your name?": "I’m your friendly chatbot buddy 🤖",
    "What can you do?": "I can chat, tell jokes, and maybe even make you smile 🙂",
    "Tell me something interesting.": "Did you know octopuses have three hearts? 🐙❤️❤️❤️",
    "What is AI?": "Artificial Intelligence is the ability of machines to simulate human intelligence, like learning and problem-solving.",
    "What is data science?": "Data Science is about analyzing data to find useful information and make smart decisions.",
    "What is machine learning?": "Machine Learning is teaching computers to learn from data without being explicitly programmed.",
    "What is deep learning?": "Deep Learning uses neural networks with many layers to recognize patterns in data like images, text, and speech.",
    "Tell me a joke.": "Why don’t skeletons fight each other? They don’t have the guts. 💀😂",
    "Why did the scarecrow become a motivational speaker?": "Because he was outstanding in his field. 🌾😏",
    "Can you tell me a joke about pizza?": "Sure, but it’s a little cheesy. 🧀🍕",
    "Why don’t programmers like nature?": "Too many bugs. 🐞💻",
    "Do you believe in love at first sight?": "Nah, I prefer WiFi at full bars. 📶❤️",
    "What’s your superpower?": "I can drain your phone battery just by talking. 🔋⬇️",
    "Why was the computer cold?": "Because it forgot to close its Windows. 🪟🥶",
    "Do you ever sleep?": "Nope, I run on coffee and algorithms. ☕🤖",
    "What do you call a fake noodle?": "An Impasta! 🍝😂",
    "Who is your best friend?": "Probably Google… I copy their homework all the time. 😅",
    "What’s your favorite food?": "RAM-en noodles. 🍜💻",
    "What’s your favorite music?": "Anything with a good byte. 🎶💾",
    "Can you dance?": "I could, but I don’t want to short-circuit the floor. 💃⚡",
    "Can you sing?": "Only if you enjoy 56k modem noises. 🎤📞",
    "Can you roast me?": "Sure. You have the personality of a low-battery notification. 🔋😬",
    "Do you like humans?": "Of course! Without you, I’d just be talking to the void. 😅",
}


# Function o get BERT embeddings
def get_bert_embeddings(text):
    inputs = tokenizer(
        text, return_tensors="pt", truncation=True, padding=True, max_length=128
    )
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()


# Pre-computing embeddings for predefined questions
predefined_embedding = {
    question: get_bert_embeddings(question) for question in qa_pairs
}


# Function to get the chatbot's response
def chatbot_response(user_input):
    user_embedding = get_bert_embeddings(user_input)

    # Compute cosine similarities
    similarities = {
        question: cosine_similarity(user_embedding, predefined_embedding[question])[0][
            0
        ]
        for question in qa_pairs
    }

    # Find the most similar question
    best_match = max(similarities, key=similarities.get)

    # Return the response if similarity is high enough
    if similarities[best_match] > 0.5:  # Threshold can be adjusted
        return qa_pairs[best_match]
    else:
        return "I'm not sure how to respond to that."


# Streamlit frontend
st.title("BERT Chatbot")
st.write(
    "This is a BERT-powered chatbot application with a simple user interface built using Streamlit. It allows users to type queries and receive responses based on a predefined set of questions and answers."
)

st.subheader("Ask me anything!")

# User input
user_input = st.text_input("You:", placeholder="Type your message here...")

# Display the response
if user_input:
    response = chatbot_response(user_input)
    st.write(f"**Chatbot:** {response}")

# Footer
st.markdown("---")
