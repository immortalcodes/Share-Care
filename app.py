 
from unicodedata import name
from flask import Flask, render_template, request

app = Flask(__name__)
details = [
    ("Parth","R55","890013332","Free time")
]

@app.route("/form", methods=["GET", "POST"])
def home():
    if request.method == "POST":

     print(request.form)
     details.append((
         request.form.get("name"),
         request.form.get("room"),
         request.form.get("phone"),
         request.form.get("details")))
    return render_template("form.html")

@app.route("/")
def display_details():
    return render_template("explore.html", entries = details)
@app.route("/about")
def display_aboutus():
    return render_template("about.html")