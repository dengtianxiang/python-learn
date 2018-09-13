# encoding:utf-8
'''
Created on 2018年1月29日

@author: root
'''
import SparkUtil
import sys

if __name__ == '__main__':
   inputPath = sys.argv[1]

   outputPath = sys.argv[2]

    conf = SparkUtil.initSparkConf(True, "WordCount")
    sc = SparkUtil.initSparkContext(conf)
    sc\
        .textFile(inputPath)\
        .flatMap(lambda line:line.split(" "))\
        .map(lambda word:(word,1))\
        .reduceByKey(lambda v1,v2:v1+v2)\
        .sortBy(lambda t:t[1],False)\
        .saveAsTextFile(outputPath)
    sc.stop()
    
    
