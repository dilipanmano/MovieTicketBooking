from application import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Movie Home<h1>"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/movies")
def movies():
    return "<h1>Movie list</h1>"

@app.route("/booking")
def booking():
    return "<h1>Booking</h1>"