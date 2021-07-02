from dataclasses import dataclass, asdict

from sqlalchemy import Column, Integer, String, Boolean, \
     ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base(name='Model')


@dataclass
class PostTag(Model):
    id: int
    post_id: int
    user_id: int

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('userprofile.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'PostTag: id={self.id}, post_id={self.post_id}, user_id={self.user_id}'


@dataclass
class Post(Model):
    id: int
    post_id: int

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Post: id={self.id}, post_id={self.post_id}'


@dataclass
class Tag(Model):
    id: int
    value: str

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(100), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Tag: id={self.id}, value={self.value}'


@dataclass
class User(Model):
    __tablename__ = 'userprofile'

    id: int
    public: bool

    id = Column(Integer, primary_key=True)
    public = Column(Boolean, nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'User: id={self.id}, public={self.public}'
