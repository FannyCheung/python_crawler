一、基本语法
#字符串拼接 .format() 占位符
for i in range(0,100):
    print ("item{0},{1}".format(i,"hello"))

#定义函数
def max(a,b):
    if a>b:
        return a;
    else:
        return b;

print'the max number is:',max(2,3),'good'

#oop 继承(类的定义)
class hello:
    def __init__(self,name):
        self._name = name
    def sayhello(self):
        print("hello {0}".format(self._name))
        
class hi(hello):  # 继承hello类
    def __init__(self,name):
        hello.__init__(self,name)
    def sayhi(self):
        print("hi {0}".format(self._name))
        
h = hello("every day")   #创建了一个hello实例
h.sayhello()

h1 = hi("Sunday")    
h1.sayhi()

#引入文件  访问
     首先在mylib.py里面定义一个类
class Hello:    def sayHello(self):        print("hello Sunday")
##法一
     在主文件learn.py中引入库
import mylibh = mylib.Hello()     #创建一个hello实例h.sayHello()            #访问到hello类里面的函数

##法二
     在主文件learn.py中直接引入类
from mylib import Helloh = Hello()      #创建一个hello实例h.sayHello()    #访问到hello类里面的函数


二、python语言Web开发框架  web2py


#创建web2py项目
#静态处理文件
#编写控制器

 
三、python 语法基础

放在Lib文件夹下，变成一个模块，下次使用直接import
#定义一个常量模块class _const(object):    class ConstError(TypeError):pass        def __setattr__(self,name,value):        if self.__dict__.has_key(name):            raise self.ConstError,"Can't rebing const(%s)"%name        self.__dict__[name] = value    def __delattr__(self,name):        if name in self.__dict__:            raise self.ConstError,"Can't unbind const(%s)"%name        raise NameError,name
import syssys.modules[__name__] = _const()


#类型：整数型（int），长整形（long），浮点型（float），布尔型（bool），复数型（complex）

#字符串
	单引号   str = 'It is a "dog" '
	双引号   str = "It's a dog"
	三引号   str=""" you
                    are
                    my
                    sun shine"""


#自然字符串(转义字符原样保留输出)
print r"hello \n Sunday"

#字符串重复输出
print "hello Sunday"*20

#子字符串运算方法：
##索引运算法[]，从0开始索引
##切片运算法[a:b]，第一位下标为0，从第a个下标到第b-1个下标

#数据类型 ： 列表[]、元组、集合、字典
##列表[]，从0开始，可修改
students["小明","小哈","小娟","小红"]
print students[0]

##元组(),只能读不能修改


##集合，交&，并|，差-，去除重复元素b=set(a)

##字典{}，关联数组
info={'name':'puppy','age':'5','sex':'male'}
print info['name']
#添加项目
info['music'] = 'music'print info['habbit']

#标识符，大小写敏感  ；关键字（保留字28种）

#对象\pickle腌制（将对象序列化，能持久性存储）

import pickle

#dumps(object) 将对象序列化lista = ["mingyue","jishi","you"]listb = pickle.dumps(lista)print listb

#loads(string) 将对象原样恢复，并且对象类型也恢复为原来的格式listc = pickle.loads(listb)print listc
#dump(object,file)，将对象存储到文件里面序列化group1 = ("bajiu","wen","qingtian")f1 = file('1.pk1','wb')pickle.dump(group1,f1,True)f1.close()
#load(object,file)  将dump（）存储在文件里面的数据恢复f2 = file('1.pk1','rb')t = pickle.load(f2)print tf2.close()

#行连接，\ 在行末作为行连接
print "我们都是\
好孩子"



四、python 控制流
break：停止执行——while\for循环、内层嵌套则跳出所在层
continue:跳出本次循环的执行，直接跳到下一次执行


五、python函数
形参、实参
全局变量、局部变量
    作用域
函数的使用和返回值
     多个返回值（元组）
def test(i,j):
    k = i*j
    return (i,j,k)
    
y,z,m = test(4,5)
print y

文档字符串

def d(i,j):
    '''This函数实现一个乘法运算。
    
    This函数会返回一个乘法运算的结果。'''
    k = i*j
    return k

#文档字符串的使用    
print d.__doc__
help(d)

六、python模块

1、模块：实现一类功能，函数功能的扩展          函数：一项/多项功能

2、导入模块
import mathmath.pi

3、标准库模块：python官方提供的自带的模块，和python安装时一起产生的；是指一类模块，不是特定的一种模块

4、sys模块：在标准库中与系统功能有关的这些模块
import sys

sys.version     #查看版本信息的方法
sys.executable      #当前运行的文件所在位置
sys.getwindowsversion()    #运行环境信息
sys.modules.keys()          #已导入模块的关键字


字节编译
1、.pyc ： 模块编译后产生的对应二进制文件
2、字节编译：把模块编译成二进制语言程序的过程
3、python是解释型语言，其字节编译这部分的功能由解释器完成
4、编译型语言是指软件中有一个独立的编译模块将程序编译

1、.pyc文件的生成
法一：#直接执行文件
import zipfile

法二：#在cmd下进入Lib文件夹执行编译
python -m compileall xmllib.py

2、.pyc文件的使用
a、加快了模块的运行速度
b、做反编译等高级功能
二进制文件阅读器（binary viewer）

from。。。import 详解

>>from sys import version  #  从模块sys中导入方法（属性）version
>>version

>> from sys import *    #一次性导入模块的所有功能（属性&方法）
>>executable

__name__属性
主模块：自己执行，调用其他模块。主模块的__name__属性的值是__main__

if __name__=="__main__":    print "it's main"else:    print "it's not main"

自定义模块
将python程序放在Lib目录下面就可以了
1、参数初始化/声明参数类型
2、模块外参数传递到模块内
---------------learn.py---------------
int iint jdef add(i,j):    k = i+j    return kk = add(i,j)print k
-----------command line------------
>>import learn
>>learn.add(1,5)

dir()函数
1、查看指定模块的功能列表，宏观上知道模块中提供的功能
>>import sys
>>dir(sys)

2、使用功能列表中的属性、方法  (得出文档说明信息)
>>sys.__doc__

3、
>>d =[]
>>dir(d)














