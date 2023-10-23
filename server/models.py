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
    

class Location(db.Model):
     __tablename__ = 'locations'

     location_id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(100), unique=True, nullable=False)
     latitude = db.Column(db.Real)
     longitude  = db.Column(db.Real)

     def __init__ (self, name, latitude, longitude):
        self.name = name 
        self.latitude = latitude 
        self.longitude = longitude

     def __repr__(self):
         return f'<name {self.name}>'
     


class WeatherData(db.Model):
    __tablename__ = 'weather_data'
   
    data_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, ForeignKey('loction_id'))
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    temperature = db.Column(db.Real, nullable=False)
    humidity = db.Column(db.Real, nullable=False)
    wind_speed = db.Column(db.Real, nullable=False)
    weather_condition = db.Column(db.String(100), nullable=False)


    def __init__ (self, temperature, humidity, wind_speed, weather_condition):
        self.temperature = temperature 
        self.humidity = humidity 
        self.wind_speed = wind_speed
        self.weather_condition = weather_condition

    def __repr__(self):
        return f' <
        temperature {self.temperature} 
        humidity  {self.humidity} 
        windspeed {self.wind_speed}>'

