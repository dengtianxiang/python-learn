# -*- coding: utf-8 -*-
'''
@author: zfg
'''
from pyspark.sql.context import HiveContext
from pyspark import SparkConf
from pyspark import SparkContext

def initSparkConf(isLocal,appName):
    conf = SparkConf()
    conf.setAppName(appName)
    if isLocal is True:
        conf.setMaster("local[*]")
    return conf

def initSparkContext(conf):
    return SparkContext(conf=conf)
conf =  initSparkConf(False, "HiveDataSource")
sc =  initSparkContext(conf)
hiveContext = HiveContext(sc);
hiveContext.sql("DROP TABLE IF EXISTS student_infos");
hiveContext.sql("CREATE TABLE IF NOT EXISTS student_infos (name STRING, age INT) row format delimited fields terminated by '\t'");
hiveContext.sql("LOAD DATA "
  + "LOCAL INPATH '/root/resource/student_infos' "
  + "INTO TABLE student_infos");

hiveContext.sql("DROP TABLE IF EXISTS student_scores");
hiveContext.sql("CREATE TABLE IF NOT EXISTS student_scores (name STRING, score INT) row format delimited fields terminated by '\t'");
hiveContext.sql("LOAD DATA "
  + "LOCAL INPATH '/root/resource/student_scores' "
  + "INTO TABLE student_scores");

goodStudentsDF = hiveContext.sql("SELECT si.name, si.age, ss.score "
      + "FROM student_infos si "
      + "JOIN student_scores ss ON si.name=ss.name "
      + "WHERE ss.score>=80");
hiveContext.sql("DROP TABLE IF EXISTS result.good_student_infos");
hiveContext.sql("USE result")
goodStudentsDF.write.saveAsTable("good_student_infos")
