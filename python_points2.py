# coding=utf-8
'''
# __new__() 与 __init__()的区别
#
'''


class A(object):
    def __init__(self, *args, **kwargs):
        print("init &&&&  %s" % self.__class__)

    def __new__(cls, *args, **kwargs):
        print ("new &&&&  %s" % cls)
        return object.__new__(cls, *args, **kwargs)


a = A()
'''
# 输出结果为：
# new &&&&  <class '__main__.A'>
# init &&&&  <class '__main__.A'>
#
# 如果把最后一行的return代码屏蔽掉，输出结果为：
# new &&&&<class '__main__.A'>
对于”new”和”init”可以概括为： 
    1.“new”方法在Python中是真正的构造方法（创建并返回实例），
    通过这个方法可以产生一个”cls”对应的实例对象，
    所以说”new”方法一定要有返回。 
    2.对于”init”方法，是一个初始化的方法，
    ”self”代表由类产生出来的实例对象，
    ”init”将对这个对象进行相应的初始化操作。
'''
# part 2
# 编码，二进制和解码
# ASCII 码，最早的
# GB2312 1980年收录了6763个汉字和682个字符
# GBK   是G2312的扩展
# GB18030  对嵌入式产品暂不做要求，手机，MP3一般只支持GB2312

# Unicode（统一码，万国码，单一码）是一种在计算机上适应的字符编码，其最少有16位（两个字节）来表示
# UTF-8 是对Unicode编码的压缩和优化
'''
以上编码格式，都是向下兼容的。
python2 解释器在架子啊.py文件的时候，会对内容进行编码（默认是ASCII）
python3 默认是utf-8，故一般不会出现中文乱码情况
'''

name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")
# 在python2.x中，input()其实输入的是一个变量，他会在内存中找是否有该变量。否则就会报错（name:xx is not defined）
information = '''
--------- info of %s----------
Name:%s
Age:%s
Job:%s
Salary:%s
''' % (name, name, age, job, salary)
information2 = '''
--------- info of {_name}----------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name = name, _age = age, _job = job, _salary = salary)
information3 = '''
--------- info of {0}----------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name, age, job, salary)
# 三者的输出是一样的
print (information)
print (information2)
print (information3)
