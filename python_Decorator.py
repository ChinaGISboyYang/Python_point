# # coding=utf-8
#
# # 修饰器代码实现
#
# #
#
# # -*- coding:gbk -*-
# '''示例6: 对参数数量不确定的函数进行装饰，
# 参数用(*args, **kwargs)，自动适应变参和命名参数'''
#
#
# def deco(func):
#     def _deco(*args, **kwargs):
#         print("before %s called." % func.__name__)
#         ret = func(*args, **kwargs)
#         print("  after %s called. result: %s" % (func.__name__, ret))
#         return ret
#
#     return _deco
#
#
# @deco
# def myfunc(a, b):
#     print(" myfunc(%s,%s) called." % (a, b))
#     return a + b
#
#
# @deco
# def myfunc2(a, b, c):
#     print(" myfunc2(%s,%s,%s) called." % (a, b, c))
#     return a + b + c
#
#
# myfunc(1, 2)
# myfunc(3, 4)
# myfunc2(1, 2, 3)
# myfunc2(3, 4, 5)

def fun(test):
    def choice():
        test()
        print('this is Alex')
    return choice
    
    
def fun_speak():
    print("I`m speaking")

def fun_eat():
    print('I`m eating')


Fun = 

