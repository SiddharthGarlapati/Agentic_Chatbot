import streamlit as st
from src.langgraphAI.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphAI.LLMS.groqllm import GroqLLM
from src.langgraphAI.graphs.graph_builder import GraphBuilder
from src.langgraphAI.ui.streamlitui.display_result import DisplayResult

def load_langgraph_agentic_app():

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input")

    user_message = st.chat_input("Enter you query")

    if user_message:
        try: 
            llm_obj_config = GroqLLM(user_controls_input= user_input)
            llm = llm_obj_config.get_llm_model()

            if not llm:
                st.error("Error: LLM could not be initialized")
                return
            
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No usecase selected")
            
            try: 
                graph_builder = GraphBuilder(model = llm)
                graph = graph_builder.setup_graph(usecase)
                display_obj = DisplayResult(usecase = usecase, graph = graph, user_message = user_message)
                display_obj.display_result_on_ui()

            except Exception as e:
                st.error(f"Error with exception {e}")
                return

            

        except Exception as e:
            st.error(f"Error with exception {e}")    




