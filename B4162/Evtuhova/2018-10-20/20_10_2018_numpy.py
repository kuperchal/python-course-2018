#класс для работы с матрицей
class Matrix:
  def __init__(self, m):
    self.m = m
    self.x = len(self.m)
    self.y = len(self.m[0])
  #заполнение
  def fill_matrix(self, new_m):
    for i in range(self.x):
      for j in range(self.y):
        self.m[i][j] = new_m[i][j]
  #вывод
  def print_matrix(self):
    for i in range(len(self.m)):
      for j in range(len(self.m[i])):
	    #печатаем текущий элемент без переноса строки end == ''
        print(self.m[i][j] , ", ", end = '')
	  #перенос строки	
      print("")
  #размерность матрицы
  def get_size(self):
    return [self.x, self.y]
  #поиск элемента в матрице
  def search(self, element):
    for i in range(self.x):
      for j in range(self.y):
        if self.m[i][j] == element:
          return "true"
    return "false"
  #сумма всех элементов матрицы
  def sum_matrix(self):
    s = 0
    for i in range(self.x):
      for j in range(self.y):
        s = s + self.m[i][j]
    return s
  #транспонирование матрицы
  def transpose(self):
    #создаем копию текущий матрицы
    temp_m = self.m
    for i in range(self.x):
      for j in range(self.y):
        self.m[i][j] = temp_m[j][i]
#создаем экземпляр класса матрица и заполняем его
m = Matrix([[1,2,3],[4,5,6],[7,8,9]])
#выводим
m.print_matrix()
#заполнить матрицу другими значениями
m.fill_matrix([[10,20,30],[40,50,60],[70,80,90]])
m.print_matrix()
print("Размерность матрицы:", m.get_size())
#поиск элемента 20 в матрице
print(m.search(20))
print("Сумма всех элементов матрицы : ", m.sum_matrix())
#транспонируем матрицу
m.transpose()
m.print_matrix()