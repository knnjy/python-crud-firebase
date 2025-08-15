from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth, firestore
from functools import wraps
 
# Load environment variables
load_dotenv()
 
app = Flask(__name__)
  
# Init Firebase Admin
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
 
# Auth decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({"message": "Token is missing"}), 401
        try:
            decoded_token = auth.verify_id_token(token)
            request.user = decoded_token
        except Exception as e:
            return jsonify({"message": "Token is invalid", "error": str(e)}), 401
        return f(*args, **kwargs)
    return decorated
 
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    try:
        user = pb_auth.create_user_with_email_and_password(email, password)
        return jsonify({"message": "User created successfully", "user": user}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
 
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    try:
        user = pb_auth.sign_in_with_email_and_password(email, password)
        token = user['idToken']
        return jsonify({"token": token})
    except Exception as e:
        return jsonify({"error": str(e)}), 401
 
# CRUD: Read
@app.route('/users', methods=['GET'])
# @token_required
def get_users():
    users = [doc.to_dict() | {"id": doc.id} for doc in db.collection("users").stream()]
    return jsonify(users)

@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()
    doc_ref = db.collection("users").add(data)
    return jsonify({"message": "User created", "id": doc_ref[1].id})
 
# CRUD: Update
@app.route('/update-user/<id>', methods=['PUT'])
# @token_required
def update_update(id):
    data = request.get_json()
    db.collection("users").document(id).update(data)
    return jsonify({"message": "User updated"})
 
# CRUD: Delete
@app.route('/delete-user/<id>', methods=['DELETE'])
# @token_required
def delete_user(id):
    db.collection("users").document(id).delete()
    return jsonify({"message": "User deleted"})
 
@app.route('/')
def home():
    return jsonify({"message": "Firebase Flask CRUD API is running!"})
 
if __name__ == '__main__':
    app.run(debug=True)