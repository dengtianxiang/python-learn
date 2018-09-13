#--coding:utf-8--

 
try:
    float('abc')
except Exception,e:
    print e
    
 
try:
    float(1.0)
except Exception,e:
    print e
finally:
    print 'Do not forget to close database.'
      
     
try:
    assert 1==0
except AssertionError, args:
    print 'One does equal zero silly',args
     
     
try:
    raise ZeroDivisionError
except ZeroDivisionError, args:
    print 'raise ZeroDivisionError'