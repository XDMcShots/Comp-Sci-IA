from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = "supersecretkey"  # change this to something random
app.permanent_session_lifetime = timedelta(days=7)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Events page
@app.route("/events")
def events():
    return render_template("events.html")

# Get Involved page
@app.route("/get_involved")
def get_involved():
    return render_template("get_involved.html")

# Team page
@app.route("/team")
def team():
    return render_template("team.html")


# ---------------------------
# Login Page
def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode("utf-8")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admins WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(password, user["password"]):
            session.permanent = True
            session["user"] = username
            return redirect(url_for("admin_dashboard"))
        else:
            return "Invalid credentials. Try again."

    return render_template("login.html")


# ---------------------------
# Admin Dashboard (protected)
@app.route("/admin")
def admin_dashboard():
    if "user" in session:
        return render_template("admin_dashboard.html", user=session["user"])
    else:
        return redirect(url_for("login"))

# ---------------------------
# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
