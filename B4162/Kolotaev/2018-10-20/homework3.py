

class sp:
 def __init__(self, a):
   self.a = a
  #заполняет матрицу выбранным значением
 def fill(self, ch):
   self.ch = ch
   for i in range(len(self.a)):
     for j in range(len(self.a[i])):
       self.a[i][j] = self.ch 
  #выводит матрицу
 def show(self):
    print(self.a)
  #выводит размерность матрицы
 def shape(self):
   stro = len(self.a)
   stolb = len(self.a[0])
   print(stro, stolb)
  #ищет выбранное значение в матрице. Если находит выводит True
 def search(self, ch):
   tr = 0
   for i in range(len(self.a)):
     for j in range(len(self.a[i])):
       if self.a[i][j] == ch:
         tr = 1
   if tr == 0:
     print('False')
   else:
     print('True')
  #конвертация двухмерного массива в одномерный
 def flatten(self):   
   z = []
   for i in range(len(self.a)):
     for j in range(len(self.a[i])):
       newelement = self.a[i][j]
       z.append(newelement)
   self.a = z
  #транспонирование матрицы
 def trans(self):
    transposed = [None]*len(self.a[0])
    for i in range(len(self.a)):
        transposed[i] = [None]*len(self.a)
        for j in range(len(self.a[i])):
            transposed[i][j] = self.a[j][i]
    self.a = transposed

    



print('массив принадлежащий моему классу')
b = sp([[1, 2, 3.3, 4], [5, 6, 7, 7], [7, 8, 9, 9]])
b.show()
print('размерность матрицы')
b.shape()
print('поиск значения 8')
b.search(8)
print('поиск значения 11')
b.search(11)
print('заполнение массива значениемм 6')
b.fill(6)
b.show()
print('конвертация в одномерный массив')
b.flatten()
b.show()
print('новый массив')
c = sp([[5, 3, 2], [9, 8, 0], [3, 6, 9]])
c.show()
print('транспонированный массив')
c.trans()
c.show()