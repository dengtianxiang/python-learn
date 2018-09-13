# -*- coding: utf-8 -*-
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
class SparkUtil(object):
    @staticmethod
    def initSparkConf(isLocal,appName):
        conf = SparkConf()
        conf.setAppName(appName)
        if isLocal is True:
            conf.setMaster("local[2]")
        return conf

    @staticmethod
    def initSparkContext(conf):
        return SparkContext(conf=conf)

    @staticmethod
    def initSparkStreamingContext(sc,batchInterval):
        return SparkContext(sc,batchInterval)


class RealTimeCalculateRoadState(object):
    @staticmethod
    def calculateRoadState():
        conf = SparkUtil.initSparkConf(True,"RealTimeCalculateRoadState")
        sc = SparkUtil.initSparkContext(conf)
        ssc = SparkUtil.initSparkStreamingContext(sc,5)

if __name__ == "__main__":
    RealTimeCalculateRoadState.calculateRoadState()