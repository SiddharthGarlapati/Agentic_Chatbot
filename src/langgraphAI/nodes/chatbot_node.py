from src.langgraphAI.state.state import State


class ChatbotNode:
    def __init__(self,llm):
        self.llm = llm

    def process(self, state: State)-> dict:
            ai_msg = self.llm.invoke(state["messages"])
            return {"messages": [ai_msg]}


