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
    <title>EE461L HW5 – Projects</title>
    <style>
      body {{
        font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
        margin: 0;
        background:#f3f4f6;
      }}
      .page {{
        min-height: 100vh;
        display:flex;
        align-items:center;
        justify-content:center;
        padding:32px 16px;
      }}
      .card {{
        background:white;
        border-radius:10px;
        box-shadow:0 8px 18px rgba(0,0,0,.08);
        padding:20px 24px;
        width:900px;
      }}
      h1 {{
        margin-top:0;
        margin-bottom:16px;
      }}
      .project {{
        border:1px solid #d1d5db;
        border-radius:8px;
        margin-bottom:10px;
        padding:10px 12px;
        background:#f9fafb;
      }}
      .project.active {{
        background:#ecfdf5;
      }}
      .row {{
        display:flex;
        justify-content:space-between;
        align-items:center;
        gap:12px;
        flex-wrap:wrap;
      }}
      .hw-row {{
        display:flex;
        gap:12px;
        align-items:center;
        margin-top:6px;
      }}
      .hw-label {{
        min-width:80px;
      }}
      input[type="number"], input[type="text"] {{
        width:70px;
        padding:4px 6px;
      }}
      button {{
        padding:6px 10px;
        border-radius:6px;
        border:1px solid #9ca3af;
        background:#e5e7eb;
        cursor:pointer;
      }}
      button.primary {{
        background:#2563eb;
        color:white;
        border-color:#2563eb;
      }}
    </style>
  </head>
  <body>
    <div class="page">
      <div class="card">
        <h1>Projects</h1>
        <p>Use the buttons below to join/leave projects and check hardware in and out. Messages from the server will appear as pop-ups.</p>

        <!-- Project 1 -->
        <div class="project" id="proj1">
          <div class="row">
            <strong>Project 1</strong>
            <div>
              <button onclick="joinProject(1)" class="primary">Join</button>
              <button onclick="leaveProject(1)">Leave</button>
            </div>
          </div>
          <div class="hw-row">
            <span class="hw-label">HWSet1:</span>
            <span>50 / 100</span>
            <input id="p1_hw1_qty" type="number" min="0" placeholder="qty" />
            <button onclick="checkin(1, 'p1_hw1_qty')">Check In</button>
            <button onclick="checkout(1, 'p1_hw1_qty')">Check Out</button>
          </div>
          <div class="hw-row">
            <span class="hw-label">HWSet2:</span>
            <span>0 / 100</span>
            <input id="p1_hw2_qty" type="number" min="0" placeholder="qty" />
            <button onclick="checkin(1, 'p1_hw2_qty')">Check In</button>
            <button onclick="checkout(1, 'p1_hw2_qty')">Check Out</button>
          </div>
        </div>

        <!-- Project 2 -->
        <div class="project active" id="proj2">
          <div class="row">
            <strong>Project 2</strong>
            <div>
              <button onclick="joinProject(2)" class="primary">Join</button>
              <button onclick="leaveProject(2)">Leave</button>
            </div>
          </div>
          <div class="hw-row">
            <span class="hw-label">HWSet1:</span>
            <span>50 / 100</span>
            <input id="p2_hw1_qty" type="number" min="0" placeholder="qty" />
            <button onclick="checkin(2, 'p2_hw1_qty')">Check In</button>
            <button onclick="checkout(2, 'p2_hw1_qty')">Check Out</button>
          </div>
          <div class="hw-row">
            <span class="hw-label">HWSet2:</span>
            <span>0 / 100</span>
            <input id="p2_hw2_qty" type="number" min="0" placeholder="qty" />
            <button onclick="checkin(2, 'p2_hw2_qty')">Check In</button>
            <button onclick="checkout(2, 'p2_hw2_qty')">Check Out</button>
          </div>
        </div>

        <!-- Project 3 -->
        <div class="project" id="proj3">
          <div class="row">
            <strong>Project 3</strong>
            <div>
              <button onclick="joinProject(3)" class="primary">Join</button>
              <button onclick="leaveProject(3)">Leave</button>
            </div>
          </div>
          <div class="hw-row">
            <span class="hw-label">HWSet1:</span>
            <span>0 / 100</span>
            <input id="p3_hw1_qty" type="number" min="0" placeholder="qty" />
            <button onclick="checkin(3, 'p3_hw1_qty')">Check In</button>
            <button onclick="checkout(3, 'p3_hw1_qty')">Check Out</button>
          </div>
          <div class="hw-row">
            <span class="hw-label">HWSet2:</span>
            <span>0 / 100</span>
            <input id="p3_hw2_qty" type="number" min="0" placeholder="qty" />
            <button onclick="checkin(3, 'p3_hw2_qty')">Check In</button>
            <button onclick="checkout(3, 'p3_hw2_qty')">Check Out</button>
          </div>
        </div>
      </div>
    </div>

    <script>
      const base = "{base}";

      function showMessage(resp) {{
        alert(resp.message + " (projectId=" + resp.projectId + ", qty=" + (resp.qty ?? "n/a") + ")");
      }}

      async function joinProject(id) {{
        const r = await fetch(base + "/api/join?projectId=" + id);
        const data = await r.json();
        showMessage(data);
      }}

      async function leaveProject(id) {{
        const r = await fetch(base + "/api/leave?projectId=" + id);
        const data = await r.json();
        showMessage(data);
      }}

      async function checkin(id, inputId) {{
        const qty = document.getElementById(inputId).value || 0;
        const r = await fetch(base + "/api/checkin?projectId=" + id + "&qty=" + qty);
        const data = await r.json();
        showMessage(data);
      }}

      async function checkout(id, inputId) {{
        const qty = document.getElementById(inputId).value || 0;
        const r = await fetch(base + "/api/checkout?projectId=" + id + "&qty=" + qty);
        const data = await r.json();
        showMessage(data);
      }}
    </script>
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
