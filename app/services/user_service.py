from app.dao.user_dao import UserDAO
from app.dto.user_response_dto import UserResponseDTO
from flask import request


class UserService:
    def __init__(self):
        self.userDAO = UserDAO()
    
    def get_users(self):

        rows = self.userDAO.get_users()
        
        return [UserResponseDTO(**row) for row in rows]

    def create_user(self, data: dict):
        user_id = self.userDAO.create_user(data)
        return {"id": user_id}, 201
