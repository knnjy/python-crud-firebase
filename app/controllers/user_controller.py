from app.services.user_service import UserService
from flask import Blueprint, request, jsonify

user_bp = Blueprint('users', __name__, url_prefix='/api/users')

user_svc = UserService()


@user_bp.get('/list')
def get_users():
    u = user_svc.get_users()
    return jsonify([user.dict() for user in u])

@user_bp.post('/post')
def create_user():
    data = request.json
    return user_svc.create_user(data)
