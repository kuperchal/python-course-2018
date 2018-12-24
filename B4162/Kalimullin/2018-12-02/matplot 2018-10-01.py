import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-6,6.01,0.01)
x1=np.arange(-1.56,1.57,0.05)
c=np.arange(0,3.15,0.05)
#subplot 1
plt.subplot(221)
plt.plot(x,np.sin(x))
plt.title(r'$\sin(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.annotate('local max', xy=(1.57, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.01),)
plt.annotate('local min', xy=(-1.57, -1), xytext=(-1, -0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
#subplot 2)
plt.subplot(222)
plt.plot(x,np.cos(x),'g')
plt.grid(True)
plt.title(r'$\cos(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.annotate('local max', xy=(0, 1), xytext=(1, 0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
plt.annotate('local min', xy=(-3.14, -1), xytext=(-3, -0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
#subplot 3
plt.subplot(223)
plt.plot(x1,np.tan(x1),'y')
plt.title(r'$tg(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.text (-1, -25, u"HET max u min")
#subplot 4
plt.subplot(224)
plt.plot(c,1/np.tan(c),'r')
plt.title(r'$ctg(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.text (0.5, 10, u"HET max u min")
plt.show()
plt.cla()
print('Bbedute K')
k=input()
if k=='1':
    plt.subplot(211)
    plt.plot(x,np.cos(x),'g')
    plt.grid(True)
    plt.title(r'$\cos(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.annotate('local max', xy=(0, 1), xytext=(1, 0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.annotate('local min', xy=(-3.14, -1), xytext=(-3, -0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.subplot(223)
    plt.plot(x1,np.tan(x1),'y')
    plt.title(r'$tg(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.text (-1, -25, u"HET max u min")
    plt.subplot(224)
    plt.plot(c,1/np.tan(c),'r')
    plt.title(r'$ctg(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.text (0.5, 10, u"HET max u min")
    plt.show()
elif k=='2':
    plt.subplot(211)
    plt.plot(x,np.sin(x))
    plt.title(r'$\sin(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.annotate('local max', xy=(1.57, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.annotate('local min', xy=(-1.57, -1), xytext=(-1, -0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.subplot(223)
    plt.plot(x1,np.tan(x1),'y')
    plt.title(r'$tg(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.text (-1, -25, u"HET max u min")
    plt.subplot(224)
    plt.plot(c,1/np.tan(c),'r')
    plt.title(r'$ctg(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.text (0.5, 10, u"HET max u min")
    plt.show()
elif k=='3':
    plt.subplot(211)
    plt.plot(x,np.sin(x))
    plt.title(r'$\sin(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.annotate('local max', xy=(1.57, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.annotate('local min', xy=(-1.57, -1), xytext=(-1, -0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.subplot(223)
    plt.plot(x,np.cos(x),'g')
    plt.grid(True)
    plt.title(r'$\cos(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.annotate('local max', xy=(0, 1), xytext=(1, 0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.annotate('local min', xy=(-3.14, -1), xytext=(-3, -0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.subplot(224)
    plt.plot(c,1/np.tan(c),'r')
    plt.title(r'$ctg(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.text (0.5, 10, u"HET max u min")
    plt.show()
elif k=='4':
    plt.subplot(211)
    plt.plot(x,np.sin(x))
    plt.title(r'$\sin(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.annotate('local max', xy=(1.57, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.annotate('local min', xy=(-1.57, -1), xytext=(-1, -0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.subplot(223)
    plt.plot(x,np.cos(x),'g')
    plt.grid(True)
    plt.title(r'$\cos(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.annotate('local max', xy=(0, 1), xytext=(1, 0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.annotate('local min', xy=(-3.14, -1), xytext=(-3, -0.5), arrowprops=dict(facecolor='black', shrink=0.01),)
    plt.subplot(224)
    plt.plot(x1,np.tan(x1),'y')
    plt.title(r'$tg(x)$')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.text (-1, -25, u"HET max u min")
    plt.show()
