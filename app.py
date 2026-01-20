from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about")
@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/membership")
@app.route("/membership.html")
def membership():
    return render_template("membership.html")


app.run(debug=True)