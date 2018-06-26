import psycopg2
from config import config
from flask import Flask, request, abort, make_response, jsonify
import json

app = Flask(__name__)

conn = None

conn_string = "host='localhost' dbname='ride-my-way' user='postgres' password='Ar15tottle'"

@app.route('/api/v2/auth/signup', methods=['POST'])
def register_user():
    if not request.is_json:
        abort(400,"request not json")
    
    if not "name" in request.get_json() or not "password" in request.get_json():
        abort(422,"user name or password missing")
    
    data = request.get_json(force=True)
    name = data['name']
    email = data['email']
    password = data['password']
    dl_path = data['dl_path']
    car_reg = data['car_reg']
    values = [name, email, dl_path, car_reg, password]

    db = psycopg2.connect(conn_string)
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email, dl_path, car_reg, password) VALUES (%s,%s,%s,%s, %s)",values)
    db.commit()
    cursor.close()
    db.close()

    return make_response(jsonify({
        "status":"registered",
        "name":name,
        'email':email
        }),201)

@app.route('/api/v2/auth/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    email = data['email']
    password = data['password']
    values = [email,password]
    db = psycopg2.connect(conn_string)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM users WHERE email = %s AND password = %s",values)
    user_name = cursor.fetchone()
    if user_name is None:
        return make_response(jsonify({"status":"username or password wrong"}),404)
    
    return make_response(jsonify({"status":"success","name":user_name[0]}),200)

    
    

    

    
if __name__ == '__main__':
    app.run(debug=True)










