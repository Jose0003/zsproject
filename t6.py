from datetime import datetime

"""
class A:
    def __init__(self):
        print('111111')

    def __enter__(self):
        print('222222')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print('3333333')
        return self

a = A()

with a as b:
    print('4444444')

    print('5555555')

print(a is b)
print(a == b)
print(a)
print(b)

"""
import time
import datetime
from functools import wraps


def Timeit(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        '''wrapper'''
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__,'{:.2f}'.format(delta))
        print(fn.__doc__)
        return ret
    return wrapper

@Timeit       #add3 = Timeit(add3)(x,y)
def add3(x,y):
    '''add3'''
    time.sleep(1)
    return x + y


#add3(3,4)


class TimeIt:
    def __init__(self,fn):
        self.fn = fn

    def __enter__(self):
        self.start = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delta = (datetime.datetime.now() - self.start).total_seconds()
        print(self.fn.__name__,self.delta)


with TimeIt(add3) as f:
    for i in range(3):
        add3(4, 5)

with open('t5.py') as f:
    print(f.read())

