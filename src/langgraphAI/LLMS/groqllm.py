import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try: 
            groq_api_key = self.user_controls_input["groq_api_key"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]
            if groq_api_key == " ":
                st.error("Please enter your groq api key")
            llm = ChatGroq(groq_api_key = groq_api_key , model = selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error occured with exception as {e}")

        return llm
    
            
