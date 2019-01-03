class np:
    def __init__(self, arr):
        self.arr = arr

    def display(self):      #Метод выводит матрицу в консоль
        for i in range(len(self.arr)):
            print("[", end='')
            for j in range(len(self.arr[0])):
                print(self.arr[i][j], end=" ")
            print("]")

    def size(self):     #Реализация метода numpy.size(подсчет элементов в матрице)
        return len(self.arr[0])*len(self.arr)       #Возвращает число столцов перемноженное на число строк

    def reshape(self, a, b):        #Реализация метода numpy.reshape (разбиение однострочной матрицы на матрицу размерности (a,b))
        if (a * b == len(self.arr)):        #Проверка на соответствие размера начальной и конечной матриц
            res = []        #Создание резервной матрица, значение которой позже присвоим классовому полю
            for i in range(a):
                res1 = []       #Создание строчек
                for j in range(b):
                    res1.append(self.arr[(i*b + j)])    #Заполнение строчек
                res.append(res1)    #Добавление строчки конечную матрицу
            self.arr = res
        else:                                       #Ответ в случае неправильного ввода исходных данных
            print('operation is impossible')

    def resize(self, a, b):     #Реализация метода numpy.resize (Переопределение размерности матрицы)
        if (a * b == len(self.arr)*len(self.arr[0])):    #Проверка на соответствие размера начальной и конечной матриц
            res = []        #Создание резервной матрица, значение которой позже присвоим классовому полю
            for i in range(len(self.arr)):
                for j in range(len(self.arr[0])):
                    res.append(self.arr[i][j])      #Преобразование матрицы в однострочную
            self.arr = res
            self.reshape(a, b)      #Вызов фунции разбиения от одностроочной матрицы
        else:       #Ответ в случае неправильного ввода исходных данных
            print('operation is impossible')


numpy = np([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
numpy.reshape(4, 3)
numpy1 = np([[1, 7, 3],
             [4, 5, 6],
             [7, 8, 9],
             [10, 11, 12]])
numpy1.resize(6, 2)
numpy.display()
print('Size of matrix', numpy.size(), '\n')
numpy1.display()
print('Size of matrix', numpy1.size(), '\n')



