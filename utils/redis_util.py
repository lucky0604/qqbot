import redis


def get_redis():
    redis_client = redis.Redis(host="localhost",
                               port=6379,
                               db=1,
                               decode_responses=True)
    return redis_client