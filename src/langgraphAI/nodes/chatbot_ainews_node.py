from src.langgraphAI.state.state import State
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from src.langgraphAI.tools.ai_news_tool import fetch_news
import json


class ChatbotAinewsNode:

    def __init__(self,llm):
        self.llm = llm


    def process(self,state: State) -> dict:
       response = fetch_news(state)  
       return {"messages": [AIMessage(content = json.dumps(response))]}                             



    def summarize(self, state: State) -> dict:
        system = SystemMessage(content=(
        "You are a news summarizer.\n"
        "Return Markdown ONLY.\n"
        "Group items by date (YYYY-MM-DD) newest to oldest.\n"
        "Under each date, list 2-3 bullets.\n"
        "Each bullet must be: **Title** — 1-line summary — (Source) — URL.\n"
        "If date is missing, put under 'Unknown date'.\n"
        "Do not add facts not present in the results."
        ))
        news_blob = state["messages"][-1].content
        response = self.llm.invoke([system] + [HumanMessage(content = news_blob)])
        return {"messages": [response]}

