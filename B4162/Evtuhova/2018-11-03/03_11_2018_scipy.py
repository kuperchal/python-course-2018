#детерминирование матрицы
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
    for i in range(self.x):
      for j in range(self.y):
        print(self.m[i][j] , ", ", end = '')
      print("")
  #детерминирование квадратной матрицы
  def determinate_square(self,square_matrix):
    if len(square_matrix) == 2 & len(square_matrix[0]) == 2:
      return square_matrix[0][0]*square_matrix[1][1] - square_matrix[0][1]*square_matrix[1][0]
    else:
      return None
  #детерминирование матрицы
  def determinate(self):
    if self.x == 2 & self.y == 2:
      result = self.determinate_square(self.m)
      return result
    elif self.x == 3 & self.y == 3:
      a = self.m[0][0] * self.determinate_square([[self.m[1][1],self.m[1][2]],[self.m[2][1],self.m[2][2]]])
      b = self.m[0][1] * self.determinate_square([[self.m[1][0],self.m[1][2]],[self.m[2][0],self.m[2][2]]])
      c = self.m[0][2] * self.determinate_square([[self.m[1][0],self.m[1][1]],[self.m[2][0],self.m[2][1]]])
      return a - b + c
    else:
      return None
m = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print("Детерминировать матрицу 3*3:")
m.print_matrix()
print(m.determinate())
m2 = Matrix([[1,2],[3,4]])
print("Детерминировать матрицу 2*2:")
m2.print_matrix()
print(m2.determinate())