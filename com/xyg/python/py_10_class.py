#coding=utf-8

class AddrBookEntry(object):
    myVersion = '1.0' #静态数据
    # 定义构造类
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        print 'Created instance for:', self.name
    # 定义方法
    def updatePhone(self, new_phone):
        self.phone = new_phone
        print 'Updated phone# for:', self.name    
    
# 创建实例    
john = AddrBookEntry('John', '123')
jane = AddrBookEntry('Jane', '456')

print john
print john.name, john.phone
jane.updatePhone(183)
print jane.name, jane.phone

 
print bool("1")
 
print 1/2
print 1.0/2.0
print 15//4
print 15.0//4.0
 
print divmod(15,6)
 

 
def func(args=[]):
    args.append(1)
    print args
     
func()
func()
func()