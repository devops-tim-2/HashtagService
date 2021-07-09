from models.models import PostTag
from repository import posttag_repository


def create(post_id: int, tag_id: int):
    post_tag = PostTag(post_id=post_id, tag_id=tag_id)
    posttag_repository.save(post_tag)


def delete_with_post(post_id: int):
    posttag_repository.delete_with_post(post_id)


def delete_with_user(user_id: int):
    posttag_repository.delete_with_user(user_id)