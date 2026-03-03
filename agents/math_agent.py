from flask import Flask, request, jsonify

app = Flask("Math Helper")

@app.route("/execute", methods=["POST"])
def execute():
    data = request.get_json()
    try:
        result = str(eval(data.get("input", "0")))
        return jsonify({"task_id": data.get("task_id"), "status": "success", "result": result, "error": None})
    except Exception as e:
        return jsonify({"task_id": data.get("task_id"), "status": "error", "result": None, "error": str(e)})

app.run(port=8001)