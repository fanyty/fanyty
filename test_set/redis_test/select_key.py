import redis

def connect_redis():
    r = redis.StrictRedis(host='地址',port="6379",password='密码',decode_responses=True)
    try:
        r.ping()
        print("Connected to Redis successfully!")
        return r
    except redis.exceptions.ConnectionError as e:
        print(f"Failed to connect to Redis: {e}")
        return None

    # return r
def query_data_by_key(r, key):
    if r is None:
        print("Redis connection is not established.")
        return None
    
    try:
        data_type = r.type(key)
        if data_type == 'string':
            return r.get(key)
        elif data_type == 'list':
            return r.lrange(key, 0, -1)
        elif data_type == 'set':
            return r.smembers(key)
        elif data_type == 'zset':
            return r.zrange(key, 0, -1, withscores=True)
        elif data_type == 'hash':
            return r.hgetall(key)
        else:
            return None
    except Exception as e:
        print(f"Error querying data for key {key}: {e}")
        return None

def print_data(key, data):
    if data is None:
        print(f"No data found for key: {key}")
    elif isinstance(data, str):
        print(f"Key: {key}, Value: {data}")
    elif isinstance(data, list):
        print(f"Key: {key}, List Values: {data}")
    elif isinstance(data, set):
        print(f"Key: {key}, Set Members: {data}")
    elif isinstance(data, list) and all(isinstance(i, tuple) for i in data):
        print(f"Key: {key}, ZSet Members: {data}")
    elif isinstance(data, dict):
        print(f"Key: {key}, Hash Values: {data}")
    else:
        print(f"Key: {key}, Unknown Type or Empty")
def list_all_keys(r):
    try:
        keys = r.keys()
        print(f"All keys in Redis: {keys}")
    except Exception as e:
        print(f"Error listing keys: {e}")

def main():
    r = connect_redis()
    if r is None:
        print("Failed to connect to Redis. Exiting.")
        return
    list_all_keys(r)


    key = input("Enter the Redis key to query: ")
    data = query_data_by_key(r, key)
    print_data(key, data)

if __name__ == "__main__":
    main()
