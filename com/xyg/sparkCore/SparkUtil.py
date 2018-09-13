# encoding: utf-8
from pyspark import SparkConf
from pyspark import SparkContext
'''
Created on 2017年11月29日

@author: root
'''
 
def initSparkConf(isLocal,appName):
    conf = SparkConf()
    conf.setAppName(appName)
    if isLocal is True:
        conf.setMaster("local[*]")
    return conf


def initSparkContext(conf):
    return SparkContext(conf=conf)

def createRDD(isLocal,appName,filePath):
    conf = initSparkConf(isLocal, appName)
    sc = initSparkContext(conf)
    return sc.textFile(filePath,2000)
