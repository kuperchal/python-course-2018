# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:33:11 2018

@author: Роман
"""

a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4*a*c
x1 = (-b + D**0.5) / (2*a)
x2 = (-b - D**0.5) / (2*a)
x = -b / (2*a)
if D < 0:
    print ('Корней нет')
elif D > 0:
    print (x1)
    print (x2)
elif D == 0:
    print (x)


d = float(input())
h = float(input())
S_с_одной_банки = 5
S_круга = 3.14 * d**2 / 4
S_цилиндра = 3.14 * d * h
S_бака = (S_круга * 2 + S_цилиндра) * 2
print (S_бака / S_с_одной_банки)


a = float(input())
b = float(input())
c = float(input())
P = a+b+c
S = a*b/2
if c**2 != a**2 + b**2:
    print ('Треугольник непрямоугольный')
else:
    print (P)
    print (S)
