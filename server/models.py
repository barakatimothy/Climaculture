from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    email = db.Column(db.String(60), nullable=False )
    password_hash = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__ (self, username, email, password_hash):
        self.username = username
        self.email = email 
        self.password_hash = password_hash

    def __repr__(self):
        return f'<User {self.username}>'