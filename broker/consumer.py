import json
from common.database import db_session
from models.models import Post, PostTag, User
from service import post_service, user_service

class PostConsumer:
    def __init__(self, channel):
        self.exchange_name = 'post'
        self.channel = channel
        channel.exchange_declare(exchange=self.exchange_name, exchange_type='fanout')
        q = channel.queue_declare(queue='')
        channel.queue_bind(exchange=self.exchange_name, queue=q.method.queue)
        channel.basic_consume(queue=q.method.queue, on_message_callback=self.on_message, auto_ack=True)

    def on_message(self, ch, method, properties, body):
        try:
            data = json.loads(body)

            if properties.content_type == 'post.created':      
                print('here')      
                post_service.create(data)
            elif properties.content_type == 'post.deleted':
                post_service.delete(data['id'])
        except Exception:
            # don't crash
            pass

class UserConsumer:
    def __init__(self, channel):
        self.exchange_name = 'user'
        self.channel = channel
        channel.exchange_declare(exchange=self.exchange_name, exchange_type='fanout')
        q = channel.queue_declare(queue='')
        channel.queue_bind(exchange=self.exchange_name, queue=q.method.queue)
        channel.basic_consume(queue=q.method.queue, on_message_callback=self.on_message, auto_ack=True)

    def on_message(self, ch, method, properties, body):
        try:
            data = json.loads(body)

            if properties.content_type == 'user.created':            
                user_service.save(data)
            elif properties.content_type == 'user.deleted':
                user_service.delete(data['id'])
            elif properties.content_type == 'user.updated':
                user_service.update(data)
        except Exception:
            # don't crash
            pass
