# info = 'test, url("http://www.baidu.com")&,dddddd "=" <svg></svg><path></path><imgsrc="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'
#
# import re
# regex = re.compile('url("http://www.baidu.com")')
# print(regex)
# result = regex.sub("url('http://www.baidu.com')",info,1)
# print(result)

# import json
# from pathlib import Path
# p = Path('E:/test/a.txt')
#
# with open(p, 'r+') as f:
#     j = json.dump(f)
#



# class Student:
#     d = {}
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.d[name] = age
#
#     def allstudent(self):
#         return len(__class__.d)
#
# if __name__ == '__main__':
#
#     a = Student('a', 1)
#     b = Student('b', 2)
#     c = Student('c', 3)
#     print(Student.d)
#     print(len(Student.d))
#     print(a.allstudent())


# class House:
#     def __init__(self, Apartment, area, furniture=[]):
#         self.Apartment = Apartment
#         self.area = area
#         self.furniture = furniture
#         #家具
#         self.bed = 4
#         self.bookcase = 2
#         self.table = 1.5
#         self.chair = 2
#
#     def showallarea(self):
#         return self.area
#
#
#     def residual_area(self):
#         area = self.area
#         for i in self.furniture:
#             if i == 'bed':
#                 area = area - 4
#             elif i == 'bookcase':
#                 area = area - 2
#             elif i == 'table':
#                 area = area - 1.5
#             elif i == 'chair':
#                 area = area - 2
#         return area
#
# a = House('a', 10, ['bed', 'bookcase', 'chair'])
# print(a.Apartment)          #户型
# print(a.area)               #面积
# print(a.residual_area())    #剩余面积
# print(*a.furniture)         #家具名称

# class Book:
#
#     def __init__(self, title, author, number, borrower=None):
#         self.title = title
#         self.author = author
#         self.number = number
#         self.borrower = borrower
#
#
# a = Book('a', 'zz', 1)
# b = Book('b', 'ss', 2)
# c = Book('c', 'vv', 3)
# d = Book('d', 'ww', 4)
#
# class BookManagement:
#     book_list = ['a', 'b', 'c', 'd']
#     borrowerlist = {}
#     def __init__(self):
#         pass
#     #借书
#     def borrowing(self, name, borrower):
#         self.borrower = borrower
#         if self.borrowerlist[borrower] > 3:
#             raise ('not borrowing')
#         if borrower not in self.borrowerlist:
#             self.borrowerlist[borrower] = 1
#         else:
#             self.borrowerlist[borrower] += 1
#         self.book_list.remove(name)
#
#     #找书
#     def lookupbook(self, name):       #书名a,b,c
#         if name in self.book_list:
#             print('ok')
#         else:
#             print('no')
#     #加书
#     def addbook(self, name):          #书名abcd
#         self.book_list.append(name)
#
#     #归还
#     def giveback(self,name):
#         self.book_list.append(name)
#
#
# test = BookManagement()
# test.borrowing('a', 'tom')
# test.borrowing('c', 'tom')
# test.borrowing('b', 'tom')
# test.borrowing('d', 'tom')
# print(test.borrowerlist)
# test.addbook('d')
# print(test.book_list)
# print(test.lookupbook('a'))



# from functools import wraps
#
# def logger(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         print('begin')
#         ret = fn(*args,**kwargs)
#         print('over')
#         return ret
#     return wrapper
#
#
# @logger
# def foo1(x, y):
#     return x+ y
# import re
# info = 'test, url("http://www.baidu.com")&,dddddd "=" <svg></svg><path></path><imgsrc="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'
#
# regex = re.compile('in.*')
# result = regex.sub('</img>ininnnin<img src="http://www.dd.com"></img>"', info)
# print(result)

# from pathlib import Path
# p = Path('E:/test/a.txt')
#
# for i,j in enumerate(p.read_text()):
#
#     print(j,end='')

# all = 0
# dict_test = {}
# with open("E:/test/a.txt", "r+", encoding="utf-8") as f:
#     for line in f.readlines():
#         line = line.strip().split(" ")
#         a = line[0]
#         dict_test['name'] =line[0]
#         dict_test['price'] =line[1]
#         dict_test['amount'] = line[2]
#         print(dict_test)
#         all += int(line[1]) * int(line[2])
#         print(line)
#
# print(all)


# import re
# info = 'test, url("http://www.baidu.com")&,dddddd "=" <svg></svg><path></path><imgsrc="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'
#
# regex = re.compile('in.*')
# result = regex.sub('</img>ininnnin<img src="http://www.dd.com"></img>"', info)
# print(result)
#
# import re
# info = 'test, url("http://www.baidu.com")&,dddddd "=" <svg></svg><path></path><imgsrc="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'
#
# regex = re.compile('url.*&')
# result = regex.sub("url('http://www.baidu.com')&", info)
# print(result)
import time
import threading


# def work(x, y):
#     a = 0
#     while True:
#         if a == x:
#             break
#         time.sleep(y)
#         a += 1
#         print('I am working')
#         print(threading.current_thread())
#         # print(threading.get_ident())
#     print('finshed')
#
#
# t = threading.Thread(target=work, name='work', args=(1, 1))
# t.start()
def work():
    for i in range(5):
        time.sleep(1)
        print('i am working')
    print('finished')

class MyThread(threading.Thread):
    def start(self):
        print('start~~~')
        super().start()

    def run(self):
        print('run~~~')
        super().run()


t = MyThread(target=work, name='work')
t.start()
