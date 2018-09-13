#--encoding:utf-8--
'''
Created on 2017年10月20日

@author: root
'''
from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster("local").setAppName("AggregateByKey")
sc = SparkContext(conf = conf)

rdd1 = sc.parallelize(range(0,10))
rdd2 = sc.parallelize(range(10,20))
zipRest = rdd1.zip(rdd2)

def f(a):
    print a

zipRest.foreach(f)

