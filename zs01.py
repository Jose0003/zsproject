# class A:
#     def __init__(self,a):
#         self.a = a
#
#
# a = A(3)
# print('in 01',dir())
"""
class A:
    def __init__(self):
        self.d = []
        self.d = sorted(self.d)
    def fib(self,x,a=0,b=1):
        for i in range(x):
            a,b =b,a+b
            self.d.append(a)
        return a
    def __iter__(self):
        return iter(self.d)

    def __len__(self):
        return len(self.d)

    def __getitem__(self, item):
        return self.d[item]

    def __setitem__(self, key, value):
         self.d[key] = value

    def __str__(self):
        return str(self.d)

a =A()
print(a.fib(10))
print(a.d)
print(a[4])
print(len(a))
print(a)
for i in a:
    print(i)

"""
