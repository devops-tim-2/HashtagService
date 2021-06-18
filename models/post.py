from common.database import db
from dataclasses import dataclass, asdict


@dataclass
class Post(db.Model):
    id: int
    post_id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Post: id={self.id}, post_id={self.post_id}'
