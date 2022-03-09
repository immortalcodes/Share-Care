 
from unicodedata import name
import psycopg2

from flask import Flask, render_template, request

app = Flask(__name__)
postgresql_uri="postgres://eaqqbrqz:yDS2nKH7_pTOFqK45gaoHTtMa_M5SlcJ@satao.db.elephantsql.com/eaqqbrqz"

connection= psycopg2.connect(postgresql_uri)
try:
 with connection:
    with connection.cursor() as cursor:
        cursor.execute("Create Table details(Name TEXT,Room REAL,Phone REAL,Details TEXT);")
except psycopg2.errors.DuplicateTable:
    pass



@app.route("/form", methods=["GET", "POST"])
def home():
    if request.method == "POST":

     print(request.form)
     with connection:
         with connection.cursor() as cursor:
             cursor.execute(
                 "insert into details values(%s,%s,%s,%s);",(
         request.form.get("name"),
         request.form.get("room"),
         request.form.get("phone"),
         request.form.get("details")) 
             )
    
    return render_template("form.html")

@app.route("/")
def display_details():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("select * from details")
            details=cursor.fetchall()
    return render_template("explore.html", entries = details)
@app.route("/about")
def display_aboutus():
    return render_template("about.html")