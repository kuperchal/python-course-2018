from math import ceil

d=float(input("Введите диаметр бака: "))
h=float(input("Введите высоту бака: "))
s=float(input("Введите какую площаь можно окрасить одной банкой краски: "))
pi=3.14159265
print("potrebuetsya", ceil(2*(2*pi*d*d/4+pi*d*h)/s), "banok kraski")