import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.01)  # от -10 до 10 с шагом 0.01 
fig = plt.figure()
#subplot 1
plt.subplot(221)            # первая область
plt.plot(x, np.sin(x))      
plt.title('sin(x)')          
plt.annotate('local max', xy=(1.7, 1), xytext=(4, 1.2),      #локальный максимум
            arrowprops=dict(facecolor='pink', shrink=5.01))    
#subplot 2
plt.subplot(222)            # вторая область
plt.plot(x, np.cos(x), 'g') 
plt.grid(True)              # рисовать решетку
plt.title('cos(x)')         
plt.annotate('local min', xy=(3.1, -1), xytext=(4, -1.4),   #локальный минимум
            arrowprops=dict(facecolor='pink', shrink=5.01))
#subplot 3
plt.subplot(223)            # третья область
plt.plot(x, np.tan(x), 'r') 
plt.axis([-2*np.pi, 2*np.pi, -10, 10]) #гррафик в диапазоне +-2Пи
plt.title('tan(x)')                         
#subplot 4
plt.subplot(224)            # четвертая область
plt.plot(x, np.cos(x)/np.sin(x), 'b') 
plt.axis([-2*np.pi, 2*np.pi, -10, 10])
plt.title('ctg(x)')
plt.grid(True)
#редактирование
plt.subplots_adjust(left=0.1, right=0.95, bottom=0.5, top=2, wspace=0.3, hspace=0.3) 
plt.show()
#вывод отдельного графика
a = int (input("для вывода отдельного графика введите цифру: 1 - синус, 2 - косинус, 3 - тангенс, 4 - котангенс:"))
if a == 1:
    plt.figure(figsize=(15, 10))
    plt.plot(x, np.sin(x))
    plt.title('sin(x)') 
    plt.show()
if a== 2:
    plt.figure(figsize=(10, 5))
    plt.plot(x, np.cos(x), 'g')
    plt.grid(True) 
    plt.title('cos(x)')
    plt.show()
if a== 3:
    plt.figure(figsize=(15, 10))
    plt.plot(x, np.tan(x), 'r')
    plt.axis([-2*np.pi, 2*np.pi, -10, 10])
    plt.title('tan(x)')
    plt.show()
if a == 4:
    plt.figure(figsize=(15, 10))
    plt.plot(x, np.cos(x)/np.sin(x), 'b')
    plt.axis([-2*np.pi, 2*np.pi, -10, 10])
    plt.title('ctg(x)')
    plt.grid(True)
    plt.show()