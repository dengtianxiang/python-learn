# --encoding:utf-8--
from __future__ import print_function

import sys

from pyspark import SparkContext


if __name__ == "__main__":
    sc = SparkContext(appName="WC")
    lines = sc.textFile("hdfs://hadoop1:9000/input/log.txt")
    wordRDD = lines.flatMap(lambda x: x.split(' '))
    pairRDD = wordRDD.map(lambda x: (x, 1)) 
    resultRDD = pairRDD.reduceByKey(lambda v1,v2:v1+v2)
    resultRDD.sortBy(lambda x:x[1]).saveAsTextFile("hdfs://hadoop1:9000/result/nongda")
    sc.stop()