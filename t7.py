



# def logger1(fn):
#     def inner(*args,**kwargs):
#         print('begin')
#         fn(*args,**kwargs)
#         print('after')
#         #return ret
#     return inner
#
# @logger1
# def foo1(x, y):
#     print(x+y)
# #logger1(foo1)(1,2)
# foo1(3,4)
# print(foo1.__name__)
# '''
# import datetime
# import time
# from functools import update_wrapper
#
#
# class Logger3:
#     '''this is logger3'''
#     def __init__(self,fn):
#         self.fn = fn
#         update_wrapper(self,fn)
#
#     def __call__(self, *args):
#         start = datetime.datetime.now()
#         self.fn(*args)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print(delta)
#
#
#
#
# @Logger3       #foo3 = Logger3(foo3)  类似于 a = A(add)
# def foo3(x, y):
#   #  '''this foo3'''
#     time.sleep(1)
#     print(x+y)
#
#
#
# foo3(1,2)
# print(foo3.__doc__)
# print(foo3.__name__)
#
# '''
# import datetime
# import time
# from functools import wraps,update_wrapper
#
#
# def logger3(duration=3):
#     def _logger3(fn):
#         @wraps(fn)
#         def inner(*args,**kwargs):
#             start = datetime.datetime.now()
#             ret = fn(*args,**kwargs)
#             delta = (datetime.datetime.now() - start).total_seconds()
#             if delta > duration:
#                 print(fn.__name__,'{:.4f}'.format(delta) )
#             else:
#                 print('good')
#             return ret
#         return inner
#     return _logger3
#
#
# @logger3(0.1)
# def add3(x,y):
#     time.sleep(1)
#     return x + y
#
#
#
#
# class Timeit:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __enter__(self):
#         self.start = datetime.datetime.now()
#         return self   #1,返回值是self 说明返回了实例给f,f(3,4)需要call方法
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.delta = (datetime.datetime.now() - self.start).total_seconds()
#         print(self.delta,'111111111111111111')
#
#     def __call__(self, *args, **kwargs):
#         return self.fn(*args, **kwargs)  #2,call方法返回函数self存的函数self.fn
#
# #self = Timeit(add3)
# with Timeit(add3) as f:  #3,f拿到函数,直接调用
#     f(3,4)

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.d = []
#
#     def addcart(self):
#         self.d.append((self.x,self.y))
    # def show(self):
    #     print(self.x,self.y)

# a = Point(3,4)
#
# print(getattr(a,'x'))
# print(setattr(a,'x',100))
# print(setattr(a,'z',333))
# print(a.__dict__)
# print(hasattr(a,'q'))
# if not hasattr(a,'q'):
#     setattr(a,'q',999)
#
# print(a.__dict__)
#
# print(setattr(Point,'xyz',100))
# print(Point.__dict__)
#
# if not hasattr(Point,'show'):
#     setattr(Point,'show',lambda self:print(self.x,self.y))
#
# print(Point.__dict__)
# p = Point(3,4)
# p.show()
# Point.show(Point(1,2))
#
# if not hasattr(p,'showy'):
#     setattr(p,'showy',lambda self: print(self.x,self.y))
#
#
# p.showy(p)
# print(p.show)
# print(p.showy)
#
# setattr(Point,'__add__',lambda self,other: Point(self.x + other.x,self.y + other.y))
# setattr(Point,'__repr__',lambda self:'{},{}'.format(self.x,self.y))
# setattr(Point,'addcart',lambda self:self.d.append(self.x,self.y))

# a = Point(1,2)
# b = Point(3,4)
# c = Point(1,3)
# print(a + b + c)


# class A:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#
#         return A(self.x + other.x,self.y + other.y)
#
#     def __repr__(self):
#         return '{},{}'.format(self.x,self.y)


# a = A(1,2)
# b = A(1,2)
# c = A(0,2)
#
# print(a + b + c)
# '''
# def asd():
#     print('666')
#
#
#
# class A:
#     def __init__(self):
#
#         self.x = lambda :print('1')
#         self.y = lambda :print('2')
#         self.z = lambda :print('3')
#         self.asd = asd
#
#
#     def reg(self,name,fn):
#         setattr(self,name,fn)
#
#
#     # @staticmethod
#     # def x1():
#     #     print('1')
#     #
#     # @staticmethod
#     # def x2():
#     #     print('2')
#     #
#     # @staticmethod
#     # def x3():
#     #     print('3')
#
#     def foo1(self):
#         while True:
#             n = input('>>>>>>')
#             if n == 'quit':
#                 return
#             if hasattr(self, n):
#                 getattr(self, n)()
#             else:
#                 print('no no no')
#
#
# a = A()
# #
#
# a.foo1()
# a.reg('ls',lambda :print('666'))
#
#
# '''

# class A:
#     n = 3
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.c = 3
#
#     def __getattr__(self, item):
#         print(item)
#         self.__dict__[item] = 1000
#         return self.__dict__[item]
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delattr__(self, item):
#         del self.__dict__[item]
#
# a = A()
# print(a.axxx)
# print(a.__dict__)
# print(a.xasda)
# print(a.__dict__)

# print(a.a)
# print(a.b)
# print(a.c)
# print(a.__dict__)
# print(A.n)
# print(A().a)
# print(a.n)
# del a.n
#print(A.n)

