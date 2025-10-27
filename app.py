from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder=None)
CORS(app)  # allow localhost React during dev; OK for HW

def parse_int(v, default=0):
    try:
        return int(v)
    except:
        return default

@app.get("/api/checkin")
def check_in():
    project_id = request.args.get("projectId", "").strip()
    qty = parse_int(request.args.get("qty", "0"))
    return jsonify({"projectId": project_id, "qty": qty, "message": f"{qty} hardware checked in"})

@app.get("/api/checkout")
def check_out():
    project_id = request.args.get("projectId", "").strip()
    qty = parse_int(request.args.get("qty", "0"))
    return jsonify({"projectId": project_id, "qty": qty, "message": f"{qty} hardware checked out"})

@app.get("/api/join")
def join():
    project_id = request.args.get("projectId", "").strip()
    return jsonify({"projectId": project_id, "message": f"Joined {project_id}"})

@app.get("/api/leave")
def leave():
    project_id = request.args.get("projectId", "").strip()
    return jsonify({"projectId": project_id, "message": f"Left {project_id}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
