a = float (input("vvedite a:"))
b = float (input("vvedite b:"))
c = float (input("vvedite c:"))
d = b**2 - 4 *a*c
if d > 0:
    x1 = (-b + d**0.5) / (2* a)
    x2 = (-b - d**0.5) / (2* a)    
    print ("Answer: x1=", x1, "x2=", x2 )
elif d == 0:
    x1 = -b / (2*a)
    print("Answer: x1=" , x1)
else:
    print("korney net")