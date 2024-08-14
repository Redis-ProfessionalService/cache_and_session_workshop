import os
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = 16379


class RedisConnection(object):

    @staticmethod
    def get_client():
        return redis.Redis(host=REDIS_HOST,
                           port=REDIS_PORT,
                           decode_responses=True)
