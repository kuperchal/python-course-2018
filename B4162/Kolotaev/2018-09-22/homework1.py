d=float(input("Введите диаметр бака: "))
h=float(input("Введите высоту бака: "))
s=float(input("Введите какую площаь можно окрасить одной банкой краски: "))
pi=3.14159265
a = 2*(2*pi*d*d/4+pi*d*h)
if a % s == 0  :
  b=a/s
else:
 b=a//s+1

print("potrebuetsya", b, "banok kraski")
