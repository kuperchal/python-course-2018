import pandas as pd
import matplotlib.pyplot as plt
table = pd.read_excel('kri.xlsx')
x = table.values[:, 0][::3]                     #определение столбца и сглаживание
y = table.values[:, 1][::3]
y1 = table.values[:, 2][::3]
plt.figure(figsize=(10, 6))

#поиск максимума
def maxx(gr):
 maxGR = max(gr)                      #максимальное значение по игрик
 for i in range(len(gr)):             #находим номер ячейки с этим значением
    if gr[i]== maxGR:
        numbmaxGR=i        
        xGR=x[numbmaxGR]                #находим значение по иксу в ячейке с тем же номером
        plt.annotate('local max', xy=(xGR, maxGR), xytext=(2700, 0.14),      
            arrowprops=dict(facecolor='#ffb20a', shrink=5.01))
                            
#поиск минимума
def minn(gr):
 minGR = min(gr)                      
 for i in range(len(gr)):
    if gr[i]== minGR:
        numbminGR=i       
        x1GR=x[numbminGR]
        plt.annotate('local min', xy=(x1GR, minGR), xytext=(1000, 0.025),      
            arrowprops=dict(facecolor='#ffb20a', shrink=5.01)) 

#постороение спектров
plt.plot(x, y, 'r', x, y1, 'b')
maxx(y)
minn(y) 
maxx(y1)
minn(y1)



plt.title("полный спектр")
plt.xlabel("частота")
plt.ylabel("поглощение")
lgnd = plt.legend(['графен', 'графен в жидком стекле'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('#ffb19a')

plt.show()

#обрезаный график с важной информацией
a = table.values[:, 0][::3]                     #определение столбца и сглаживание
b = table.values[:, 3][::3]
b1 = table.values[:, 4][::3]
plt.figure(figsize=(10, 6))
                    
                        
plt.plot(a, b, 'r', a, b1, 'b')
minn(y)                                         #локальный минимум

plt.title("частичный спектр")
plt.xlabel("частота")
plt.ylabel("поглощение")
lgnd = plt.legend(['графен', 'графен в жидком стекле'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('#ffb19a')

plt.show()