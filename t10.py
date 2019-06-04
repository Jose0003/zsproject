# class A:
#     def __init__(self,x):
#         self.x = x
#
#     def __add__(self, other):
#         if type(self) != type(other):
#             return self.x + int(other)
#         return A(self.x  + other.x)
#
#     def __iadd__(self, other):
#         A(self.x  + other.x)
#         return self
#
#     def __radd__(self, other):
#         if type(self) != type(other):
#             if isinstance(other, int):
#                 return self.x + other
#         return A(self.x + other.x)
#
#     def __repr__(self):
#         return '{}'.format(self.x)
#
#
# a = A(2)
# b = A(3)
# print(a + b + a + '1' )
# print(1 + a + A(3))
#


# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#         #print('A.init')
#
#     def __get__(self, instance, owner):
#         return self
#
#     def __set__(self, instance, value):
#         #print(value,'~~~~~~~~~~~')
#         self.data = value
#
#
# class B:
#     x = A()
#     def __init__(self):
#         pass
#         #print('B.init')
#         self.x = 'b.x~~~~~~'
#         #self.z = 123
#
#
#
# b = B()
# print(b.x)
# print(B.x.a1)
# print(b.__dict__)
# print(b.x.__dict__)
# print(b.x.data)
# b.x = 500
#
#
# print(b.x)
# print(b.x.__dict__)

# print(b.z)
# print(b.z.__dict__)


# class A:
#     #a1 = 3
#     def __init__(self):
#         self.a1 = 'a1'
#         print('A.init')
#
#     # def __get__(self, instance, owner):
#     #     return self
#
#     def __set__(self, instance, value):
#         #print(value)
#         self.data = value
#         #instance.data = value
#

# class B:
#     x = A()
#     y = A()
#     def __init__(self):
#         print('B.init')
#         #print(self)
#         self.x = 333
#         self.y = 111


#print(B.x)
#print(B.x.a1)

#print(B.x.a1)
# b = B()
#print(B())

#print(B.x)
# print(b.x)

#print(b.x.a1)
#print(b.x.__dict__)
#print(b.x.a1)
# print(b.x)
# print(b.y)
# print(b.y.__dict__)
# # print(b.x.__dict__)
# # print(B.x)
# # print(b.__dict__)
# print(b.x)
#
# b.x = 500
# print()


# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#
#     def __get__(self, instance, owner):
#         print('get~~~~~~~~',self)
#         return self
#
#     def __set__(self, instance, value):
#         # self.data = value
#         # print(self,'````````````````````````')
#         # print('set~~~~~~~~~~~~')
#         #self.data = value
#         #instance.__dict__['x'] = value
#         if instance:
#             raise AttributeError('no')
#
#     # def __delete__(self, instance):
#     #     instance.data = '1'
#
# class B:
#     x = A()
#     def __init__(self):
#         #self.y = A()
#         self.x = 'b.x'
#         #print(self,'++++++++++++++++++++++')
#         pass
#

# class A:
#     def __init__(self):
#         self.a1 = 'a1'
#
#     def __get__(self, instance, owner):
#         return self
#
#     def __set__(self, instance, value):
#         self.__dict__['x'] = value
#
#     def __set_name__(self, owner, name):
#         print(name,self,owner)
#         self.name = name
# class B:
#     x = A()
#     y = A()
#     def __init__(self):
#         self.x = 'abc'
#
# b =B()
# b.x.a1 = 300
# print(b.x.a1)
# print(b.x.__dict__)
# print(b.y.__dict__)
# from functools import partial,update_wrapper
#
# class Stm:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#
#         return self.fn
#
#
# class Clas:
#     def __init__(self,fn):
#         self.fn = fn
#
#     def __get__(self, instance, owner):
#         newfun = partial(self.fn,owner)
#         update_wrapper(newfun,self.fn)
#         return newfun
#
#
#
# class A:
#
#     @Stm    #smtd = Stm(smtd)(x,y)
#     def smtd(x,y):
#         print ('static',x,y)
#
#     @Clas   #cls = Clas(cls,x,y)
#     def cls(cls,x,y):
#         '''++++++++++++++'''
#         print(cls.__name__,x,y)
#
#
# a = A()
# a.smtd(3,4)
# a.cls(10,11)
# print(a.cls.__name__,a.cls.__doc__)
# print()

