#--encoding:utf-8--
'''
Created on 2018年1月6日

@author: root
'''
from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster("local").setAppName("AggregateByKey")
sc = SparkContext(conf = conf)
accumulator = sc.accumulator(0)
rdd = sc.parallelize([(1,1),(1,2),(2,1),(2,3),(2,4),(1,7)],2)
rdd.map(lambda x:accumulator.add(1)).count()
def fun(x):
    accumulator.add(1)
    print accumulator.value
rdd.map(fun).count()
print accumulator.value
sc.stop()
