# class Property:
#     def __init__(self, fget, fset=None):
#         self.fget = fget
#         self.fset = fset
#
#     def __get__(self, instance, owner):
#         return self.fget(instance)
#
#     def __set__(self, instance, value):
#         if self.fset:
#             self.fset(instance,value)
#
#     def setter(self,fn):
#         self.fset = fn
#         return self
#
#
# class A:
#
#     def __init__(self,a):
#         self._a = a
#
#     @Property       #a = Property(a)
#     def a(self):
#         return self._a
#
#     @a.setter       #a = a.setter(a)
#     def a(self,n):
#         self._a = n
#
#
# x = A(3)
# print(x.a)
# x.a = 100
# print(x.a)

# class A:
#     x = 123
#     def __init__(self,name):
#         self._name = name
#         self.__age = 29
#         self.weight = 20
#
#     def __dir__(self):
#         return [self._name]
#
#
#
#
#
# a = A('asd')
# print(dir(a))

# class A:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __repr__(self):
#         return '{},{}'.format(self.a,self.b)
#
#     def __hash__(self):
#         return hash((self.a,self.b))
#
#     def __eq__(self, other):
#         return self.a == other.a,self.b == other.b
#
#
# a = A(1,2)
# b = A(1,3)
# print(a)
# print(hash(a),hash(b))
# print(a == b)

# class A:
#     def __init__(self,name,age = 18):
#         self.name = name
#         self.age = age
#
#     def __sub__(self, other):
#         return self.age - other.age
#
#     def __isub__(self, other):
#         self.age -= other.age
#         return self.age
#
#
# a = A('a',28)
# b = A('b',29)
# # print(a.age)
# print(a - b)
# a -= b
# print(a)


# class A(dict):
#     # def __init__(self,a):
#     #     self.a = a
#     def __missing__(self, key):
#         print(key)
#         return 0
#
# a = A()
# print(a['s'])

# class Cart:
#     def __init__(self):
#         self.d = [1,2,3]
#
#     def appe(self,good):
#         self.d.append(good)
#
#     def __getitem__(self, item):
#         return self.d[item]
#
#     def __setitem__(self, key, value):
#         self.d[key] = value
#
#     def __add__(self, other):
#         self.d.append(other)
#         return self
#
#     def __repr__(self):
#         return '{}'.format(self.d)
#
#     def __call__(self, *args, **kwargs):
#         for i in args:
#             self.d.append(i)
# a = Cart()
# print(a[1])
# a[2] = 10000
#
# print(a(1,2,3))
# print(a)

# class Adder:
#     def __call__(self, *args):
#         ret = 0
#         for x in args:
#             ret += x
#         self.ret = ret
#         return ret
# adder = Adder()
# print(adder(4, 5, 6))
# print(adder.ret)


# class A:
#     def __call__(self, *args, **kwargs):
#         ret = 0
#         for i in args:
#             ret += i
#         self.d = ret
#         return self.d
#
# a = A()
# print(a(1,2,3,4))
# print(a.__dict__)

# class A:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#         self.d = []
#
#     def __call__(self, index):
#         if len(self.d) == 0:
#             for i in range(index):
#                 self.a, self.b = self.b, self.a + self.b
#                 self.d.append(self.a)
#                 self.seek = len(self.d)
#             return self.a
#         if self.seek >= index:
#             return self.d[index - 1]
#         elif self.seek < index:
#             for i in range(self.seek,index):
#                 self.a, self.b = self.b, self.a + self.b
#                 self.d.append(self.a)
#                 self.seek = len(self.d)
#             return self.a
#
#
#
# #
# a = A()
# print(a(5))
# print(a.d)
# print(a(10))
# print(a.d)
# print(a(5))
# print(a.d)
# # print(a(10))
# # print(a.d)
# print(a(20))
# print(a.d)
# print(a(10))
# print(a.d)
# # print(a(5))
# # print(a.d)
# # print(a(6))
# # print(a.d)
#

# class A:
#     def __init__(self):
#         self.a = [1,2,3]
#
#     def __getitem__(self, item):
#         # if item in self.a:
#         return self.a[item]
#         # else:
#         #     return 100
#
#     # def __contains__(self, item):
#     #     return self.a[item]
#
#     def __setitem__(self, key, value):
#         if key in self.a:
#             self.a[key] = value
#         else:
#             self.a.append(value)
#
#     def __missing__(self, key):
#         return 'no key{}'.format(self.a[key])
#
#
#
# a = A()
# print(a[0])
#
#
# print(a[1])
# print(a[9])
# print(a.a)

# class A(dict):
#     def __init__(self):
#         self.d = {'a':1,'b':2}
#
#     def __missing__(self, key):
#         return 'no key {}'.format(self.d[key])
#
# a = A()
# print(a['c'])
# import datetime
# import time
#
# def foo1(x,y):
#     time.sleep(1)
#     return x+y
#
#
#
#
#
# class A:
#     def __init__(self,fn):
#         self.fn = fn
#
    # def __enter__(self):
    #     print('begin')
    #     self.start = datetime.datetime.now()
    #     return self.fn
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.delta = (datetime.datetime.now() - self.start).total_seconds()
    #     print(self.delta)
    #     print('over')
#
#
#
# with A(foo1) as f:
#     f(3,4)
#
# from functools import update_wrapper
# import time
# import datetime
#
# class TimeDate:
#     '''TimeDate'''
#     def __init__(self,fn):
#         self.fn = fn
#         update_wrapper(self,fn)
#
#     # def __enter__(self):
#     #     print('begin')
#     #     self.start = datetime.datetime.now()
#     #     return self.fn
#     #
#     # def __exit__(self, exc_type, exc_val, exc_tb):
#     #     self.delta = (datetime.datetime.now() - self.start).total_seconds()
#     #     print(self.delta)
#     #     print('over')
#
#     def __call__(self, *args, **kwargs):
#         self.start = datetime.datetime.now()
#         self.fn(*args,**kwargs)
#         self.delta = (datetime.datetime.now() - self.start).total_seconds()
#         print(self.delta)
#
#
# @TimeDate     # foo1 = Time(foo1)(x,y)
# def foo1(x, y):
#     '''foo1'''
#     time.sleep(1)
#     print(x+y)
#     return x + y
#
#
# foo1(3, 4)
# print(foo1.__doc__)
# print(foo1.__name__)


# def foo3(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         print('go')
#         ret = fn(*args,**kwargs)
#         print('over')
#         return ret
#     return wrapper

# class Foo3:
#     '''foo3'''
#     def __init__(self,fn):
#         self.fn = fn
#         update_wrapper(self,fn)
#     def __call__(self, *args, **kwargs):
#         print('go')
#         self.fn(*args,**kwargs)
#         print('over')
#
#
#
# @Foo3  # foo1 = Foo3(foo1)(x,y)
# def foo1(x, y):
#     '''foo1'''
#     print(x+y)
#
# foo1(3,4)
# print(foo1.__doc__)
# print(foo1.__name__)


# class A:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __enter__(self):
#         print('begin')
#         return self.fn
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('over')
#
#
# with A(foo1) as f:
#     f(3, 4)
#from  functools import  wraps,update_wrapper
# def ls1():
#     print('ls1123123')
#
#
# class A:
#     def __init__(self):
#         pass
#
#     def reg(self, name, fn):
#         setattr(self, name, fn)
#
#     def run(self):
#         while True:
#             x = input('>>>>')
#             if x == 'quit':
#                 break
#             getattr(self, x, lambda: print('no'))
#
#
# a = A()
# a.reg('ls1', ls1)
# print(a.run())

# def foo1():
#     print('1')
#
#
# class A:
#     def __init__(self):
#         pass
#
#     def reg(self,name,fn):
#         setattr(self,name,fn)
#
#     def run(self):
#         while True:
#             x = input('>>>')
#             if x == 'quit':
#                 break
#             getattr(self, x, lambda: print('no'))()
#
#
# a = A()
# a.reg('ls',lambda :print('ls'))
# a.run()

# class A:
    # d = {}
    # def __init__(self):
        # self.x = 1
        # self.y = 2
        # self.n = [1,2,3,4]
        # pass


    # def __getattr__(self, item):
        # if item not in self.__dict__.keys():
        #     self.d[item] = 999
        # return self.d[item]
        # return 'missing {}'.format(item)
        # return self.d[item]
        # return 999

    # def __setattr__(self, key, value):
    #     self.d[key] = value
        # print('setattr {}={}'.format(key,value))
    # def __getattribute__(self, item):
        # self.__dict__[item] = 999
        # return 999

    # def __getitem__(self, item):
    #     return self.n[item]
    #
    # def __setitem__(self, key, value):
    #     self.n[key] = value


# a =A()
# print(a.x)
# print(a.x)
# print(a.__class__,dir(a.__class__))
# print(a.__class__.d)
# print(a.__dict__)
# print(a.__dict__)
# print(a.d)
# print(a[3])
# print(a.z)

# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A init')
#
#     def __get__(self, instance, owner):
#         return self
#         # print('{} {} {}'.format(self, instance, owner))
#
#     def __set__(self, instance, value):
#         self.data = value
#
#
# class B:
#     x = A()
#     y = A()
#
#     def __init__(self):
#         self.x = 'b.x'
#         self.y = '123'
#         print('B init')
#
# # print(B.x)
# # print(B.x.a1)
# # b = B()
# # # print(B.x.a1)
# # print(b.x.__dict__)
# # print(b.y.__dict__)
# # # print(B.x.a1)
# # # print(b.x)
# # b.x = 500
# # print(b.x.__dict__)
# # print(b.x.data)
#
# print(B.x.a1)
#
# b = B()
# print(b.__dict__)
# print(b.x.data)
# print(b.y.data)
# from functools import partial
# class S:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         return self.fn
#
# class C:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         return partial(self.fn, owner)
#
#
#
#
# class B:
#     @C    #foo2 = C(foo2)(cls,x)
#     def foo2(cls, x):
#         print(cls, x)
#
#
#     @S    #foo1 = S(foo1)(x,y)
#     def foo1(x, y):
#         print(x, y)


# b = B()
# print(b.foo1(1, 2))
# print(b.foo2(3))

# class A:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         return self.fn
#
#     def __set__(self, instance, value):
#         self.date = value
#
#
# class B:
#     # x = A()
#     # y = A()
#
#     def __init__(self):
#         self.x = 1
#
#     @A  # foo1 = A(foo1)(self)
#     def foo1(self,x,y):
#         print('333',x,y,self)
#
# b =B()
# print(b.foo1(1,2,3))
# print(b.__dict__)
# import inspect
#
# # class B:
# #     def __init__(self):
# #         pass
# #
# #     def __get__(self, instance, owner):
# #         return self
# #
# #     def __set__(self, instance, value):
# #         self.data = value
# #
# #
# # class Person:
# #     # name = B()
# #     # age = B()
# #
# #     def __init__(self, name: str, age: int):
# #         self.name = name
# #         self.age = age
# #         params = ((self.name, str), (self.age, int))
# #         for k, v in params:
# #             if not isinstance(k, v):
# #                 raise TypeError('type no')
# #         print('123')
# #
# #
# # a = Person('a', 3)
#
# def checkdata(fn):
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters
#         for k,v in params.items():
#             if not isinstance(k,v.annotation):
#                 raise TypeError('nonono')
#
#         return fn(*args, **kwargs)
#     return wrapper
#
#
#
# @checkdata  #Person = checkdata(Person)(name,age)
# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#
# a = Person('a', 3)
# import inspect
#
#
# def foo1(fn):
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters
#         print(params)
#         values = [*params.values()]
#         for i, p in enumerate(args):
#             if values[i].annotation is not inspect._empty \
#                     and not isinstance(p, values[i].annotation):
#                 raise TypeError('111111111')
#
#         for k, v in kwargs.items():
#             print(v)
#             if params[k].annotation is not inspect._empty \
#                     and not isinstance(v, params[k].annotation):
#                 raise TypeError('22222222')
#
#         return fn(*args, **kwargs)
#     return wrapper
#
#
# @foo1
# class A:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#
# a = A(name='12', age=11)
# b = A('12', 1)


# import inspect
# def check(fn):
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
        # print(sig)
        # params = sig.parameters

        # for k, v in params.items():
        #     print(k,v.annotation)
        # print(params)
        # for c in args:
        #     # print(c)
        #     for k, v in params.items():
        #         if v.annotation is not inspect._empty and not isinstance(c,v.annotation):
        #             raise TypeError('1111')
    #     for p in kwargs.values():
    #         print(p)
    #         for j in params.values():
    #             if j.annotation is not inspect._empty and not isinstance(p,j.annotation):
    #                 raise TypeError('2222')
    #     return fn(*args, **kwargs)
    # return wrapper
# import inspect
#
#
# def check(fn):
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters
#         values = [* params.values()]
#
#         for i, j in enumerate(args):
#             if values[i].annotation is not \
#                     inspect._empty and not \
#                     isinstance(j,values[i].annotation):
#                 print('!=')
#         for c, s in kwargs.items():
#             if params[c].annotation is not \
#                     inspect._empty and not \
#                     isinstance(s, params[c].annotation):
#                 print('666')
#
#         return fn(*args, **kwargs)
#     return wrapper
#
#
#
# @check
# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#
# a = Person(name='asd', age=1)
# b = Person('asd',1)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import inspect
#
# class TypeCheck:
#
#     def __init__(self, name, typ):
#         self.name = name
#         self.typ = typ
#
#     def __get__(self, instance, owner):
#         if instance:
#             return instance.__dict__[self.name]
#         else:
#             return self
#
#     def __set_name__(self, owner, name):
#         pass
#
#     def __set__(self, instance, value):
#         if instance:
#             if isinstance(value,self.typ):
#                 instance.__dict__[self.name] = value
#                 print('===')
#             else:
#                 raise TypeError('6666')
#
# def foo1(cls):
#     sig = inspect.signature(cls)
#     params = sig.parameters
#     for name, param in params.items():
#         print(param.annotation)
#         setattr(cls,name,TypeCheck(name, param.annotation))
#     return cls
#
# @foo1
# class Person:
#
#     # name = TypeCheck('name', str)
#     # age = TypeCheck('age', int)
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#
# a = Person('123', 1)
# b = Person('a',12)
# print(a.name)
# print(a.age)
# print(a.__dict__)
# print(b.name)
# print(b.age)
# print(b.__dict__)
# import t11
# from  pathlib import Path
# p = Path(__file__)
# print(p)
# print(p.with_name('zs'))
#
# import sys
# print(sys.modules)



# import t10
# print(t10.__file__)
# print(t10)
# print(type(t10))
# print(dir(t10))
# print(t10.__name__)
