# print('Hello')
# print("Здесь будут домашние работы")
import re

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
import re

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
def valid_num(tel):
    reg = r'^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}$'
    return re.findall(reg, tel)[0]


print(valid_num('+7 499 456-45-78'))
print(valid_num('+74994564578'))
print(valid_num('7 (499) 456 45 78'))
print(valid_num('7 (499) 456-45-78'))

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
