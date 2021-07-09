from models.models import Tag
from common.database import db_session
from models.models import Model
from sqlalchemy.sql import exists

def save(tag: Tag):
    db_session.add(tag)
    db_session.commit()


def get_with_value(value: str):
    Model.query = db_session.query_property()
    return Tag.query.filter_by(value=value).first()

def existsx(value):
    return db_session.query(exists().where(Tag.value == value)).scalar()