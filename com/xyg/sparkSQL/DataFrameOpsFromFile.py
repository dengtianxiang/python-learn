# -*- coding: utf-8 -*-
'''
Created on 2018年1月5日

@author: root
'''
from com.xyg.python.test import SparkUtil
from pyspark.sql.context import SQLContext
conf = SparkUtil.initSparkConf(True, "DataFrameOpsFromFile")
sc = SparkUtil.initSparkContext(conf)
sqlContext = SQLContext(sc)
df = sqlContext.read.json("../data/people.json")
df.show()
df.registerTempTable("people")
sqlContext.sql("select * from people where age > 20").show()
sc.stop()


