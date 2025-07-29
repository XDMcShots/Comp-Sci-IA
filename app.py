from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
