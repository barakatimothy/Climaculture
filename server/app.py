from flask import Flask, render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from models import User

my_url= 'https:localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Welcome to the Weather App!"

@app.route('/users', methods=['GET'])
def get_users():
   users = User.query.all()
   user_list =[{'user_id': user.id ,'user_name':user.username, 'email':user.enail}for user in users]
   return jsonify(user_list)
@app.route('/users',methods=['POST'])
def create_user():
    data = request.get_json()
    if 'username' in data and 'email' in data and 'password' in data:
        new_user = User(username=data['username'], email=data['email'], password_hash=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'user created succesfully'})
    else:
        return jsonify({'error': 'Missing required data'})
@app.route('/locations')
def locations():
    return "Location List"

@app.route('/weather_data')
def weather_data():
    return "Weather Data List"

if __name__ == '__main__':
    app.run(debug=True)
