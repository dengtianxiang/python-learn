# --coding:utf-8--


# 元组
aTuple = ('robert', 77, 93, 'try')
print aTuple[1:3]
print aTuple[1]

t1 = (1)
t2 = (1,)
print type(t1),type(t2)

a = ("one","two")
print a[0]
b = ("just-one")
print b[0]
c = "just-one",
print c[0]
 
d = "just-one"
print d[0]


# 列表
aList = [1,2,3,'a string']
bList = [2,3,4,5]
aList.extend(bList)
for item in aList:
    print "aaaaaaaaaaaaa%s" %item
print aList[0]
print aList[2:]
print aList[:3]
aList[1] = 5
print aList
del aList[1]
aList.pop()
print aList

# 字典
aDict = {'host': 'earth'}
aDict['port'] = 80
print aDict
print aDict.keys()
print aDict.values()
print aDict['host']

# 遍历字典
for key in aDict:
    print key, aDict[key]

for key,value in aDict.items():
    print key,value

 
for key,value in aDict.iteritems():
    print key,value
    
    
    
aList = [1,2,3,2,3]
a = list(set(aList))
a.sort(reverse=True)
print a
