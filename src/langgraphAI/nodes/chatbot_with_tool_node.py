from src.langgraphAI.state.state import State
from langchain_core.messages import SystemMessage

class ChatbotWithToolNode:
     def __init__(self,llm,tools):
          self.llm_with_tools = llm.bind_tools(tools) 

     def process(self, state: State) -> dict :

          system = SystemMessage(
               content  = ( "You are a helpful assistant. "
              "Use the Tavily search tool when you need up-to-date or factual info. "
              "If you use the tool, cite what you found in plain language."
            )
          )

          ai_msg = self.llm_with_tools.invoke([system] + list(state["messages"]))
          return {"messages": [ai_msg]}
     


