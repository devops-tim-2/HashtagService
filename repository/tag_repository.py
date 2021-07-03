from models.models import Tag
from common.database import db_session


def save(tag: Tag):
    db_session.add(tag)
    db_session.commit()


def get_with_value(value: str):
    return Tag.query.filter_by(value=value).first()
