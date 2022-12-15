# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти "))
if quarter == 1:
    print("X = from 0 to ∞, Y = from 0 to ∞")
if quarter == 2:
    print("X = from 0 to -∞, Y = from 0 to ∞")
if quarter == 3:
    print("X = from 0 to -∞, Y = from 0 to -∞")
if quarter == 4:
    print("X = from 0 to ∞, Y = from 0 to -∞")
if quarter >= 5:
    print("Не корректный ввод")