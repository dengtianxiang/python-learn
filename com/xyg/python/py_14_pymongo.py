#--coding:utf-8--
#pip.exe install pymongo
from pymongo import MongoClient

import random

client = MongoClient()
client = MongoClient('hadoop1', 27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client['mine'] #连接库
collection = db['mine']

#用户认证
collection.drop()
#删除集合user
collection.save({'id':1,'name':'kaka','sex':'male'})

#插入一个数据
for id in range(2,10):
    name = random.choice(['steve','koby','owen','tody','rony'])
    sex = random.choice(['male','female'])
    db.user.insert({'id':id,'name':name,'sex':sex}) 
#通过循环插入一组数据
ct = db['user'].find()
for i in ct:
    print i


content = db.user.find()
#打印所有数据
for i in content:
    print i

client.close()