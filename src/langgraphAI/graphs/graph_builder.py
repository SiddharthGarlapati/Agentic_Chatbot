from langgraph.graph import StateGraph,START,END
from src.langgraphAI.state.state import State
from src.langgraphAI.nodes.chatbot_node import ChatbotNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        
        self.chatbot_node = ChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot", END)
        return self.graph_builder.compile()


    def setup_graph(self, usecase: str ):

        if usecase == "Basic Chatbot":
            return self.basic_chatbot_build_graph()    





