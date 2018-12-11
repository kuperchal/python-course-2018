class mass:
 def __init__(self, m):
   self.m = m
   #выводит массив
 def show(self):
    print(self.m)
   #сортировка от меньшего к большему для строк массива
 def sortt(self):
     for i in range(len(self.m)):
      self.m[i].sort() 
  #выводит уникальные элементы строк массива
 def uniq(self):   
   z = []                                #объединение строк матрицы (двумерного массива) в одну строку (одномерный массив)
   for i in range(len(self.m)):
     for j in range(len(self.m[i])):
       newelement = self.m[i][j]
       z.append(newelement)
   a = set(z) 
   print(a)
  #выводит элемент с максимальным значением
 def maximal (self):
     self.mx = self.m[0][0]
     for i in range(len(self.m)):
      for j in range(len(self.m[i])):
       if  self.m[i][j] > self.mx:
              self.mx = self.m[i][j]
     print(self.mx)
  #выводит элемент с минимальным значением
 def minimal (self):
     self.ms = self.m[0][0]
     for i in range(len(self.m)):
         for j in range(len(self.m[i])):
          if self.ms > self.m[i][j]:
              self.ms = self.m[i][j]
     print(self.ms)
    
b = mass([[-9, -33, -2, -3, -5, -5, -800],[ -9, -3, -1, -2, -11, -7, 263, -6, -4, -9]])
b.show()
b.sortt()
b.show()
b.uniq()
b.maximal()
b.minimal()

