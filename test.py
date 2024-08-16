#pip install streamlit
#pip install transformers
#pip install torch

import os
import streamlit as st
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

# Set up the environment key if needed (e.g., for other APIs)
os.environ["API_KEY"] = st.secrets["API_KEY"]

# Streamlit UI
st.title("Tweet Generator - V 🐦")
st.subheader("🚀 Generate tweets on any topic")

topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

# Load LLaMA model and tokenizer
model_name = "llama3-8b"  # Use the appropriate model path
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

if st.button("Generate"):
    prompt = f"Generate {number} tweets on the topic: {topic}"
    
    # Tokenize input prompt
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate text
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100 * number, num_return_sequences=number)

    # Decode and display results
    for i, output in enumerate(outputs):
        tweet = tokenizer.decode(output, skip_special_tokens=True)
        st.write(f"Tweet {i+1}:\n{tweet}")



# python test.py
