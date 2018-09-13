# -*- coding: utf-8 -*-
 
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pprint import pprint


if __name__ == '__main__':
    conf = SparkConf().setMaster("local[2]").setAppName("abc")
    sc = SparkContext(conf = conf)
#     batch Interval 5  
    ssc = StreamingContext(sc,5)
    directKafkaStream = ssc.socketTextStream("hadoop1",9999)
  
#   pprint()类似我们之前所说的action类算子  触发执行  在你的SparkStreaming Application中必须有一个类似Action类的算子
    directKafkaStream\
        .flatMap(lambda x:x.split(" "))\
        .map(lambda x:(x,1))\
        .reduceByKey(lambda x,y:x+y)\
        .pprint()
        
    ssc.start()
    ssc.awaitTermination()