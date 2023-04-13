""" Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""
n = int(input())
g = 0
while 2 ** g < n:
    x = 2 ** g
    c = 0
    if x // 1000 != 0:
        while x // 1000 != 0:
            c += 1
            x = x // 1000
        x = str(x) + "k" * c
    print(x)
    g += 1