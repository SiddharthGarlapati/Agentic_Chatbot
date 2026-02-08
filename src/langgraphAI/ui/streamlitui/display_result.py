import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json

class DisplayResult:
    def __init__(self,usecase, graph, user_message,time_frame= None ):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        self.time_frame = time_frame


    def display_result_on_ui(self):

        st.markdown(
            f"<div style='opacity:0.8; margin-bottom:0.75rem;'>Use case: <b>{self.usecase}</b></div>",
            unsafe_allow_html=True
        )

        st.write("")


        if self.usecase == "Basic Chatbot":

            for event in self.graph.stream({"messages": [HumanMessage(content=self.user_message)]}):
                print(event.values())
                for value in event.values():
                    print(value["messages"])
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"][-1].content)    


        elif self.usecase == "Chatbot with Tool":

            with st.spinner("Starting Chat........"):
                try:
                    response = self.graph.invoke({"messages": [self.user_message]})
                    for message in response["messages"]:
                        if type(message) == HumanMessage:
                            with st.chat_message("user"):
                                st.write(message.content)
                        elif type(message) == ToolMessage:
                                with st.expander("🔧 Tool call details", expanded=False):
                                    st.code(message.content)
                                st.write("Tool call end")
                        elif type(message) == AIMessage:
                            with st.chat_message("assistant"):
                                st.markdown(message.content)
                except Exception as e:
                    st.error(f"Error with exception {e} ")                

        elif self.usecase == "AI news":

            with st.spinner("Fetching and summarazing news......"):
                try:
                    response = self.graph.invoke({"messages": ["fetch news"], "time_frame": self.time_frame})

                    with st.chat_message("assistant"):
                        st.write("")
                        st.markdown(f"## {self.time_frame} AI news updates")
                        st.markdown(response["messages"][-1].content)  
                        st.caption("Tip: Switch time frame in the sidebar to fetch a different summary.")

                    st.session_state.IsFetchButtonClicked = False              
                except Exception as e:
                    st.error(f"Error with exception {e}")                                             

