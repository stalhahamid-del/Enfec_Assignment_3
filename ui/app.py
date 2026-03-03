# app.py
import streamlit as st
import requests
import uuid

st.title("🧠 A2A Agent Marketplace")

# Fetch agents
try:
    agents = requests.get("http://127.0.0.1:8000/api/agents/list").json()
except:
    agents = []

if not agents:
    st.warning("No agents registered yet. Run register_agents.py and start agent servers.")
    st.stop()

agent_names = [agent["name"] for agent in agents]
selected_agent_name = st.selectbox("Select an Agent", agent_names)

task_input = st.text_area("Enter your task/input", "")

if st.button("Send Task") and task_input.strip():
    # Find agent endpoint
    selected_agent = next((a for a in agents if a["name"] == selected_agent_name), None)
    if selected_agent:
        task_data = {
            "task_id": str(uuid.uuid4()),
            "capability": selected_agent["capabilities"][0] if selected_agent["capabilities"] else "",
            "input": task_input,
            "context": {}
        }
        try:
            resp = requests.post(selected_agent["endpoint_url"], json=task_data)
            st.subheader("Output")
            if resp.ok:
                st.json(resp.json())
            else:
                st.error(f"Agent returned status {resp.status_code}")
        except Exception as e:
            st.error(f"Failed to send task: {e}")