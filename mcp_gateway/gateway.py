import uuid
from agents import math_agent, summarizer_agent

def mcp_to_a2a(mcp_request):
    return {
        "a2a_version": "1.0",
        "sender": "mcp_gateway",
        "receiver": mcp_request["agent"],
        "task_id": str(uuid.uuid4()),
        "skill": mcp_request["skill"],
        "payload": {
            "input": mcp_request["input"]
        }
    }

def route_to_agent(a2a_message):
    if a2a_message["skill"] == "math":
        return math_agent.handle_task(a2a_message)

    elif a2a_message["skill"] == "summarize":
        return summarizer_agent.handle_task(a2a_message)