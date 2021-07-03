from models.models import Tag
from repository import tag_repository

def save(value: str):
    tag = Tag(value=value)

    tag_repository.save(tag)

def get_with_value(value: str):
    return tag_repository.get_with_value(value)