# register_agents.py
import requests

agents = [
    {"name": "Math Helper", "description": "Solves math problems", "capabilities": ["math"], "endpoint_url": "http://127.0.0.1:8001/execute", "status": "active"},
    {"name": "Text Summarizer", "description": "Summarizes text", "capabilities": ["summarization"], "endpoint_url": "http://127.0.0.1:8002/execute", "status": "active"}
]

for agent in agents:
    resp = requests.post("http://127.0.0.1:8000/api/agents/register", json=agent)
    print(agent["name"], resp.status_code, resp.text)