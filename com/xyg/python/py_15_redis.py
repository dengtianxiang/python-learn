# -*- coding=utf-8 -*-
import redis

pool = redis.ConnectionPool(host='hadoop1', port='6379',db=2)
r = redis.Redis(connection_pool=pool)
# f = open('../data/ModelFile.txt')
# f = open('../data/UserItemsHistory.txt')
f = open('../data/ItemList.txt')
while True:
    lines = f.readlines(100)
    if not lines:
        break
    for line in lines:
        kv = line.split('\t')
#         r.hset("rcmd_features_score", kv[0], kv[1])
#         r.hset('rcmd_user_history', kv[0], kv[1])
        r.hset('rcmd_item_list', kv[0], line[:-2])
f.close()