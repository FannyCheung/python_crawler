һ�������﷨
#�ַ���ƴ�� .format() ռλ��
for i in range(0,100):
    print ("item{0},{1}".format(i,"hello"))

#���庯��
def max(a,b):
    if a>b:
        return a;
    else:
        return b;

print'the max number is:',max(2,3),'good'

#oop �̳�(��Ķ���)
class hello:
    def __init__(self,name):
        self._name = name
    def sayhello(self):
        print("hello {0}".format(self._name))
        
class hi(hello):  # �̳�hello��
    def __init__(self,name):
        hello.__init__(self,name)
    def sayhi(self):
        print("hi {0}".format(self._name))
        
h = hello("every day")   #������һ��helloʵ��
h.sayhello()

h1 = hi("Sunday")    
h1.sayhi()

#�����ļ�  ����
     ������mylib.py���涨��һ����
class Hello:    def sayHello(self):        print("hello Sunday")
##��һ
     �����ļ�learn.py�������
import mylibh = mylib.Hello()     #����һ��helloʵ��h.sayHello()            #���ʵ�hello������ĺ���

##����
     �����ļ�learn.py��ֱ��������
from mylib import Helloh = Hello()      #����һ��helloʵ��h.sayHello()    #���ʵ�hello������ĺ���


����python����Web�������  web2py


#����web2py��Ŀ
#��̬�����ļ�
#��д������

 
����python �﷨����

����Lib�ļ����£����һ��ģ�飬�´�ʹ��ֱ��import
#����һ������ģ��class _const(object):    class ConstError(TypeError):pass        def __setattr__(self,name,value):        if self.__dict__.has_key(name):            raise self.ConstError,"Can't rebing const(%s)"%name        self.__dict__[name] = value    def __delattr__(self,name):        if name in self.__dict__:            raise self.ConstError,"Can't unbind const(%s)"%name        raise NameError,name
import syssys.modules[__name__] = _const()


#���ͣ������ͣ�int���������Σ�long���������ͣ�float���������ͣ�bool���������ͣ�complex��

#�ַ���
	������   str = 'It is a "dog" '
	˫����   str = "It's a dog"
	������   str=""" you
                    are
                    my
                    sun shine"""


#��Ȼ�ַ���(ת���ַ�ԭ���������)
print r"hello \n Sunday"

#�ַ����ظ����
print "hello Sunday"*20

#���ַ������㷽����
##�������㷨[]����0��ʼ����
##��Ƭ���㷨[a:b]����һλ�±�Ϊ0���ӵ�a���±굽��b-1���±�

#�������� �� �б�[]��Ԫ�顢���ϡ��ֵ�
##�б�[]����0��ʼ�����޸�
students["С��","С��","С��","С��"]
print students[0]

##Ԫ��(),ֻ�ܶ������޸�


##���ϣ���&����|����-��ȥ���ظ�Ԫ��b=set(a)

##�ֵ�{}����������
info={'name':'puppy','age':'5','sex':'male'}
print info['name']
#�����Ŀ
info['music'] = 'music'print info['habbit']

#��ʶ������Сд����  ���ؼ��֣�������28�֣�

#����\pickle���ƣ����������л����ܳ־��Դ洢��

import pickle

#dumps(object) ���������л�lista = ["mingyue","jishi","you"]listb = pickle.dumps(lista)print listb

#loads(string) ������ԭ���ָ������Ҷ�������Ҳ�ָ�Ϊԭ���ĸ�ʽlistc = pickle.loads(listb)print listc
#dump(object,file)��������洢���ļ��������л�group1 = ("bajiu","wen","qingtian")f1 = file('1.pk1','wb')pickle.dump(group1,f1,True)f1.close()
#load(object,file)  ��dump�����洢���ļ���������ݻָ�f2 = file('1.pk1','rb')t = pickle.load(f2)print tf2.close()

#�����ӣ�\ ����ĩ��Ϊ������
print "���Ƕ���\
�ú���"



�ġ�python ������
break��ִֹͣ�С���while\forѭ�����ڲ�Ƕ�����������ڲ�
continue:��������ѭ����ִ�У�ֱ��������һ��ִ��


�塢python����
�βΡ�ʵ��
ȫ�ֱ������ֲ�����
    ������
������ʹ�úͷ���ֵ
     �������ֵ��Ԫ�飩
def test(i,j):
    k = i*j
    return (i,j,k)
    
y,z,m = test(4,5)
print y

�ĵ��ַ���

def d(i,j):
    '''This����ʵ��һ���˷����㡣
    
    This�����᷵��һ���˷�����Ľ����'''
    k = i*j
    return k

#�ĵ��ַ�����ʹ��    
print d.__doc__
help(d)

����pythonģ��

1��ģ�飺ʵ��һ�๦�ܣ��������ܵ���չ          ������һ��/�����

2������ģ��
import mathmath.pi

3����׼��ģ�飺python�ٷ��ṩ���Դ���ģ�飬��python��װʱһ������ģ���ָһ��ģ�飬�����ض���һ��ģ��

4��sysģ�飺�ڱ�׼������ϵͳ�����йص���Щģ��
import sys

sys.version     #�鿴�汾��Ϣ�ķ���
sys.executable      #��ǰ���е��ļ�����λ��
sys.getwindowsversion()    #���л�����Ϣ
sys.modules.keys()          #�ѵ���ģ��Ĺؼ���


�ֽڱ���
1��.pyc �� ģ����������Ķ�Ӧ�������ļ�
2���ֽڱ��룺��ģ�����ɶ��������Գ���Ĺ���
3��python�ǽ��������ԣ����ֽڱ����ⲿ�ֵĹ����ɽ��������
4��������������ָ�������һ�������ı���ģ�齫�������

1��.pyc�ļ�������
��һ��#ֱ��ִ���ļ�
import zipfile

������#��cmd�½���Lib�ļ���ִ�б���
python -m compileall xmllib.py

2��.pyc�ļ���ʹ��
a���ӿ���ģ��������ٶ�
b����������ȸ߼�����
�������ļ��Ķ�����binary viewer��

from������import ���

>>from sys import version  #  ��ģ��sys�е��뷽�������ԣ�version
>>version

>> from sys import *    #һ���Ե���ģ������й��ܣ�����&������
>>executable

__name__����
��ģ�飺�Լ�ִ�У���������ģ�顣��ģ���__name__���Ե�ֵ��__main__

if __name__=="__main__":    print "it's main"else:    print "it's not main"

�Զ���ģ��
��python�������LibĿ¼����Ϳ�����
1��������ʼ��/������������
2��ģ����������ݵ�ģ����
---------------learn.py---------------
int iint jdef add(i,j):    k = i+j    return kk = add(i,j)print k
-----------command line------------
>>import learn
>>learn.add(1,5)

dir()����
1���鿴ָ��ģ��Ĺ����б������֪��ģ�����ṩ�Ĺ���
>>import sys
>>dir(sys)

2��ʹ�ù����б��е����ԡ�����  (�ó��ĵ�˵����Ϣ)
>>sys.__doc__

3��
>>d =[]
>>dir(d)














