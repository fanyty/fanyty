import redis

def connect_redis():
    r = redis.StrictRedis(host='r-t4n5bd3w855krqhhsipd.redis.singapore.rds.aliyuncs.com',port=6379,password='OAhh8TMGwiMX',decode_responses=True)
    return r



def test_case_1(r):
    # 模拟周跨度，重置家族d的活跃值
    r.zadd('ksing:RankRedisKey:rank_platform_top_family:WEEK_20240520', {'<family-d-id>': 0})

    # 用户A进入周榜
    r.zadd('ksing:RankRedisKey:rank_platform_top_family:WEEK_20240520', {'<user-a-id>': 0})

    # 验证结果
    score = r.zscore('ksing:RankRedisKey:rank_platform_top_family:WEEK_20240520', '<family-d-id>')
    assert score == 0, "Test Case 1 Failed"

def test_case_2(r):
    # 模拟周跨度，重置家族d的活跃值
    r.zadd('ksing:RankRedisKey:rank_platform_top_family:WEEK_20240520', {'<family-d-id>': 0})

    # 家族d获得10活跃值
    r.zadd('ksing:RankRedisKey:rank_platform_top_family:WEEK_20240520', {'<family-d-id>': 10})

    # 用户A进入周榜
    r.zadd('ksing:RankRedisKey:rank_platform_top_family:WEEK_20240520', {'<user-a-id>': 0})

    # 验证结果
    score = r.zscore('ksing:RankRedisKey:rank_platform_top_family:WEEK_20240520', '<family-d-id>')
    assert score == 10, "Test Case 2 Failed"

if __name__ == "__main__":
    r = connect_redis()
    test_case_1(r)
    test_case_2(r)
    print("All test cases passed.")