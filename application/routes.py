from application import app
from flask import render_template, Response, request


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html",index=True)

@app.route("/login")
def login():
    return render_template("login.html",login=True)

@app.route("/register")
def register():
    return render_template("register.html",register=True)

@app.route("/movies")
def movies():
    moviesData=[{"mid":"1","name": "Pulp Fiction","poster": "static/images/Pulpfiction.jpg"},
                {"mid":"2","name": "The Shawshank Redemption", "poster": "static/images/Shawshank.jpg"},
                {"mid":"3","name": "Goodfellas", "poster": "static/images/Goodfellas.jpg"}]
    return render_template("movies.html",movies=True,moviesData=moviesData)

@app.route("/booking")
def booking():
    id = request.args.get('movieID')
    name = request.args.get('mname')
    poster = request.args.get('mposter')
    data = {'id':id,'name':name,'poster':poster}
    return render_template("booking.html",booking=True,data=data)