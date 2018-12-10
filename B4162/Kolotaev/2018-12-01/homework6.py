

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

x = np.arange(-10, 10.01, 0.01)  # от -10 до 10.01 с шагом 0.01 



fig, ax = plt.subplots(2, 2, figsize=(8,8), sharex=False, squeeze=False)
                                # sharex и squeeze задает разные оси для разных графиков
                                

#график синуса 
ss = np.sin(x)
maxInd = argrelextrema(ss, np.greater) #поиск локального максимума
r = ss[maxInd]
for i in range(len(r)): #поиск координаты х для максимума
    for k in range(len(x)):
        if r[i] == np.sin(x[k]):
            #ax[0,0].plot(x[k], r[i], marker='o') для варианта с точкой
            ax[0,0].annotate('local max', xy=(x[k], r[i]), xytext=(x[k]+1, r[i]-0.5),
            arrowprops=dict(facecolor='black', shrink=2)) #стрелочка
ax[0,0].plot(x, ss,'r')     
ax[0,0].set_title('y=sin(x)') 






#maxInd = argrelextrema(a, np.greater)
#r = a[maxInd]

#график косинуса
ss = np.cos(x)
maxInd = argrelextrema(ss, np.greater)
r = ss[maxInd]
for i in range(len(r)):
    for k in range(len(x)):
        if r[i] == np.cos(x[k]):
            #ax[0,1].plot(x[k], r[i], marker='o')
            ax[0,1].annotate('local max', xy=(x[k], r[i]), xytext=(x[k]+1, r[i]-0.5),
            arrowprops=dict(facecolor='black', shrink=2))
ax[0,1].plot(x, np.cos(x), 'g') 
ax[0,1].grid(True)              
ax[0,1].set_title('y=cos(x)') 


#график тангенса
ss = np.tan(x)
maxInd = argrelextrema(ss, np.greater)
r = ss[maxInd]
for i in range(len(r)):
    for k in range(len(x)):
        if r[i] == np.tan(x[k]):
            #ax[1,0].plot(x[k], r[i], marker='o')
            ax[1,0].annotate('local max', xy=(x[k], r[i]), xytext=(-5+i, -5+i),
            arrowprops=dict(facecolor='black', shrink=2))
ax[1,0].plot(x, np.tan(x), 'b') 
ax[1,0].set_title('y=tan(x)') 
ax[1,0].axis([-3*np.pi, 3*np.pi, -10, 10]) #"развертвывает" график, коэффициенты при pi влияют на частоту функции на графике,
# а десятки - высота графика (если поставить высоты по 1000, то можно увидеть стрелочки на экстремумах функции)
                                

#график котангенса 
ss = 1/np.tan(x)
maxInd = argrelextrema(ss, np.greater)
r = ss[maxInd]
for i in range(len(r)):
    for k in range(len(x)):
        if r[i] == 1/np.tan(x[k]):
            ax[1,1].plot(x[k], r[i], marker='o')
            ax[1,1].annotate('local max', xy=(x[k], r[i]), xytext=(-5+i, -5+i),
            arrowprops=dict(facecolor='black', shrink=2))
ax[1,1].plot(x, 1/np.tan(x), 'k') 
ax[1,1].set_title('y=ctg(x)') 
ax[1,1].axis([-3.5*np.pi, 3.5*np.pi, -10, 10]) #cм. график тангенса
ax[1,1].grid(True)  

  #подписи оси у      
ax[0, 0].set_ylabel("y")
ax[1, 0].set_ylabel("y")

# распределение графика по области с отступами
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.4, hspace=0.2)




    
plt.show()

