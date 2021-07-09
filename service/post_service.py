from exception.exceptions import InvalidDataException
from models.models import Post, Tag
from service import posttag_service, tag_service
from repository import post_repository

def create(post_data: dict):
    post = Post(id=post_data['id'], user_id=post_data['user_id'])

    post_repository.create(post)

    description:str = post_data['description']

    if len(description) == 0:
        return

    hashtags = list(filter(lambda word: word.startswith('#'), description.split(' ')))
    for hashtag in hashtags:
        try:
            if tag_service.exists(hashtag[1:]):
                tag = tag_service.get_with_value(hashtag[1:])
            else:
                tag = Tag(value=hashtag[1:])
                tag_service.save(tag)
        except Exception as e:
            print(e)
        posttag_service.create(post.id, tag.id)

def get_with_tag(value: str, page: int, per_page: int):
    if not value:
        raise InvalidDataException("You didn't provide a hashtag.")
    
    posts = [id[0] for id in post_repository.get_with_tag(value)]

    return posts[(page-1)*per_page : page*per_page]

def delete(post_id: int):
    posttag_service.delete_with_post(post_id)
    post_repository.delete(post_id)

def delete_with_user(user_id: int):
    posttag_service.delete_with_user(user_id)
    post_repository.delete_with_user(user_id)
