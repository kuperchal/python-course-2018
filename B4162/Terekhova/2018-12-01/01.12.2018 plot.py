import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-6,6.01,0.01) #Массив значений аргумента для Синуса и Косинуса
x1=np.arange(-1.56,1.57,0.05) #Массив значений аргумента для тангенса
c=np.arange(0,3.15,0.05) #Массив значений аргумента для котангенса
plt.subplot(221) #Графическая область 1 размером 2х2
plt.plot(x,np.sin(x),'m') #Построение графика с определенным цветом в области Х
plt.title(r'$\sin(x)$') #Называем график
plt.xlabel(r'$x$') #Добавляем подпись для оси Х
plt.ylabel(r'$f(x)$') #Добавляем подпись для оси У
plt.annotate('local max', xy=(1.57, 1), xytext=(1.58, 1),) #Добавляем надпись local max
plt.annotate('local min', xy=(-1.57, -1), xytext=(-1.58, -1),) #Добавляем надпись local min
plt.subplot(222) #Графическая область 2 размером 2х2
plt.plot(x,np.cos(x),'k') #Построение графика с определенным цветом в области Х
plt.grid(True)
plt.title(r'$\cos(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.annotate('local max', xy=(0, 1), xytext=(0.01,1),)
plt.annotate('local min', xy=(-3.14, -1), xytext=(-3.15, -1),)
plt.subplot(223)
plt.plot(x1,np.tan(x1),'y') #Построение графика с определенным цветом в области Х1
plt.title(r'$tg(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.text (-1, -25, u"HET max u min")
plt.subplot(224)
plt.plot(c,1/np.tan(c),'c') #Построение графика с определенным цветом в области С
plt.title(r'$ctg(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.text (0.5, 10, u"HET max u min")
plt.show()
print('Bbedute slovo')
sl=input()
if sl=='again':
    plt.subplot(221)
    plt.plot(x,np.sin(x),'m')
    plt.title(r'$\sin(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.annotate('local max', xy=(1.57, 1), xytext=(1.58, 1),)
    plt.annotate('local min', xy=(-1.57, -1), xytext=(-1.58, -1),)
    plt.subplot(222)
    plt.plot(x,np.cos(x),'k')
    plt.grid(True)
    plt.title(r'$\cos(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.annotate('local max', xy=(0, 1), xytext=(0.01,1),)
    plt.annotate('local min', xy=(-3.14, -1), xytext=(-3.15, -1),)
    plt.subplot(223)
    plt.plot(x1,np.tan(x1),'y')
    plt.title(r'$tg(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.text (-1, -25, u"HET max u min")
    plt.subplot(224)
    plt.plot(c,1/np.tan(c),'c')
    plt.title(r'$ctg(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.text (0.5, 10, u"HET max u min")
    plt.show()
