from application import app


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Movie Home<h1>"

@app.route("/login")
def login():
    return "<h1>Login</h1>"

@app.route("/register")
def register():
    return "<h1>Register</h1>"

@app.route("/movies")
def movies():
    return "<h1>Movie list</h1>"

@app.route("/booking")
def booking():
    return "<h1>Booking</h1>"