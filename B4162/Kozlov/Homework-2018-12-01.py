import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

x = np.arange(-10, 10, 0.1) #Задаём диапазон значений для ох для разных графиков
x1 = np.arange(-1.56,1.57,0.05)
x2 = np.arange(0,3.15, 0.1)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,7), dpi=85, facecolor='white',
frameon=True, edgecolor='lightblue', linewidth=4) #Создаём графики
fig.subplots_adjust(wspace=0.4, hspace=0.5, left=0.1, right=0.95, top=0.95, bottom=0.1) #Задаём отступы между графиками, сверху, снизу, по бокам

#First graph
axes[0,0].plot(x, np.sin(x), color='red')
axes[0,0].grid(True, c='lightblue', alpha=0.5)
axes[0, 0].set_title('sin(x)', fontsize=10)
axes[0,0].set_xlabel('x', fontsize=8)
axes[0,0].set_ylabel('y=sin(x)', fontsize=8)
axes[0,0].annotate('local max', xy=(1.57, 1), xytext=(3.5, 0.5), arrowprops=dict(facecolor='black', shrink=0.01))
axes[0,0].annotate('local min', xy=(-1.57, -1), xytext=(1, -0.5), arrowprops=dict(facecolor='black', shrink=0.01))

#Second graph
axes[0,1].plot(x, np.cos(x), color='green')
axes[0,1].grid(True, c='lightblue', alpha=0.5)
axes[0,1].set_title('cos(x)', fontsize=10)
axes[0,1].set_xlabel('x', fontsize=8)
axes[0,1].set_ylabel('y=cos(x)', fontsize=8)
axes[0,1].annotate('local max', xy=(0, 1), xytext=(2, 0.5), arrowprops=dict(facecolor='black', shrink=0.01))
axes[0,1].annotate('local min', xy=(-3.14, -1), xytext=(-1.5, -0.5), arrowprops=dict(facecolor='black', shrink=0.01))

#Third graph
axes[1,0].plot(x1, np.tan(x1), color='green')
axes[1,0].set_title('tg(x)', fontsize=10)
axes[1,0].set_xlabel('x', fontsize=8)
axes[1,0].set_ylabel('y=tg(x)', fontsize=8)

#Fourth graph
axes[1,1].plot(x2, 1/np.tan(x2), color='yellow')
axes[1,1].set_title('ctg(x)', fontsize=10)
axes[1,1].set_xlabel('x', fontsize=8)
axes[1,1].set_ylabel('y=ctg(x)', fontsize=8)
plt.show()
