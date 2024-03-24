import os
import streamlit as st
from embedchain import App

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

bot = App()
bot.add("./Harry_Potter_all_books_preprocessed.txt")

st.title("Harry Potter 🔮")
st.subheader("Ask about Harry Potter Series")

question = st.text_input("Ask Question!")

if st.button("Generate"):
    result = bot.query(question)
    st.write(result)