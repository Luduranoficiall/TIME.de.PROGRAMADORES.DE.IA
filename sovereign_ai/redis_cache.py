import redis
import os
import time

REDIS_URL = os.getenv("REDIS_URL")
r = redis.Redis.from_url(REDIS_URL)

def rate_limit(tenant_id: str, limit: int, window: int) -> bool:
    key = f"rate:{tenant_id}"
    current = r.incr(key)
    if current == 1:
        r.expire(key, window)
    return current <= limit

def cache_set(key: str, value: str, ttl: int = 60):
    r.setex(key, ttl, value)

def cache_get(key: str):
    return r.get(key)
