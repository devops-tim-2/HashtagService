from models.models import Post, PostTag, Tag, User
from common.database import db_session

def create(post: Post):
    db_session.add(post)
    db_session.commit()

def delete(post_id: int):
    Post.query.filter_by(id=post_id).delete()
    db_session.commit()

def delete_with_user(user_id: int):
    Post.query.filter_by(user_id=user_id).delete()
    db_session.commit()

def get_with_tag(value: str):
    return db_session.query(Post.id)\
                     .join(User)\
                     .join(PostTag)\
                     .join(Tag)\
                     .filter(User.public == True, Tag.value == value)\
                     .order_by(Post.id.desc())\
                     .all()
