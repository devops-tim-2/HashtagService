from models.models import PostTag
from common.database import db_session


def delete_with_post(post_id: int):
    PostTag.query.filter_by(post_id=post_id).delete()
    db_session.commit()

def delete_with_user(user_id: int):
    PostTag.query.filter_by(user_id=user_id).delete()
    db_session.commit()

def find(post_id: int, tag_id: int):
    return bool(PostTag.query.filter_by(post_id=post_id, tag_id=tag_id).first())

def save(post_tag: PostTag):
    db_session.add(post_tag)
    db_session.commit()