from models.models import Tag
from repository import tag_repository

def save(tag):
    tag_repository.save(tag)

def get_with_value(value: str):
    return tag_repository.get_with_value(value)

def exists(value):
    return tag_repository.existsx(value)