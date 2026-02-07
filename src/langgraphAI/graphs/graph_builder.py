from langgraph.graph import StateGraph,START,END
from src.langgraphAI.state.state import State
from src.langgraphAI.nodes.chatbot_node import ChatbotNode
from src.langgraphAI.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphAI.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import tools_condition
from src.langgraphAI.nodes.chatbot_ainews_node import ChatbotAinewsNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        
        self.chatbot_node = ChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def chatbot_with_tools_build_graph(self):
        tools = get_tools()
        tool_node = create_tool_node(tools)
        self.chatbot_with_tool_call_node = ChatbotWithToolNode(self.llm,tools)
        self.graph_builder.add_node("chatbot", self.chatbot_with_tool_call_node.process)
        self.graph_builder.add_node("tools",tool_node)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition,
                                                 {"tools": "tools",
                                                  END: END}, 
                                                  )
        self.graph_builder.add_edge("tools","chatbot") 


    def chatbot_ai_news_build_graph(self):

        self.chatbot_ai_news_node = ChatbotAinewsNode(self.llm)
        self.graph_builder.add_node("fetch_news",self.chatbot_ai_news_node.process)
        self.graph_builder.add_node("summarize",self.chatbot_ai_news_node.summarize)
        self.graph_builder.add_edge(START,"fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize")
        self.graph_builder.add_edge("summarize",END)

        

    def setup_graph(self, usecase: str ):

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()  

        elif usecase == "Chatbot with Tool":
            self.chatbot_with_tools_build_graph()  

        elif usecase == "AI news":
            self.chatbot_ai_news_build_graph()     

        return self.graph_builder.compile()   





