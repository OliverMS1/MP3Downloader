from crypt import methods
from flask import Flask, render_template, request
from test import lookup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        
       lookup(request.form.get("link"))

       return render_template("index.html") 

    else:
        return render_template("index.html")