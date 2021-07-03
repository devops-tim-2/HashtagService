from os import environ
environ['SQLALCHEMY_DATABASE_URI'] = environ.get("TEST_DATABASE_URI")

from models.models import PostTag, Tag, Post, User
from common.config import setup_config


class TestHashtag:
    @classmethod
    def setup_class(cls):
        cls.app = setup_config('test')
        from common.database import db_session

        cls.user1 = User(public=True)
        cls.user2 = User(public=False)

        db_session.add(cls.user1)
        db_session.add(cls.user2)
        db_session.commit()

        cls.post1 = Post(user_id=cls.user1.id)
        cls.post2 = Post(user_id=cls.user2.id)
        cls.post3 = Post(user_id=cls.user2.id)

        db_session.add(cls.post1)
        db_session.add(cls.post2)
        db_session.add(cls.post3)
        db_session.commit()

        cls.tag1 = Tag(value="goodday")
        cls.tag2 = Tag(value="sunnyday")
        cls.tag3 = Tag(value="lifeisbeautiful")

        db_session.add(cls.tag1)
        db_session.add(cls.tag2)
        db_session.add(cls.tag3)
        db_session.commit()

        cls.posttag1 = PostTag(post_id=cls.post1.id, tag_id=cls.tag1.id)
        cls.posttag2 = PostTag(post_id=cls.post1.id, tag_id=cls.tag2.id)
        cls.posttag3 = PostTag(post_id=cls.post2.id, tag_id=cls.tag1.id)
        cls.posttag4 = PostTag(post_id=cls.post2.id, tag_id=cls.tag3.id)
        cls.posttag5 = PostTag(post_id=cls.post3.id, tag_id=cls.tag3.id)

        db_session.add(cls.posttag1)
        db_session.add(cls.posttag2)
        db_session.add(cls.posttag3)
        db_session.add(cls.posttag4)
        db_session.add(cls.posttag5)
        db_session.commit()

        cls.client = cls.app.test_client()


    def test_get_happy(cls):
        value = cls.tag1.value

        get_response = cls.client.get(f'/api/{value}', headers={'Content-Type': 'application/json'}).get_json()
        assert len(get_response) == 1


    def test_get_sad(cls):
        value = None

        get_response = cls.client.get(f'/api/trlababalan', headers={'Content-Type': 'application/json'}).get_json()
        assert len(get_response) == 0
