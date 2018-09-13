#--encoding:utf-8--
'''
Created on 2017年10月20日

@author: root
'''
from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster("local").setAppName("AggregateByKey")
sc = SparkContext(conf = conf)

rdd1 = sc.parallelize(range(0,10))
randomSplitRDD = rdd1.randomSplit([0.2,0.8],10)

def f(a):
    print a

for rdd in randomSplitRDD:
    print '============='
    rdd.foreach(f)
