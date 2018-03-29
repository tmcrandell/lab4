from flask import (Flask,render_template)
import random

app = Flask(__name__)

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/random")
def anything():
    return render_template("random.html",
                           val=random.random())
