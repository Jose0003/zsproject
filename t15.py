# import threading
# import time
# def worker():
#     print('1')
#     print('fineshed')
#
#
# def foo1(x, y):
#     for i in range(x):
#         time.sleep(y)
#         print(threading.current_thread().ident)
#
#
# t = threading.Thread(target=foo1, name='foo1', args=(3, 1))
# t.start()

# import re
#
# s = '''bottle\nbag\nbig\nable'''
# result = re.findall('b',s)
# print(result)
# regex = re.compile('^b')
# result = regex.findall(s)
# print(result)

# class A:
#     def __init__(self,name):
#         self.name = name
#
#
# class B(A):
#     def foo1(self):
#         print('1')
#

# from functools import wraps
# import inspect
# import time
#
# def foo1(fn):
#     local_cache = {}
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters
#         # print(params.keys())
#         # param_name = [key for key in params.keys()]
#         params_dict = {}
#
#         params_dict.update(zip(params.keys(), args))
#         print(params_dict)
#
#         params_dict.update(kwargs)
#         # print(kwargs)
#         print(params_dict)
#
#         key = tuple(sorted(params_dict.items()))
#         # print(key)
#         print(params_dict.items())
#         if key not in local_cache.keys():
#             local_cache[key] = fn(*args, **kwargs)
#         print(local_cache)
#         return local_cache[key]
#     return wrapper
#
#
# @foo1
# def add3(x, y, z=6):
#     time.sleep(1)
#     return x + y + z
#
#
# print(add3(1, 2, z=3))
#
# print(add3(1, 2, 3))
#
# print(add3(1, 2, 4))

# import inspect
# from functools import wraps
# import time
#
#
# def foo2(fn):
#     local_cache = {}
#
#     def wrapper(*args, **kwargs):
#         sig = inspect.signature(fn)
#         params = sig.parameters
#
#         cache_dict = {}
#
#         cache_dict.update(zip(params.keys(), args))
#
#         cache_dict.update(kwargs)
#         keys = tuple(sorted(cache_dict.items()))
#
#         if keys not in local_cache.keys():
#             local_cache[keys] = fn(*args, **kwargs)
#         # print(cache_dict)
#         # print(keys)
#         return local_cache[keys]
#     return wrapper
#
#
# @foo2
# def foo1(x, y, z=3):
#     time.sleep(2)
#     return x + y + z
#
#
# print(foo1(1, 2, z=3))
# print(foo1(z=3, x=1, y=2))
# print(foo1(1, 2, 3))
# import os
# import shutil

# print(os.stat('E:/test'))
# with open('E:/test/asdasd.txt', 'w+') as f1:
#     f1.write('1qaws3ed5tg')
#     f1.seek(0)
#     print(f1.read())
#
# shutil.copy('E:/test/asdasd.txt', 'E:/test/asd3.txt')



# p = Path('E:/test/asdasd.txt')
# # for i in p.iterdir():
# #     print(i)
# print(p.exists())
# print(p.name)
# print(p.suffix + p.stem)
# print(p.stem)
# print(p.with_name('zs.txt').exists())
# if not p.with_name('zs.txt').exists():
#     p.with_name('zs.txt').touch()
#
# from pathlib import Path
# p1 = Path('E:/test/dirs/s/w/a')
#
# print([[*p1.parents][i] for i in range(5)])
# s = [[*p1.parents][i] for i in range(5)]
# for i in s:
#     if i.is_dir():
#         flag = False
#         for _ in i.iterdir():
#             flag = True
#             break
#         print('not Empty' if flag else 'Empty',sep='\t')
#     elif i.is_file():
#         print('file')
#     else:
#         print('other')
#
# print(*p1.glob('[a-z0-9]*'))
# if p1.match('[a-z]*'):
#     print('666')
# from urllib.parse import urlparse
#
# urls = ['https://www.baidu.com/', 'https://www.runoob.com/mongodb/mongodb-tutorial.html']
#
# for i, url in enumerate(urls,1):
#     t = urlparse(url)
#     print(i, url)
#     print(i, t, t.path)
from queue import Queue


def ip_handle(q: Queue):
    ips = {}
    while True:
        data = q.get()
        ip = data.get('remote')
        if ip:
            ips[ip] = ips.get(ip, 0) + 1
        print(len(ips), ips.keys())
        print(sorted(ips.items(), key=lambda x: x[1], reverse=True))

