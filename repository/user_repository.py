from models.models import User
from common.database import db_session

def save(user: User):
    db_session.add(user)
    db_session.commit()


def update(user_data: dict):
    user = User.query.get(user_data['id'])

    if user.public != user_data['public']:
        user.public = user_data['public']
        db_session.commit()

    
def delete(user_id):
    User.query.filter_by(id=user_id).delete()