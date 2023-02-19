# print('Hello')
# print("Здесь будут домашние работы")
import math
# import re
# from random import randint
# import os
# import os.path
# import time

# Методы строк
# Задача 1
# s = "I am learning Python. hello, World!"
# ind = s.find('h')
# ind1 = s.rfind('h')
# s1 = s[:ind] + s[ind1 + 1:]
# print(s1)
#
# # Задача 2
# s2 = s[:ind] + s[ind1:ind:-1] + s[ind1:]
# print(s2)
#
# # Задача 3
# st, ch, new_ch = input("Введите строку: "), input("Введите подстроку: "), input("На что заменить? -> ")
# st = st.replace(ch, new_ch)
# print(st)
#
# #Задача 4
# st1 = "Ежевику для ежат Принесли два ежа. Ежевику еле-еле Ежата возле ели съели."
# print(st1)
# st2 = st1.lower().split()
# counter = 0
# print(st2)
# for i in st2:
#     if i.startswith('е'):
#         counter += 1
# print("Количество слов:", counter)

# Замыкания, анонимные ф-и
# Задача 1
# def func_compute(a):
#     def func1(b):
#         return a * b
#
#     return func1
#
#
# res = func_compute(2)
# print(res(15))
# print(res(20))
# res = func_compute(3)
# print(res(15))
# print(res(20))

# Задача 2
# print((lambda a, b, c: a * b * c)(2, 5, 5))

# Задача 3
# test = [{'name': 'Jennifer', 'final': 95},
#         {'name': 'David', 'final': 92},
#         {'name': 'Nikolas', 'final': 98}]
# print(test)
# res = sorted(test, key=lambda item: item['name'])
# print(res)
# res = sorted(test, reverse=True, key=lambda item: item['final'])
# print(res)
#
# # Задача 4
# res = max(test, key=lambda item: item['final'])
# print(res)
# res = min(test, key=lambda item: item['final'])
# print(res)

# Декораторы

# def func(fn):
#     def wrap(*nums):
#         fn(*nums)
#         print("Среднее арифметическое чисел", *nums, "=", sum(nums) / len(nums))
#     return wrap
#
#
# @func
# def summa(*nums):
#     print("Сумма чисел", *nums, "=", sum(nums))
#
#
# summa(2, 3, 3, 4)


# методы строк и re
# Задача 1

# def password_ok(pas):
#     return re.findall(r'^[a-z\d@_-]{6,18}$', pas, re.IGNORECASE)
#
#
# passw = input("Введите пароль: ")
# print("Пароль", password_ok(passw), "сохранен")

# Задача 2
# my_date = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков.'
# reg = r'[\d]{2}/\d{2}/\d{4}'
# print(re.findall(reg, my_date))

# re и рекурсия
# Задача 1
# def valid_num(tel):
#     reg = r'^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}$'
#     return re.findall(reg, tel)[0]
#
#
# print(valid_num('+7 499 456-45-78'))
# print(valid_num('+74994564578'))
# print(valid_num('7 (499) 456 45 78'))
# print(valid_num('7 (499) 456-45-78'))

# Задача 2
# def neg_val(lst):
#     if len(lst) == 0:
#         return 0
#     else:
#         count = neg_val(lst[1:])
#         if lst[0] < 0:
#             count += 1
#         return count
#
#
# l1 = [3, -5, 11, 2, -7, 8, -2]
# print(neg_val(l1))


# Бинарный поиск

#
# def my_sort(ls, item):
#     first = 0
#     last = len(ls) - 1
#     found = False
#     while first <= last and not found:
#         mid = (first + last) // 2
#         if ls[mid] == item:
#             found = True
#         else:
#             if item < ls[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     if found:
#         print("Число", item, "присутствует в списке.")
#     else:
#         print("Число", item, "не присутствует в списке.")
#
#
# my_list = [randint(1, 100) for i in range(10)]
# print(my_list)
# a = int(input("Введите число: "))
# my_sort(sorted(my_list), a)


# сортировка, поиск и файлы
# Задача 1
# def my_search(ls, item):
#     pos = 0
#     found = False
#     while pos < len(ls) and not found:
#         if ls[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# my_list = [randint(1, 100) for i in range(10)]
# print(my_list)
# a = int(input("Введите число: "))
# if my_search(my_list, a):
#     print(f"Число {a} в списке присутствует")
# else:
#     print(f"Число {a} в списке отсутствует")

# Задача 2
# f = open('mytext.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# a = int(input("Введите номер строки для удаления: "))
# f.close()
#
# f = open('mytext.txt', "r")
# read_f = f.readlines()
# for i in range(len(read_f)):
#     if i == a:
#         read_f.remove(read_f[i-1])
# print(read_f)
# f.close()
#
# f = open('mytext.txt', 'w')
# f.writelines(read_f)
# f.close()

# Задача 3
# def my_search(ls, item):
#     pos = 0
#     found = False
#     while pos < len(ls) and not found:
#         if ls[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# def up_sort(a):
#     n = len(a)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a
#
#
# def down_sort(a):
#     n = len(a)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if a[j] < a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a
#
#
# ls1 = [5, 9, 6, 7]
# ls2 = [3, 11, 8]
# ls3 = [2, 4]
# ls4 = [10, 1, 12]
# new_list = ls1 + ls2 + ls3 + ls4
# print(ls1, ls2, ls3, ls4)
# print(new_list)
# print("1 - сортировка по убыванию\n2 - сортировка по возрастанию")
# a = int(input("-> "))
# if a == 1:
#     print(down_sort(new_list))
# elif a == 2:
#     print(up_sort(new_list))
# else:
#     print("ошибка")
#
# b = int(input("Введите значение для поиска: "))
# if my_search(new_list, b):
#     print(f"Значение {b} найдено")
# else:
#     print(f"Значение {b} не найдено")

# файлы
# Задача 1
# file1 = 'first.txt'
# file2 = 'second.txt'
# w_file = 'third.txt'
# with open(file1, 'r') as f1, open(file2, 'r') as f2, open(w_file, 'w') as wf:
#     for line in f1:
#         wf.write(line)
#     for line in f2:
#         wf.write(line)

# Задача 2

# test = input("Введите путь к файлу: ")
# a = os.path.exists(test)
# print(a)
# if a:
#     print(os.path.dirname(test))
#     print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getatime(test))))
# else:
#     print(f"Файла {test} не существует")

# классы
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Длина:", x)
        print("Ширина:", y)

    def s(self):
        print("Площадь:", self.x * self.y)
    def per(self):
        print("Периметр:", (self.x + self.y) * 2)
    def gep(self):
        print("Гипотенуза:", round(math.sqrt(self.x**2 + self.y**2), 2))
    def print_rec(self):
        for _ in range(self.y):
            for _ in range(self.x):
                print("*", end='')
            print()


r1 = Rectangle(9, 3)
r1.s()
r1.per()
r1.gep()
r1.print_rec()

r2 = Rectangle(10, 7)
r2.s()
r2.per()
r2.gep()
r2.print_rec()
