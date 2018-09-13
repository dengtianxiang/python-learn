# -*- coding: utf-8 -*-
 
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pprint import pprint


if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("abc")
    sc = SparkContext(conf = conf)
    ssc = StreamingContext(sc,5)
    directKafkaStream = KafkaUtils.createDirectStream(ssc, ["Angelababy"], {"metadata.broker.list": "192.168.126.111:9092,192.168.126.112:9092,192.168.126.113:9092"})
#     KafkaUtils.createStream(ssc, zkQuorum, groupId, topics, kafkaParams, storageLevel, keyDecoder, valueDecoder)
    directKafkaStream\
        .flatMap(lambda x:x[1].split(" "))\
        .map(lambda x:(x,1))\
        .reduceByKey(lambda x,y:x+y)\
        .pprint()
    ssc.start()
    ssc.awaitTermination()