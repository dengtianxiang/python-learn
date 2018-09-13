#--encoding:utf-8--
'''
Created on 2017年10月20日

@author: root
'''
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
conf = SparkConf().setMaster("local").setAppName("CombineByKey")
sc = SparkContext(conf = conf)
rdd = sc.parallelize([("A",1),("B",2),("B",3),("B",4),("B",5),("C",1),("A",2)], 2)
def f(index,items):
    print "partitionId:%d" %index
    for val in items:
        print val
    return items
rdd.mapPartitionsWithIndex(f).count()

combinerRDD = rdd.combineByKey(lambda x:"%d_" %x, lambda a,b:"%s@%s" %(a,b), lambda a,b:"%s$%s" %(a,b))

def mergeValue(list1,b):
    list1.append(b)
    return list1
     
def mergeCombiners(list1,list2):
    list1.extend(list2)
    return list1
     
groupByKeyRDD = rdd.combineByKey(lambda a:[a],mergeValue,mergeCombiners)
# 
reduceByKeyRDD = rdd.combineByKey(lambda a:a,lambda a,b:a+b,lambda a,b:a+b)

def p(x):
    print x
     
# combinerRDD.foreach(p)
reduceByKeyRDD.foreach(p)
# for item in reduceByKeyRDD.take(2):
#     print item
#     first() = take(1)
# print reduceByKeyRDD.first()
# groupByKeyRDD.foreach(p)

sc.stop()

