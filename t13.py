

import importlib


def foo1(name: str, sep=':'):
    m, _, c = name.partition(sep)
    mod = importlib.import_module(m)
    cls = getattr(mod, c)
    return cls().showme()


foo1('m:A')
