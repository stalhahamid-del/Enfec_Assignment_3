from flask import Flask, request, jsonify

app = Flask("Text Summarizer")

@app.route("/execute", methods=["POST"])
def execute():
    data = request.get_json()
    text = data.get("input", "")
    summary = " ".join(text.split()[:10]) + "..." if len(text.split()) > 10 else text
    return jsonify({"task_id": data.get("task_id"), "status": "success", "result": summary, "error": None})

app.run(port=8002)