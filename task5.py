# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# d = √ (х А – х В) 2 + (у А – у В) 2

a = int(input("Введите координату x для первой точки "))
b = int(input("Введите координату y для первой точки "))

a1 = int(input("Введите координату x для второй точки "))
b1 = int(input("Введите координату y для второй точки "))

import math
distance = math.sqrt((a - b)**2 + (a1-b1)**2)
print("%.2f" % distance)