


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

x = np.arange(-10, 10.01, 0.01)  # от -10 до 10.01 с шагом 0.01 



fig, ax = plt.subplots(2, 2, figsize=(8,8), sharex=False, squeeze=False)
                                # sharex и squeeze задает разные оси для разных графиков
                                

#график синуса 
def sin(n, m):                               
 ss = np.sin(x)
 maxInd = argrelextrema(ss, np.greater) #поиск локального максимума
 r = ss[maxInd]
 for i in range(len(r)): #поиск координаты х для максимума
    for k in range(len(x)):
        if r[i] == np.sin(x[k]):
            #ax[0,0].plot(x[k], r[i], marker='o') для варианта с точкой
            ax[n,m].annotate('local max', xy=(x[k], r[i]), xytext=(x[k]+1, r[i]-0.5),
            arrowprops=dict(facecolor='black', shrink=2)) #стрелочка
 ax[n,m].plot(x, ss,'r')     
 ax[n,m].set_title('y=sin(x)') 
sin(0, 0)




#график косинуса
def cos(n, m):
 ss = np.cos(x)
 maxInd = argrelextrema(ss, np.greater)
 r = ss[maxInd]
 for i in range(len(r)):
    for k in range(len(x)):
        if r[i] == np.cos(x[k]):
            #ax[0,1].plot(x[k], r[i], marker='o')
            ax[n,m].annotate('local max', xy=(x[k], r[i]), xytext=(x[k]+1, r[i]-0.5),
            arrowprops=dict(facecolor='black', shrink=2))
 ax[n,m].plot(x, np.cos(x), 'g') 
 ax[n,m].grid(True)              
 ax[n,m].set_title('y=cos(x)') 
cos(0,1)

#график тангенса
def tan(n, m):
 ss = np.tan(x)
 maxInd = argrelextrema(ss, np.greater)
 r = ss[maxInd]
 for i in range(len(r)):
    for k in range(len(x)):
        if r[i] == np.tan(x[k]):
            #ax[1,0].plot(x[k], r[i], marker='o')
            ax[n,m].annotate('local max', xy=(x[k], r[i]), xytext=(-5+i, -5+i),
            arrowprops=dict(facecolor='black', shrink=2))
 ax[n,m].plot(x, np.tan(x), 'b') 
 ax[n,m].set_title('y=tan(x)') 
 ax[n,m].axis([-3*np.pi, 3*np.pi, -10, 10]) #"развертвывает" график, коэффициенты при pi влияют на частоту функции на графике,
# а десятки - высота графика (если поставить высоты по 1000, то можно увидеть стрелочки на экстремумах функции)
tan(1, 0)                               

#график котангенса 
def ctg(n, m):
 ss = 1/np.tan(x)
 maxInd = argrelextrema(ss, np.greater)
 r = ss[maxInd]
 for i in range(len(r)):
    for k in range(len(x)):
        if r[i] == 1/np.tan(x[k]):
            ax[n,m].plot(x[k], r[i], marker='o')
            ax[n,m].annotate('local max', xy=(x[k], r[i]), xytext=(-5+i, -5+i),
            arrowprops=dict(facecolor='black', shrink=2))
 ax[n,m].plot(x, 1/np.tan(x), 'k') 
 ax[n,m].set_title('y=ctg(x)') 
 ax[n,m].axis([-3.5*np.pi, 3.5*np.pi, -10, 10]) #cм. график тангенса
 ax[n,m].grid(True)  
ctg(1,1)
  #подписи оси у      
ax[0, 0].set_ylabel("y")
ax[1, 0].set_ylabel("y")

# распределение графика по области с отступами
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.4, hspace=0.2)



plt.show()

#вывод в определенном порядке

zzz = []
for i in range(4):
    zzz.append(int(input()))
    
fig, ax = plt.subplots(2, 2, figsize=(8,8), sharex=False, squeeze=False)
l=0
u=0
ind = 0

for l in range(2):
 for u in range(2):
         if zzz[ind] == 1:
          cos(l,u)
         elif zzz[ind] == 2:
          sin(l,u)
         elif zzz[ind] == 3:
          tan(l,u)
         elif zzz[ind] == 4:
          ctg(l,u)
         ind=ind+1
        
 plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.4, hspace=0.2)
plt.show()

