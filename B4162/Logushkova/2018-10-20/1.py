class strk:
 def __init__(self, m):
   self.m = m
   #выводит строку
 def show(self):
    print(self.m)
   #сортировка от меньшего к большему
 def sortt(self):
      self.m.sort() 
  #выводит уникальные элементы
 def uniq(self):
     a = set(self.m)
     print(a)
  #выводит элемент с максимальным значением
 def maximal (self):
     self.mx = self.m[0]
     for i in range(len(self.m)):
       if  self.m[i] > self.mx:
              self.mx = self.m[i]
     print(self.mx)
  #выводит элемент с минимальным значением
 def minimal (self):
     self.ms = self.m[0]
     for i in range(len(self.m)):
         if self.ms > self.m[i]:
              self.ms = self.m[i]
     print(self.ms)
    
b = strk([-9, -33, -2, -3, -5, -5, -800, -9, -3, -1, -2, -11, -7, 263, -6, -4, -9])
b.show()
b.sortt()
b.show()
b.uniq()
b.maximal()
b.minimal()

