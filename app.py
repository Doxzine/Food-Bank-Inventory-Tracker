from flask import Flask, jsonify, request, render_template
from database import Database
import hashlib

db = Database()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inventory", methods=["GET"])
def get_inventory():
    items = db.list_all()
    return jsonify(items)

@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()
    name = data["name"]
    quantity = data["quantity"]
    item_type = data["type"]
    db.add_item(name, quantity, item_type)
    db.log_action("api", "added item", f"{quantity} {name}")
    return jsonify({"message": f"{name} added"})

@app.route("/inventory", methods=["DELETE"])
def remove_item():
    data = request.get_json()
    name = data["name"]
    db.remove_item(name)
    db.log_action("api", "removed item", f"{name}")
    return jsonify({"message": f"{name} removed"})

@app.route("/inventory/<name>", methods=["GET"])
def find_item(name):
    item = db.find_item(name)
    if item:
        return jsonify({"name": item[0], "quantity": item[1], "type": item[2]})
    else:
        return jsonify({"error": f"{name} not found"})
    
    
@app.route("/management", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    role = data["role"]
    db.add_user(username, password, role)
    db.log_action("api", "added user", f"{username}")
    return jsonify({"message": f"{username} created"})

@app.route("/management", methods=["DELETE"])
def remove_user():
    data = request.get_json()
    username = data["username"]
    db.remove_user(username)
    return jsonify({"message": f"{username} removed"})

@app.route("/management", methods=["GET"])
def list_users():
    users = db.list_users()
    return jsonify(users)

@app.route("/management/audit", methods=["GET"])
def list_audit_log():
    audit = db.list_audit_log()
    return jsonify(audit)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    row = db.get_user(username)
    if row and row[1] == hashlib.sha256((password + row[2]).encode()).hexdigest():
        return jsonify({"message": f"Welcome {username}", "role": row[3]})
    else:
        db.log_action("api", "Failed Login", f"{username}")
        return jsonify({"error": "Invalid username or password"})
    
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
    
if __name__ == "__main__":
    app.run(debug=True)