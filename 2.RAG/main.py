<<<<<<< HEAD
import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


loader = PyPDFLoader("./Harry_Potter_all_books_preprocessed.txt")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 300, chunk_overlap = 50)
all_splits = text_splitter.split_documents(data)

vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectorstore.as_retriever()
)

st.title("Harry Potter 🔮")
st.subheader("Ask about Harry Potter Series")

question = st.text_input("Ask Question!")

if st.button("Generate"):
    result = qa_chain({"query": question})
    st.write(result['result'])
=======
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
>>>>>>> 9be837fafbbf090c9226c42587429787851f2887
