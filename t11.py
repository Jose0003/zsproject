# import inspect



# def typecheck(cls):
#
#     def wrapper(*args,**kwargs):
#         sig = inspect.signature(cls)
#         params = sig.parameters
#         for name,param in params.items():
#             #print(name,param.name,param.annotation,param.kind,param.default)
#             if param.annotation != param.empty:
#
#
#         return cls(*args,**kwargs)
#     return wrapper






# @typecheck   #A = typecheck(A)(name,age)
# class A:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
        # params = ((name,str),(age,int))
        # if not self.checkdata(params):
        #     raise TypeError



    # def checkdata(self,params):
    #     for k,v in params:
    #         if not isinstance(k,v):
    #             print(k,v)
    #             raise False
    #     return True

# a = A('asd',123)


# import  tracemalloc
#
# tracemalloc.start()
#
# d = 1
# s = 2
#
# snapshot = tracemalloc.take_snapshot()
# stats = snapshot.statistics('filename')
#
# for s in stats:
#     print(s)


# class A:
#     __slots__ = 'x','y'
#     def __init__(self):
#         self.x = 1
#         self.y = 2
#
# print(A.__dict__)
#
#
# class B(list):
#     def __init__(self,tup):
#         self[:] = tup
#         print(self[:],id(self[:]),id(tup))
#         self = tup
#         print(self,id(self),id(tup))
#
#
# b = B((1,2,3,4))



# class A:
#     def __init__(self, x, next= None):
#         self.x = x
#         self.next = next
#
#     def __call__(self, *args, **kwargs):
#         print('{}+{}'.format(args,self.x))
#         return self.x
#
#     def __iter__(self):
#         return 1
#
#
# a = A(5)
#
#
# for i in a:
#     print(i)





# class B:
#     def __init__(self):
#         self.d = []
#         self.head = None
#         self.tail = None
#
#     def append(self,val):
#         node = A(val)
#         current = self.tail
#         if current is None:
#             self.head = node
#         self.d.append(node)
#         self.tail = node
import inspect


#
#
#
#
#
# #@check_annotation   # A = check(A) (name,age)
# class A:
#     def __init__(self,name:str,age:int):
#         params = ((name,str),(age,int))
#         self.name = name
#         self.age = age
#         if not self.check_annotation(params):
#             raise TypeError('annotation no')
#
#     def check_annotation(self,params):
#         for k,v in params:
#             if isinstance(k,v):
#                 return True
#             else:
#                 return False
#
# a = A('1',1)

# class Check:
#     def __init__(self,cls):
#         self.cls = cls
#         sig = inspect.signature(cls)
#         params = sig.parameters
#         for k, v in params.items():
#             print(k,v.annotation)
#             #print(v.annotation)
#         if v.annotation != v.empty:
#             if not isinstance(k,v.annotation):
#                 raise TypeError('no~~~~~~~~~~~~~~')
#
#     def __call__(self, *args, **kwargs):
#         return self.cls(*args, **kwargs)
#


# def check3(cls):
#     def wrapper(*args,**kwargs):
#         sig = inspect.signature(cls)
#         params = sig.parameters
#         for k,v in params.items():
#             print(k,v.annotation)
#
#             # if isinstance(k,v.annotation):
#             #     print('good~~~~~~~~~~')
#             # else:
#             #     print('no~~~~~~~~~~~')
#         return cls(*args,**kwargs)
#     return wrapper
# #@Check
#
# @check3
# class C:   #C = Check(C)
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
# c = C('asd',1)


# def foo(x:str):
#     sig = inspect.signature(foo)
#     params = sig.parameters
#     for k,v in params.items():
#         print(k)
#         if type(k) == v.annotation:
#             print('good')
#         else:
#             print('no')
#
#
#
#
# foo(1)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#
# list1 = Node(3)
#
# class Linklist:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
# linklist = Linklist()
#
#
# def is_empty(self):
#     return self.head is None
#
# print(is_empty(linklist))



# class Property:
#     def __init__(self):
#
from functools import partial
# class Property:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         return self.fn
#
#
#
# class A:
#     def __init__(self):
#         pass
#
#
#     #@Property #foo = Property(foo)
#     #@property  #foo = property(foo)(self)
#     @Property
#     def foo(x,y):
#         print(x,y)
#
#
#
# a = A()
# a.foo

class MyProperty:
    def __init__(self, fget, fset):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)


class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def __repr__(self):
        return ''.format(self._x)
    x = MyProperty(getX, setX)
from os import path
from pathlib import Path
# if __name__ == '__main__':
# #     print('111111111111111111111111')
# #     print(__name__)
# # print(__name__)
# # import pathlib
# # print(pathlib.Path)
# # print(id(pathlib.Path))

