import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If the ask button is clicked
if submit:
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    st.write(response)
