#pip install streamlit
#pip install langchain-google-genai
import os
import streamlit as st

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

st.title("Tweet Generator - V 🐦")

st.subheader("🚀 Generate tweets on any topic")

topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)


# Import ChatOpenAI module
#from langchain_openai import ChatOpenAI
# Initialize OpenAI's GPT 3.5 model
#gpt3_model = ChatOpenAI(model_name = "gpt-3.5-turbo-0125")

# Using Google Models (Gemini Pro)
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

if st.button("Generate"):
    prompt = f"Give me {number} tweets on {topic}."
    response = gemini_model.invoke(prompt)
    st.write(response.content)


# python test.py
