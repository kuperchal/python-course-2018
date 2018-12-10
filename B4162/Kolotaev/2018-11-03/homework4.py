#расчет детерминанта квадратной матрицы
class sip:
    def __init__(self, a):
        self.a = a
     #показывает  массив   
    def show(self):
     print(self.a)
    #нахождение детерминанта
    def det(self):
     s = len(self.a)
     #если матрица 2х2
     if s == 2:
      print(self.a[0][0]*self.a[1][1]-self.a[0][1]*self.a[1][0])
      #остальные случаи
     else:
       
        #этот цикл создает новый массив, который является "удвоенной версией" оригинала,
        #чтобы, при перемножении значений диагоналей при выходе за границы матрицы, возвращаться к началу матрицы
        z = self.a
        for i in range (len(self.a)):
            for j in range (len(self.a[i])):
                newel = self.a[i][j]
                z[i].append(newel)
        outf = 0
        out = 0
        i = 0
        #перемножение значений в диагоналях и последующее их сложение
        for j in range (len(self.a)+1):
            outf = outf + out
            out = 1
            for k in range(len(self.a)):
             out = out*z[i+k][j+k]
        outm = 0
        out = 0
        #перемножение значений в диагоналях и последующее их вычитание
        for j in range ((len(self.a))*2 - 1, len(self.a)-2, -1):
            outm = outm + out
            out = 1
            for k in range(len(self.a)):
                out = out*z[i+k][j-k]
        
        print(outf-outm)
        
b = sip([[1, 2, 3], [9, 5, 6], [4, 5, 6]])
b.show()
b.det()