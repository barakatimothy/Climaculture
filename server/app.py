from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DATABASE_URI'] = ''

db = SQLAlchemy(app)
