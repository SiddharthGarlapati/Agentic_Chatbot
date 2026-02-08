from src.langgraphAI.ui.uiconfigfile import Config
import streamlit as st
import os 
from pathlib import Path

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        col1, col2 = st.columns([1, 8])

        with col1:
            ICON_DIR = Path(__file__).parent / "icons"

            st.image(ICON_DIR / "title_icon.png", width=70)

        with col2:
            st.markdown(
                """
                <h2 style="margin-bottom: 0;">LangGraph: Agentic AI</h2>
                <p style="margin-top: 0.25rem; opacity: 0.75;">
                    Choose a use case, select a model, and start chatting.
                </p>
                """,
                unsafe_allow_html=True
            )



        st.write("")


        st.markdown(
            """
            <style>
            /* Hide Streamlit footer/menu for a cleaner look */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            /* Slightly improve chat spacing */
            .stChatMessage { padding: 0.25rem 0; }
            </style>
            """,
            unsafe_allow_html=True
        )


        with st.sidebar:

            ICON_DIR = Path(__file__).parent / "icons"

            st.image(ICON_DIR / "sidebar_icon.png", width=70)

            st.markdown("### ⚙️ Controls")

            llm_options = self.config.get_llm_options()
            usercase_options = self.config.get_usecase_options()


            st.markdown("**Model Provider**")
            self.user_controls["selected_llm"] = st.selectbox("Select llm",llm_options)

            if self.user_controls["selected_llm"]:
               st.markdown("**Groq Model**")
               model_options = self.config.get_groq_model_options()
               self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
               
               st.markdown("**API Key**")
               self.user_controls["groq_api_key"] = st.text_input("API KEY", type = "password")
               st.session_state["GROQ_API_KEY"] = self.user_controls["groq_api_key"]

               if not self.user_controls["groq_api_key"]:
                   st.warning("Please Enter your groq api key to proceed")

            st.divider()

            st.markdown("**Use Case**")       

            self.user_controls["selected_usecase"] = st.selectbox("Select Use case", usercase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Tool" or self.user_controls["selected_usecase"] == "AI news":
                st.markdown("**Tavily API Key**")
                st.session_state["TAVILY_API_KEY"] = st.text_input("Tavily API KEY",type = "password")
                self.user_controls["tavily_api_key"]  = st.session_state["TAVILY_API_KEY"]
                os.environ["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"]

                if not self.user_controls["tavily_api_key"]:
                    st.warning("Please Enter the tavily api key")

            if self.user_controls["selected_usecase"] == "AI news":
                st.divider()
                st.markdown("### 🗞️ AI News Explorer")

                time_frame = st.selectbox("Select Time Frame",
                                           ["Daily","Weekly","Monthly"],
                                           index = 0)
                
                if st.button("🚀 Fetch news", use_container_width = True):
                    st.session_state.IsFetchButtonClicked = True
                    self.user_controls["IsFetchButtonClicked"] = True
                    st.session_state.timeframe = time_frame
                    self.user_controls["selected_timeframe"] = time_frame   

        return self.user_controls    









