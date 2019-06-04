class StaticMethod:

    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return self.fn


from functools import partial

class ClassMethod:
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        return partial(self.fn,owner)


class A:

    @StaticMethod   #smtd = StaticMethod(smtd)(x,y)
    def smtd(x,y):
        print('666',x,y)

    @ClassMethod     #foo = ClassMethod(foo)(cls,x,y)
    def foo(cls,x,y):
        print(cls.__name__,x,y)


a = A()
a.smtd(3,4)
a.foo(1,2)
class TypeCheck:
    def __init__(self,name,typ):
        self.name = name
        self.type = typ

    def __get__(self, instance, owner):
        if instance:
            return instance.__dict__[self.name]
        else:
            return self

    def __set__(self, instance, value):
        if instance:
            if isinstance(value,self.type):
                instance.__dict__[self.name] = value
            else:
                raise  TypeError(self.name + '----------')


import inspect
class Datainject:
    def __init__(self,fn):
        self.fn = fn
        sig = inspect.signature(self.fn)
        params = sig.parameters
        for name,param in params.items():
            if param.annotation != param._empty:
                setattr(self.fn,name,TypeCheck())

    def __call__(self, *args, **kwargs):

        return self.fn(*args,**kwargs)

    def datainject(self):

        '''pass'''




# Person = Datainject(Person)


