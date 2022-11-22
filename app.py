from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask import render_template, request, redirect, url_for
import projects
app = Flask(__name__)


@app.route("/")
def home_route():
    return render_template("home.html" , projects=projects.setup())
@app.route("/happy/")
def happy_route():
    return render_template("happy.html" , projects=projects.setup())
@app.route("/gloomy/")
def sad_route():
    return render_template("sad.html" , projects=projects.setup())
@app.route("/boredom/")
def bored_route():
    return render_template("bored.html" , projects=projects.setup())
@app.route("/motivated/")
def motivated_route():
    return render_template("motivated.html" , projects=projects.setup())
@app.route("/musicrec")
def musicrec_route():
    return render_template("musicrec.html" , projects=projects.setup())

if __name__ == "__main__":
    app.run(debug=True, port='8008 ', host='127.0.0.1')