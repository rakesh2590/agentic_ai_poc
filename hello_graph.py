from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class MessagesState(TypedDict):
    name : str
    message:str
    
    
def welcome_msg(state : MessagesState) -> MessagesState:
   return {
        "message": f"Welcome {state['name']}"
    }

graph = StateGraph(MessagesState)

graph.add_node("message", welcome_msg)
graph.add_edge(START ,"message")
graph.add_edge("message", END)

graph = graph.compile()

# response = compiled_graph.invoke({
#         "name": "Rakesh"
#     })
# print(response)