from tavily import TavilyClient
from src.langgraphAI.state.state import State

time_range_map = {"daily": "d", "weekly": "w", "monthly": "m", "year": "y"}
days_map = {"daily": 1, "weekly": 7, "monthly": 30, "year": 366}

def fetch_news(state: State):
    frequency = state["time_frame"].lower().strip()
    if frequency not in time_range_map:
        frequency = "weekly"   # default
    tavily = TavilyClient()
    response = tavily.search(
        query = "Latest Artificial Intelligence (AI) Technology news globally",
        topic = "news",
        time_range = time_range_map[frequency],
        include_answer= True,
        days = days_map[frequency],
        max_results= 6,
    )

    return response
