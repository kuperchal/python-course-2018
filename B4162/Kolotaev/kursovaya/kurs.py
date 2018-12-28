from tkinter import *
from tkinter import filedialog as fd



def may():
#выбор загружаемого файла
 fn = fd.askopenfilename()
#ключевые слова для поиска, чтоб вывести только нужные строки в новый документ
 word = 'Kohn-Sham energy differences'
 word2 = 'Sum of osc. strength'
 word3 = 'Fermi (or HOMO) energy (hartree)'
 k=0
 
 z1 = []
 z2 = []
 #создание txt в который будут выгружены нужные мне данные
 f = open('textt.txt', 'w')
 with open(fn, encoding='utf-8') as file:
    for line in file:
        #cчетчик строк
        k += 1
        #поиск номера строки где начинаются столбцы нужных данных
        if word in line:
            z1.append(k)
        #конец данных
        if word2 in line:
            z2.append(k)
        #поиск ключевого числа            
        if word3 in line:
            g = line[37:45]
            kk = k
    k=0
#Вывод нужных данных в отдельный текстовый документ
 with open(fn, encoding='utf-8') as file:    
    for line in file:
        k += 1
        #условие, по которому будут скопированы те строки, которые входят в диапазон 
        #нужных данных
        if (k>z1[0]+3) and (k<z2[0]-1):
         f.write(line[2:21] + '\n')
        if (g in line) and k>kk:
            gg = line
    f.write(gg)
 f.close()

#интерфейс            
w1 = Tk()
w1.title('Извлекатель')
w1.geometry('302x62')
w1.config(bg='blue') 
b1 = Button(text="Выполнить", command=may)
b1.grid(row=1)
w1.mainloop()         

 
       
        
        
            
            

           

        
    
    
            


