import pandas as pd
import matplotlib.pyplot as plt
table = pd.read_excel('kri.xlsx')
x = table.values[:, 0][::3]                     #определение столбца и сглаживание
y = table.values[:, 1][::3]
y1 = table.values[:, 2][::3]
plt.figure(figsize=(10, 6))
#поиск максимума
maxGR = max(y)                      #максимальное значение по игрик
for i in range(len(y)):             #находим номер ячейки с этим значением
    if y[i]== maxGR:
        numbmaxGR=i        
xGR=x[numbmaxGR]                    #находим значение по иксу в ячейке с тем же номером
#поиск минимума
minGR = min(y)                      
for i in range(len(y)):
    if y[i]== minGR:
        numbminGR=i       
x1GR=x[numbminGR]
#поиск максимума
maxGRST = max(y1) 
for i in range(len(y1)):
    if y1[i]== maxGRST:
         numbmaxGRST=i       
xGRST=x[numbmaxGRST]
#поиск минимума
minGRST = min(y1) 
for i in range(len(y1)):
    if y1[i]== minGRST:
        numbminGRST=i      
x1GRST=x[numbminGRST]
#постороение спектров
plt.plot(x, y, 'r', x, y1, 'b')
plt.annotate('local max', xy=(xGR, maxGR), xytext=(2700, 0.14),      #локальный максимум
            arrowprops=dict(facecolor='#ffb20a', shrink=5.01)) 

plt.plot(x, y, 'r', x, y1, 'b')
plt.annotate('local min', xy=(x1GR, minGR), xytext=(1000, 0.025),      #локальный минимум
            arrowprops=dict(facecolor='#ffb20a', shrink=5.01)) 
plt.plot(x, y, 'r', x, y1, 'b')                           
plt.annotate('local max', xy=(xGRST, maxGRST), xytext=(1000, 0.177),      #локальный максимум
            arrowprops=dict(facecolor='#ffb20a', shrink=5.01))     
                            
plt.plot(x, y, 'r', x, y1, 'b')
plt.annotate('local min', xy=(x1GRST, minGRST), xytext=(3500, 0.025),      #локальный минимум
            arrowprops=dict(facecolor='#ffb20a', shrink=5.01))

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
plt.annotate('local min', xy=(x1GR, minGR), xytext=(1600, 0.02),      #локальный минимум
            arrowprops=dict(facecolor='#ffb20a', shrink=5.01)) 

plt.title("частичный спектр")
plt.xlabel("частота")
plt.ylabel("поглощение")
lgnd = plt.legend(['графен', 'графен в жидком стекле'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('#ffb19a')

plt.show()