from typing_extensions import TypedDict,Annotated
from typing import List,Optional
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[List,add_messages]
    time_frame: Optional[str]

