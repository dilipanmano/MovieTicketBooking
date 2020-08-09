import flask
from application import db

class Users(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField()
    password = db.StringField(max_length=24)

class Movies(db.Document):
    mid = db.IntField(unique=True)
    mname = db.StringField()
    mposter = db.StringField()
    width = db.IntField()
    height = db.IntField()

class Booking(db.Document):
    user_id = db.IntField()
    mid = db.IntField()