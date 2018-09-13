#--coding:utf-8--

# 函数参数传递

def mytest(num):
    return num * 2

# 不光可以传递变量,还可以传递函数
def convert(func, seq):
    'convert sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = [123, 45.67, -6.2e8, 99999999L]
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)
print convert(mytest, myseq)


# 参数的默认赋值
def taxMe(cost, rate=0.0825):
    return cost + cost * rate
  
print taxMe(100)
print taxMe(100, 0.05)
  
  
def taxMe2(cost, rate=0.0825, *theRest):
    for eachRest in theRest:
        print 'another arg:' , eachRest
        cost += eachRest
    return cost + cost * rate
 
print taxMe2(100, 0.05, 100, 200,300,400)
 
 
def taxMe3(cost, rate=0.0825, **theRest):
    for eachRest in theRest.keys():
        print 'another arg:' , eachRest
        cost += theRest[eachRest]
    return cost + cost * rate
 
print taxMe3(100, rate = 0.05, electric=100, water=200, gas=300)


def taxMe4(cost, rate=0.0825, *theRest, **theRest2):
    for eachRest in theRest2.keys():
        print 'another arg:' , eachRest
        cost += theRest2[eachRest]
    return cost + cost * rate

print taxMe4(100, 0.05, 50,60, electric=100 ,water=200,gas=30)