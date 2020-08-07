from application import app
from flask import render_template, Response, request,json

moviesData=[{"mid":"1","name": "Pulp Fiction","poster": "static/images/Pulpfiction.jpg","width":"160","height":"190"},
                {"mid":"2","name": "The Shawshank Redemption", "poster": "static/images/Shawshank.jpg","width":"190","height":"190"},
                {"mid":"3","name": "Goodfellas", "poster": "static/images/Goodfellas.jpg","width":"160","height":"190"}]

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
    
    return render_template("movies.html",movies=True,moviesData=moviesData)

@app.route("/booking",methods=["POST","GET"])
def booking():
    id = request.form.get('movieID')
    name = request.form.get('mname')
    poster = request.form.get('mposter')
    width = int(request.form.get('mwidth')) +100 
    height = int(request.form.get('mheight')) +100  
    data = {'id':id,'name':name,'poster':poster,'width':width,'height':height}
    return render_template("booking.html",booking=True,data=data)

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx==None:
        datajson = moviesData 
    else:
        datajson = moviesData[int(idx)]
    return Response(json.dumps(datajson),mimetype="application/json")