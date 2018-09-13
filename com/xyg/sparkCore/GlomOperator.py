#--encoding:utf-8--
'''
Created on 2017年10月20日

@author: root
'''
from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster("local").setAppName("GlomOperator")
sc = SparkContext(conf = conf)

rdd1 = sc.parallelize(range(0,10),2)
glomRDD = rdd1.glom()

def f(a):
    print a

glomRDD.foreach(f) 
