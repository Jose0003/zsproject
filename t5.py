"""
class A:
    def __init__(self):
        self.d = []

    def __call__(self, *args, **kwargs):
        a = 0
        b = 1
        for i in args:
            x = i
        if x < len(self.d):
            return self.d[x-1]
        else:
            self.d.clear()
        for n in range(x):
            a,b = b,a+b
            self.d.append(a)

        return a,self.d

a = A()
b = A()

print(a(35))
print(a(6))
print(a(9))
print(a(36))
print(a(12))
print(a(6))

"""

"""
from functools import wraps,update_wrapper
import time
import datetime

def fn(x):
    @wraps(fn)
    def inner(*args):
        da1 = datetime.datetime.now()
        ret = x(*args)
        dalt = (datetime.datetime.now() - da1).total_seconds()
        print(dalt)
        return ret
    return inner


@fn  #foo = fn(foo)
def foo(x,y):
    time.sleep(3)
    return x + y

foo(3,4)


class A:
    def __init__(self,x):
        self.a = None
        self.x = x

    def __enter__(self):
        self.a = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        dalt = datetime.datetime.now() - self.a
        return dalt

def foo(x,y):
    time.sleep(3)
    return x + y
a = A()

with A(foo) as t:


"""

#
# import time
# import datetime
# from functools import wraps
#
# """"""
# class Timeit:
#     """class"""
#     def __init__(self,fn):
#         self.fn = fn
#         self.__doc__ = fn.__doc__
#
#     def __call__(self, *args, **kwargs):
#         start = datetime.datetime.now()
#         ret = self.fn(*args,**kwargs)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print(delta)
#         return ret
#
# @Timeit
# def add3(x,y):
#     """add3"""
#     time.sleep(1)
#     return x + y
#
# print(add3(3,4))
# print(add3.__doc__)


#
# class A:
#     def __init__(self):
#         self.d = dict()
#
#     def regiter(self,x,y):
#         setattr(self,x,y)
#
#     def d1(self,x):
#         while True:
#
#
#     def foo1(self):
#         print('1')
#
#     def foo2(self):
#         print('2')
#
#     def foo3(self):
#         print('3')
#
#
# a = A()


"""
class A:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.d = []


    def __getitem__(self, index):
        if index == 0:
            return 0
        if index > len(self.d):
            for x in range(len(self.d), index):
                self.a, self.b = self.b, self.a+self.b
                self.d.append(self.a)
                #print('++++++++++++++++')
            return self.a
        else:
            return self.d[index-1]
    def __repr__(self):
        return '{} {}'.format(__class__.__name__,self.d)

    def __call__(self, index):
        return self[index]



a = A()
print(a(10))
print(a[10])
print(a(15))
print(a(16))
print(a[17])
print(a)

"""
