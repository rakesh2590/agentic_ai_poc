from langgraph_sdk import get_sync_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("LANGGRAPH_URL")
client = get_sync_client(url=url)

def call_graph(graph_name: str, input_data: dict):
    result = client.runs.wait(
        None,
        graph_name,
        input=input_data
    )
    return result

# Call different graphs
result1 = call_graph("hello",   {"name": "Susmitha"})
result2 = call_graph("goodbye", {"name": "Rakesh"})
result3 = call_graph("summary", {"text": "Some text here"})

print(result1)
print(result2)
print(result3)