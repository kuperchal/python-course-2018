import copy
import math
class scp:
    def __init__(self, arr):
        self.arr = arr

    def determinant(self):  #Метод основан на рекурсивном дроблении матрицы до того момента, как мы ее сможем вычсилить по формуле(2х2)
        if len(self.arr) != len(self.arr[0]):   #Проверочное условие
            print("need a square matrix")
        else:
            if len(self.arr) == 2:     #Детерминант матрицы (2х2)
                return self.arr[0][0]*self.arr[1][1] - self.arr[1][0]*self.arr[0][1]        #Возвращает значение по формуле
            else:
                result = 0      #Значение детерминанта
                for i in range(len(self.arr)):      #Проход по строчкам родительской матрицы
                    resarr = copy.deepcopy(self.arr)        #Полное копирование изначальной матрицы, для упращения используется метод copy.deepcopy
                    del(resarr[i])      #Удаление строки
                    for j in range(len(resarr)):
                        del(resarr[j][0])       #Удаление столбца
                    result += math.cos(i*math.pi) * self.arr[i][0] * scp(resarr).determinant()      #Рекурсивный вызов функции, перемножение его на отобранный элемент, и переумножение его на чередующийся знак,
                                                                                                    # для упрощения была реализована функция math.cos (как мы знаем cos(PI*n) равен 1 или -1, при n = 0,1,2,3...
                return result


array = [[-3, 4, 4, 3],
         [5, -5, 5, 5],
         [1, 3, -3, 1],
         [7, 5, 5, -7]]
a = scp(array)
print(a.determinant())
