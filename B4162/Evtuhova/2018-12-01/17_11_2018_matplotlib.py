import numpy as np
import matplotlib.pyplot as plt

xyz = np.arange(-25, 25, 0.025)
xyzt = np.arange(-1.25, 1.25, 0.025)
xyzct = np.arange(-2.5, 2.5, 0.25)

#4 пустых графика]
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10), dpi=100, facecolor='white', frameon=True, edgecolor='lightblue', linewidth=4)
#отступы
fig.subplots_adjust(wspace=0.5, hspace=0.5, left=0.1, right=0.90, top=0.90, bottom=0.2)

#sinus 1
axes[0,0].plot(xyz, np.sin(xyz), color='green')
axes[0,0].grid(True, c='lightblue', alpha=0.5)
axes[0,0].set_title('sin(x)', fontsize=12)
axes[0,0].set_xlabel('x', fontsize=8)
axes[0,0].set_ylabel('y=sin(x)', fontsize=8)
axes[0,0].annotate('local max', xy=(1.57, 1), xytext=(3.5, 0.5), arrowprops=dict(facecolor='black', shrink=0.01))
axes[0,0].annotate('local min', xy=(-1.57, -1), xytext=(1, -0.5), arrowprops=dict(facecolor='black', shrink=0.01))

#cosinus 2
axes[0,1].plot(xyz, np.cos(xyz), color='red')
axes[0,1].grid(True, c='lightblue', alpha=0.5)
axes[0,1].set_title('cos(x)', fontsize=12)
axes[0,1].set_xlabel('x', fontsize=8)
axes[0,1].set_ylabel('y=cos(x)', fontsize=8)
axes[0,1].annotate('local max', xy=(0, 1), xytext=(2, 0.5), arrowprops=dict(facecolor='black', shrink=0.01))
axes[0,1].annotate('local min', xy=(-3.14, -1), xytext=(-1.5, -0.5), arrowprops=dict(facecolor='black', shrink=0.01))

#tangens 3
axes[1,0].plot(xyzt, np.tan(xyzt), color='brown')
axes[1,0].set_title('tg(x)', fontsize=12)
axes[1,0].set_xlabel('x', fontsize=8)
axes[1,0].set_ylabel('y=tg(x)', fontsize=8)

#cotangens 4
axes[1,1].plot(xyzct, 1/np.tan(xyzct), color='blue')
axes[1,1].set_title('ctg(x)', fontsize=12)
axes[1,1].set_xlabel('x', fontsize=8)
axes[1,1].set_ylabel('y=ctg(x)', fontsize=8)
plt.show()

a = input('Input separate: ')
if a == 'separate':
    #sinus 1
    plt.plot(xyz, np.sin(xyz), color='green')
    plt.grid(True, c='lightblue', alpha=0.5)
    plt.title('sin(x)', fontsize=12)
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y=sin(x)', fontsize=8)
    plt.annotate('local max', xy=(1.57, 1), xytext=(3.5, 0.5), arrowprops=dict(facecolor='black', shrink=0.01))
    plt.annotate('local min', xy=(-1.57, -1), xytext=(1, -0.5), arrowprops=dict(facecolor='black', shrink=0.01))
    plt.show()
    
    #cosinus 2
    plt.plot(xyz, np.cos(xyz), color='red')
    plt.grid(True, c='lightblue', alpha=0.5)
    plt.title('cos(x)', fontsize=12)
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y=cos(x)', fontsize=8)
    plt.annotate('local max', xy=(0, 1), xytext=(2, 0.5), arrowprops=dict(facecolor='black', shrink=0.01))
    plt.annotate('local min', xy=(-3.14, -1), xytext=(-1.5, -0.5), arrowprops=dict(facecolor='black', shrink=0.01))
    plt.show()
    
    #tangens 3
    plt.plot(xyzt, np.tan(xyzt), color='brown')
    plt.title('tg(x)', fontsize=12)
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y=tg(x)', fontsize=8)
    plt.show()
    
    #cotangens 4
    plt.plot(xyzct, 1/np.tan(xyzct), color='blue')
    plt.title('ctg(x)', fontsize=12)
    plt.xlabel('x', fontsize=8)
    plt.ylabel('y=ctg(x)', fontsize=8)
    plt.show()    