# import importlib
#
#
# def foo1(name: str, sep=':'):
#     m, _, c = name.partition(sep)
#     print(c)
#     mod = importlib.import_module(m)
#     cls = getattr(mod, c)
#     print(mod)
#     return cls()
#
#
#
#
#
# # import test01.t13
# # getattr(test01.t13,'test01.t13.A')
# import inspect
# # class A:
# #     def __init__(self, name: str, age: int):
# #
# #         if not isinstance(name, str) or not isinstance(age, int):
# #             raise TypeError('666')
# #         self.name = name
# #         self.age = age
#
#
#
#
#
# #
# # def checkdata(fn):
# #     def winner(*args):
# #         sign = inspect.signature(args)
# #         params = sign.parameters
# #         print(params)
# #         print(params.values())
# #         for n, i in params.items():
# #             print(n, i.annotation)
# #             if isinstance(n, i.annotation):
# #                 pass
# #                 # print('111')
# #             else:
# #                 print('nonono')
# #     return winner
#
#
# # @checkdata   #A = checkdata(A)(args)
# # class A:
# #     def __init__(self, n: str, a: int):
# #         self.n = n
# #         self.a = a
#
#
# # a = A('123', 123)
#
# def checkdata(fn):
#     def wrapper(*args):
#         sig = inspect.signature(fn)
#         # print(sig)
#         params = sig.parameters
#         # print(params)
#         values = list(params.values())
#         # print(values)
#
#         for i, p in enumerate(args):
#             # print(i, p)
#             if not isinstance(p, values[i].annotation):
#                 print('TypeError')
#
#     return wrapper
# # @checkdata        #add3 = checkdata(add3)(x,y)
# def add3(x: str, y: int):
#     # if not isinstance(x,str):
#     #     print('123')
#     # if not isinstance(y,int):
#     #     print('456')
#     sig = inspect.signature(add3)
#     print(sig)
#     params = sig.parameters
#     print(params)
#     return x + y
#
#
# add3('1', '2')
# # print(add3('1','2'))
import inspect

def checkdata(cls):
    def inner(*args):
        sig = inspect.signature(cls)
        params = sig.parameters
        print(params)

        values = list(params.values())
        # print(params.annotation)
        for i, j in enumerate(args):
            print(j, values[i].annotation)
            if not isinstance(j, values[i].annotation):
                print('~~~~~~~~~~~~')
            else:
                print('+++')

    return inner


@checkdata   #A = checkdata(A)(args)
class A:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


a = A('a', 2)
