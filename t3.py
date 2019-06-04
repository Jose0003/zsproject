# """
# s = [11,20,33,2,3,4,5,7,9]
# print(sorted(s))
# """
# # import time
# # s = [11,20,33,2,3,4,5,7,9]
# #
# # print(filter(lambda x:x>4,s))
# #
# # print(sorted(filter(lambda x:x>4,s)))
# # filter(lambda x:x>4,s)
# """
# class A:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#         self.d = []
#
#     def __call__(self, *args, **kwargs):
#
#         for i in args:
#             self.a,self.b = self.b,self.a + self.b
#             self.d.append(self.a)
#         return self.d
# """
#
#
#
# # class Test:
# #     def __init__(self):
# #         self.d = []
# #
# #     def __call__(self, *args, **kwargs):
# #         a = 0
# #         b = 1
# #         for i in args:
# #             x = i-1
# #
# #         if int(*args) < len(self.d):
# #             return self.d[x]
# #
# #         for i in range(*args):
# #             a,b = b,a+b
# #             self.d.append(a)
# #         return a
# #
# #
# # a = Test()
# #
# # print(a(11))
# # print(a(8))
# # print(a.d)
#
# """
#
# class A:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#         self.d = []
#
#     def __call__(self, index):
#         if index == 0:
#             return 0
#         if index > len(self.d):
#             for x in range(len(self.d), index):
#                 self.a, self.b = self.b, self.a+self.b
#                 self.d.append(self.a)
#                 print('++++++++++++++++')
#             return self.a
#         else:
#             return self.d[index-1]
#     def __repr__(self):
#         return '{} {}'.format(__class__.__name__,self.d)
#
#     def __getitem__(self, index):
#         return self.d[index-1]
# """
#
# import importlib
# import test01.t13
# test01.t13.A().showme()
#
# getattr(test01.t13.A,'showme')(1)

# class A:
#     def foo1(self,name:str,sep=':'):
#         self.name = name
#         n = name.partition(sep)
#         m,_,c = n
#         mode = importlib.import_module(m)
#         getattr(mode,c)(1)
#
#
#
# a = A()
# a.foo1('test01.t13:A.showme')

# m = importlib.import_module('test01.t13')
#
# print(m.A.showme)
#
#
# # print(getattr(m,'A.showme'))
# import sys
# print(sorted(filter(lambda x:x.startswith('m'),sys.modules.keys())))

# import importlib
#
#
# def foo1(name: str, sep=':'):
#     m, _, c = name.partition(sep)
#     mod = importlib.import_module(m)
#     cls = getattr(mod, c)
#     return cls().showme()
#
#
# if __name__ == '__main__':
#     foo1('test01.t13:A')
#

# import importlib
#
#
# def foo1(name: str, sep=':'):
#     m, _, c = name.partition(sep)
#     mod = importlib.import_module(m)
#     cls = getattr(mod, c)
#     return cls().showme()
#
#
# foo1('test01.t13:A')

