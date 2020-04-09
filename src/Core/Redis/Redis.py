import redis
import time
from Web.Static import REDIS_ADDRESS, APP_NAME
import atexit


class Redis:
    pool = None

    def __new__(cls):
        if not Redis.pool:
            addr = REDIS_ADDR[0].split(':')
            Redis.pool = redis.BlockingConnectionPool(host=addr[0], port=addr[1], db=0, max_connections=100)
        return redis.Redis(connection_pool=Redis.pool)


class RedisLock(object):
    def __init__(self, key, expires=60, timeout=10):
        self.key = f'{APP_NAME}::lock::{key}'
        self.timeout = timeout
        self.expires = expires

    def __enter__(self):
        self.redis = Redis()
        timeout = self.timeout
        while timeout >= 0:
            expires = time.time() + self.expires + 1

            if self.redis.setnx(self.key, expires):
                return

            current_value = self.redis.get(self.key)

            if current_value and float(current_value) < time.time() and \
                    self.redis.getset(self.key, expires) == current_value:
                return

            timeout -= 1
            time.sleep(1)

        raise Exception("timeout whilst waiting for lock")

    def __exit__(self, exc_type, exc_value, traceback):
        self.redis.delete(self.key)


class RedisSequencer(object):
    def __init__(self, key, expires=120, sleep=10):
        self.key = f'{APP_NAME}::sequencer::{key}'
        self.expires = expires
        self.sleep = sleep

        def ex():
            self.redis.delete(self.key)

        atexit.register(ex)

    def __enter__(self):
        self.redis = Redis()
        num = self.redis.ttl(self.key)
        if num < 1:
            self.redis.setex(self.key, self.expires, '')
            return True
        return False

    def __exit__(self, exc_type, exc_value, traceback):
        if self.sleep > 0:
            time.sleep(self.sleep)
        self.redis.delete(self.key)
