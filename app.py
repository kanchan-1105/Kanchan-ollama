import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM   # updated import

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that answers questions based on the question asked."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("Where should we begin!")
input_text = st.text_input("What question do you have?:")

# LLM model (gemma2)
llm = OllamaLLM(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Validation based input
if input_text:
    st.write(chain.invoke({"question": input_text}))
