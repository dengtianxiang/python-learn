# -*- coding:utf-8 -*-
from pyspark import SparkConf,SparkContext
import sys

class SparkUtil(object):
    @staticmethod
    def initSparkConf(isLocal,appName):
        conf = SparkConf()
        conf.setAppName(appName)
        if isLocal is True:
            conf.setMaster("local")
        return conf

    @staticmethod
    def initSparkContext(conf):
        return SparkContext(conf=conf)

    @staticmethod
    def createRDD(isLocal,appName,filePath):
        conf = SparkUtil.initSparkConf(isLocal, "PVAnalyze")
        sc = SparkUtil.initSparkContext(conf)
        return sc.textFile(filePath)

class PUVAnalyze(object):
    @staticmethod
    def f(x): print(x)

    def pageId2One(self,x):
        splited = x.split("\t")
        return (splited[3],1)

    def pageId2UserId(self,x):
        splited = x.split("\t")
        return (int(splited[3]),splited[2])

    def distinctUserId(self,iterator):
        ret = []
        for item in iterator:
            distinctUsers = set([])
            for userId in item[1]:
                distinctUsers.add(userId)
            ret.insert(0,(item[0],len(distinctUsers)))
        return ret

    @staticmethod
    def getActiveUserPerChannel(item):
        hotchannel = item[0]
        userIds = item[1]
        userIdCount = {}
        rest = []
        for userId in userIds:
            if userId in userIdCount:
                userIdCount[userId] = userIdCount[userId] + 1
            else:
                userIdCount[userId] = 1

        sortuserIdCount = sorted(userIdCount.items(),key=lambda x:x[1],reverse=True)
        for i in range(len(sortuserIdCount)-1,9,-1):sortuserIdCount.pop(i)
        print len(sortuserIdCount)
        for item in sortuserIdCount:
            rest.insert(0,(hotchannel,"%s_%d" %(item[0],item[1])))
        return rest

    def getVistHotChannelNumPerUser(self,item):
        userId = item[0]
        channles = item[1]
        channel2Count = {}
        rest = []
        for channel in channles:
            if(channel in channel2Count):
                channel2Count[channel]  = channel2Count[channel] + 1
            else:
                channel2Count[channel] = 1

        for channel,count in channel2Count.items():
            rest.insert(0,(channel,"%s_%d" %(userId,count)))
        return rest

    def getTop10ActivePerChannel(self,item):
        channel = item[0]
        userId2Counts = item[1]
        sorts = ['','','']
        for userId2Count in userId2Counts:
            splited = userId2Count.split("_")
            userId = splited[0]
            count = int(splited[1])
            for i in range(0,len(sorts)):
                if sorts[i] == '':
                    sorts[i] = userId2Count
                    break
                elif count > int(sorts[i].split("_")[1]):
                    for j in range(len(sorts) - 1,i,-1):
                        sorts[j] = sorts[j-1]
                    sorts[i] = userId2Count
                    break
        print type(channel)
        print "%s最活跃的用户有：%s,%s,%s" %(channel.encode("utf-8"),sorts[0].encode("utf-8"),sorts[1].encode("utf-8"),sorts[2].encode("utf-8"))

    @staticmethod
    def PVAnalyze(isLocal,inputPath,outputPath):
        puva = PUVAnalyze()
        filePath = inputPath
        rdd = SparkUtil.createRDD(isLocal,"PVAnalyze",filePath)
        results = rdd\
            .filter(lambda x:x.split("\t")[5] != 'Register')\
            .map(puva.pageId2One)\
            .reduceByKey(lambda a,b:a+b)\
            .map(lambda x:(x[1],x[0]))\
            .sortByKey(False)\
            .map(lambda x:(x[1],x[0]))\
            .saveAsTextFile(outputPath)
            # .foreach(PUVAnalyze.f)

#         resultss = rdd\
#             .filter(lambda x:x.split("\t")[5] != 'Register')\
#             .map(puva.pageId2One)\
#             .countByKey()
        #如何查看对象的类型  通过type方法可以查看
        
#         print type(resultss)
        #通过type方法可以知道数据类型是dict  dict字典表遍历方法如下：
#         for i in resultss:
#             print "dict[%s]=%d" % (i, resultss[i])

        # for k,v in results.items():
        #     print  k+"="+v

        # for (k,v) in results.iteritems():
        #     print "dict[%d]=" % k, v

    @staticmethod
    def UVAnalyze():
        puva = PUVAnalyze()
        filePath = "d:/demo/userLog"
        rdd = SparkUtil.createRDD(True, "PVAnalyze", filePath)
        results = rdd \
            .filter(lambda x: x.split("\t")[2] <> 'null') \
            .map(puva.pageId2UserId)\
            .groupByKey()\
            .mapPartitions(puva.distinctUserId)\
            .sortBy(lambda x:x[1],False)\
            .saveAsTextFile("d:/demo/output/uvRet")

    @staticmethod
    def UVAnalyzeOptimization():
        puva = PUVAnalyze()
        filePath = "d:/demo/userLog"
        rdd = SparkUtil.createRDD(True, "PVAnalyze", filePath)
        results = rdd \
            .filter(lambda x: x.split("\t")[2] <> 'null') \
            .map(lambda x:(x.split("\t")[3],x.split("\t")[2])) \
            .distinct()\
            .countByKey()
        for k,v in results.items():
            print "pageId:%s UV:%s" % (k,v)

    @staticmethod
    def HotChannelAnalyze():
        puva = PUVAnalyze()
        filePath = "d:/demo/userLog"
        rdd = SparkUtil.createRDD(True, "PVAnalyze", filePath)
        filteredRDD = rdd.filter(lambda x: x.split("\t")[2] <> 'null')
        results =filteredRDD\
            .map(lambda x: (x.split("\t")[4],None))\
            .countByKey()

        sortResult = sorted(results.iteritems(),key=lambda x:x[1],reverse=True)
        for i in range(len(sortResult)-1,2,-1):sortResult.pop(i)
        hotChannels = [item[0] for item in sortResult]
        return (hotChannels,filteredRDD)

    @staticmethod
    def activeUserPerChannel():
        hotChannels,filteredRDD = PUVAnalyze.HotChannelAnalyze()
        #拿到sparkContext对象
        sc = filteredRDD.context
        hotChannelsBroadcast = sc.broadcast(hotChannels)
        filteredRDD\
            .filter(lambda x: x.split("\t")[4] in hotChannelsBroadcast.value)\
            .map(lambda x:(x.split("\t")[4],x.split("\t")[2]))\
            .groupByKey()\
            .flatMap(PUVAnalyze.getActiveUserPerChannel)\
            .foreach(PUVAnalyze.f)

    @staticmethod
    def activeUserPerChannelOptimization():
        puva = PUVAnalyze()
        hotChannels, filteredRDD = PUVAnalyze.HotChannelAnalyze()
        sc = filteredRDD.context
        hotChannelsBroadcast = sc.broadcast(hotChannels)
        filteredRDD \
            .filter(lambda x: x.split("\t")[4] in hotChannelsBroadcast.value) \
            .map(lambda x:(x.split("\t")[2],x.split("\t")[4]))\
            .groupByKey()\
            .flatMap(puva.getVistHotChannelNumPerUser)\
            .groupByKey()\
            .foreach(puva.getTop10ActivePerChannel)

if __name__ == "__main__":
#     print "inputPath:%s , outputPath:%s" %(sys.argv[1],sys.argv[2])
    PUVAnalyze.PVAnalyze(True,sys.argv[1],sys.argv[2])
    #有问题的思路实现出来的代码
    PUVAnalyze.UVAnalyze()
    PUVAnalyze.UVAnalyzeOptimization()
#     PUVAnalyze.HotChannelAnalyze()
#     PUVAnalyze.activeUserPerChannel()
#     PUVAnalyze.activeUserPerChannelOptimization()
    