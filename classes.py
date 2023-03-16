# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.last_name} {self.first_name} {self.age} ", end='')
#
#
# class Student(Human):
#     def __init__(self,  last_name, first_name, age, speciality, group, rating):
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#         super().__init__(last_name, first_name, age)
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.group} {self.rating} ", end='')
#
#
# class Teacher(Human):
#     def __init__(self, last_name, first_name, age, speciality, exp):
#         self.speciality = speciality
#         self.exp = exp
#         super().__init__(last_name, first_name, age)
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.exp}", end=' ')
#
#
# class Graduate(Student):
#     def __init__(self, last_name, first_name, age, speciality, group, rating, topic):
#         super().__init__(last_name, first_name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f'{self.topic}', end=' ')
#
#
# group1 = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group1:
#     i.info()

import math

# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)



