# -*- coding: utf-8 -*-
 
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pprint import pprint


if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("abc")
    sc = SparkContext(conf = conf)
    ssc = StreamingContext(sc,5)
    directKafkaStream = ssc.socketTextStream("hadoop1",9999)
    directKafkaStream\
        .flatMap(lambda x:x[1].split(" "))\
        .map(lambda x:(x,1))\
        .reduceByKey(lambda x,y:x+y)\
        .pprint()
    ssc.start()
    ssc.awaitTermination()