from src.langgraphAI.ui.uiconfigfile import Config
import streamlit as st
import os 

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config( page_title= "🤖 " + self.config.get_page_title(), layout = "wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:

            llm_options = self.config.get_llm_options()
            usercase_options = self.config.get_usecase_options()
            

            self.user_controls["selected_llm"] = st.selectbox("Select llm",llm_options)

            if self.user_controls["selected_llm"]:
               model_options = self.config.get_groq_model_options()
               self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)

               self.user_controls["groq_api_key"] = st.text_input("API KEY", type = "password")
               st.session_state["GROQ_API_KEY"] = self.user_controls["groq_api_key"]

               if not self.user_controls["groq_api_key"]:
                   st.warning("Please Enter your groq api key to proceed")

            self.user_controls["selected_usecase"] = st.selectbox("Select Use case", usercase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Tool" or self.user_controls["selected_usecase"] == "AI news":
                st.session_state["TAVILY_API_KEY"] = st.text_input("Tavily API KEY",type = "password")
                self.user_controls["tavily_api_key"]  = st.session_state["TAVILY_API_KEY"]
                os.environ["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"]

                if not self.user_controls["tavily_api_key"]:
                    st.warning("Please Enter the tavily api key")

            if self.user_controls["selected_usecase"] == "AI news":
                st.subheader("AI news Explorer")

                time_frame = st.selectbox("Select Time Frame",
                                           ["Daily","Weekly","Monthly"],
                                           index = 0)
                
                if st.button("Fetch the news", use_container_width = True):
                    st.session_state.IsFetchButtonClicked = True
                    self.user_controls["IsFetchButtonClicked"] = True
                    st.session_state.timeframe = time_frame
                    self.user_controls["selected_timeframe"] = time_frame   

        return self.user_controls    









