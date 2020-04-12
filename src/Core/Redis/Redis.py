import redis
from Web.Configs.AppSettings import REDIS_ADDRESS


class Redis:
    pool = None

    def __new__(cls):
        if not Redis.pool:
            addr = REDIS_ADDRESS.split(':')
            Redis.pool = redis.BlockingConnectionPool(host=addr[0], port=addr[1], db=0, max_connections=100)
        return redis.Redis(connection_pool=Redis.pool)
