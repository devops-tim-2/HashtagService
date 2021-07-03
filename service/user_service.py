from models.models import User
from repository import user_repository
from service import post_service

def save(user_data: dict):
    user = User(id=user_data['id'], public=user_data['public'])
    
    user_repository.save(user)

def update(user_data: dict):
    user_repository.update(user_data)

def delete(user_id: int):
    post_service.delete_with_user(user_id)
    user_repository.delete(user_id)