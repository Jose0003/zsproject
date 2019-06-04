# class A:
#     d = {}
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.d['x'] = x
#         self.d['y'] = y
#
#     def __setattr__(self, key, value):
#         self.d[key] = value
#         self.__dict__[key] = value
#
#     def __getattr__(self, item):
#         if item not in self.d.keys():
#             self.d[item] = 100
#         return self.d[item]
#
#     def __getattribute__(self, item):
#         raise AttributeError('aaaaa')
#
#
#
#
# a = A(3,5)
# print(a.x)
# print(a.fgdf)
# print(a.__dict__)
# print(a.d)
#


# class A:
#     d = {}
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __getattr__(self, item):
#         if item not in self.__class__.d.keys():
#             self.__class__.d[item] = 999
#         return self.__class__.d[item]
#
#     def __setattr__(self, key, value):
#         self.__class__.d[key] = value
#         #print(self.__class__.d)
#
#
#
# a = A(1,2)
# print(a.d)
# print(a.dasd)

def foo1():
    print('123')


class A:
    def __init__(self):
        self.ls = foo1

    def reg(self,name,fn):
        setattr(self,name,fn)

    def scheduler3(self):
        while True:
            x = input('>>>')
            if x == 'quit':
                break
            getattr(self,x,lambda :print('no no no'))()

    def __call__(self, *args, **kwargs):
        return self.scheduler3()



a = A()
#a.scheduler3()
a()
