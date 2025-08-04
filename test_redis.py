import redis

try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    pong = r.ping()
    if pong:
        print("Redis is running and responding! ✅")
except Exception as e:
    print("Redis connection failed ❌")
    print(e)
