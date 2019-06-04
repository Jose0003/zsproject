
# import zs01
# print('01  ',dir(zs01))
# class B(zs01.A):
#     def __init__(self,b):
#         super().__init__(b)
#         self.c = 100
#     def __dir__(self):
#         return {6,7,8,9}
#
# x= 100
#
# print('in 02 {}'.format(__name__),dir())
#
# print('*'*150)
#
# print(dir(B))
# print(sorted(B.__dict__.keys() | zs01.A.__dict__.keys() | object.__dict__.keys()))
#
# c = B('e')
# print(dir(c))
#
# print(dir())
# class A:
#     def __init__(self):
#         self.e = 5
#
#     def foo1(self):
#         self.f = 6
#
#
#
# class C:
#     c =3
#     def __init__(self):
#         self.a = []
#         self.f = 5
#     def foo(self,e=5):
#         c = 4
#         d = 6
#         #self.ccc = 5
#         print(2,dir())
#
#
# def foo3(a=1,b=2):
#     c =3
#     print(3,dir())
#
# #
# # foo3()
# x = C()
# # x.foo()
# print(5,x.__dict__)
# print(1,dir(C))
# print(3,dir())
# print(2,sorted( locals().keys()))
# print(locals()['x'].c)
#
# print(locals())
#
# print(globals())


# class B:
#     def __init__(self, a=3, b=4, c=5):
#         self.a = a
#         self.b = b
#         self.c = c
#
#
# class A:
#     def __init__(self, x):
#         self.x= x
#
#     def __sub__(self, other):
#         return self.x - other.x
#
#     def __isub__(self, other):
#         self.x -= other.x
#         return self
#
#     def __repr__(self):
#         return '{}'.format(self.x)
#
#     def __add__(self, other):
#         return self.x + other.x
#
#
#
# a = A(10)
# b = A(12)
# a -=b
# print(a)
# print(a.x)
"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.__class__(self.x + other.x,self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __repr__(self):
        return 'Point({},{})'.format(self.x,self.y)

    def __sub__(self, other):
        return self.x - other.x ,self.y - other.y


# a = Point(1,2)
# b = Point(3,4)
# a += b
# print(a + b + a)
# print(a)

class A(dict):
    def __init__(self):
        super().__init__()
        self.d = []
    def __add__(self, other):
        self.d.append(other)
        return self

    def __missing__(self, key):
        return '{} not in {}'.format(key,A.__name__)

    def __len__(self):
        return len(self.d)

    def __contains__(self, item):
        return item in self.d

    def __iter__(self):
        return iter(self.d)

    def __getitem__(self, item):
        return self.d[item]

    def __setitem__(self, key, value):
        self.d[key] = value



a = A()
a.d.append(3)
a.d.append(6)
print(a.d)
print(6 in a)
for i in a:
    print(i)
print(a.get(1))
a[0] = 100
a[1] = 101
print(a.d)
print(101 in a)
print(a[1])
print(a + 4 + 5)
print(a.d)

"""

with open('zs01.py') as f:
    print(f.read())