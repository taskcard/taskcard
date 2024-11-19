from server import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    category = db.Column(db.String(200), nullable=False, index=True)  
    modify_date = db.Column(db.DateTime(), nullable=True, default=None)  
    create_date = db.Column(db.DateTime(), nullable=False) 