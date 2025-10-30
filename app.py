from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder=None)
CORS(app)  # allow requests from your React dev server or elsewhere

# ----- Root page with links -----
@app.get("/")
def home():
    base = request.url_root.rstrip("/")
    return f"""
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>EE461L HW5 Backend</title>
    <style>
      body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; margin: 2rem; }}
      code {{ background:#f3f4f6; padding:2px 6px; border-radius:6px; }}
      ul {{ line-height: 1.8; }}
    </style>
  </head>
  <body>
    <h1>EE461L HW5 Backend</h1>
    <p>Quick test links (sample <code>projectId</code>=2, <code>qty</code>=5):</p>
    <ul>
      <li><a href="{base}/api/health">{base}/api/health</a></li>
      <li><a href="{base}/api/join?projectId=2">{base}/api/join?projectId=2</a></li>
      <li><a href="{base}/api/leave?projectId=2">{base}/api/leave?projectId=2</a></li>
      <li><a href="{base}/api/checkin?projectId=2&qty=5">{base}/api/checkin?projectId=2&qty=5</a></li>
      <li><a href="{base}/api/checkout?projectId=2&qty=5">{base}/api/checkout?projectId=2&qty=5</a></li>
    </ul>
    <h3>Usage</h3>
    <ul>
      <li><code>/api/join?projectId=&lt;id&gt;</code></li>
      <li><code>/api/leave?projectId=&lt;id&gt;</code></li>
      <li><code>/api/checkin?projectId=&lt;id&gt;&amp;qty=&lt;n&gt;</code></li>
      <li><code>/api/checkout?projectId=&lt;id&gt;&amp;qty=&lt;n&gt;</code></li>
    </ul>
  </body>
</html>
"""

# ----- Health -----
@app.get("/api/health")
def health():
    return jsonify({"ok": True})

# ----- Helpers -----
def parse_int(v, default=0):
    try:
        return int(v)
    except:
        return default

# ----- Endpoints -----
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
