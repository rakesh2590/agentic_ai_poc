from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class MessagesState(TypedDict):
    question: str
    answer: str


def ask_llm(state: MessagesState):
    llm = get_llm("openai:gpt-4")
    response = llm.invoke(state["question"])

    return {
        "answer": response.content
    }


graph = StateGraph(MessagesState)

graph.add_node("ask_llm", ask_llm)

graph.add_edge(START, "ask_llm")
graph.add_edge("ask_llm", END)

app = graph.compile()


if __name__ == "__main__":
    result = app.invoke({
        "question": "What is LangGraph in simple terms?"
    })

    print(result["answer"])