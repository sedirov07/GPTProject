import streamlit as st
from model import AIModel


model = AIModel()

st.title('AI Response Generator')

user_input = st.text_input("Ask a question:")

if user_input:
    with st.spinner('Generating response...'):
        response = model.generate_response(user_input)
    st.text_area("Response:", response, height=150)
