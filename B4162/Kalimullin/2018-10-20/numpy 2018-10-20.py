# def concatenate(a1,a2,k) - Метод конкатинейт. Присоединение массивов по какой-либо существующей оси.
#Соединяем массивы в столбик при k=0 через создание пустого списка и прохождению по элементам массивов.
#Присоединяем к массиву а1 транспонированный массив а2 при k=1 через пустой список и прохождению по элементам подмассива
#и элементам массива.
#Соединяем массивы в строку при k=2.
# def mm(a,word) - Объединеный метод максимума и минимума. Нахождение максимума или минимума в массиве через перебор,
#принимая за минимальный или максимальный 1ый элемент массива.
# def repeat(a,x) - Метод повтора. Проходим через каждый элемент подмассива и добавляем его X-раз.
class Kokoc:
    def __init__(self,array):
        self.array=array
        self.column=len(array[0])
        self.ros=len(array)

    def concatenate(a1,a2,k):
        if k==0:
            if len(a1.array[0])==len(a2.array[0]):
                b=[]
                for i in range (len(a1.array)):
                    b.append(a1.array[i])
                for i in range (len(a2.array)):
                    b.append(a2.array[i])

                return b
        if k==1:

            if len(a1.array)==len(a2.array[0]):
                b=[]
                for i in range (len(a1.array)):
                    c=[]
                    for t in range (len(a1.array[i])):
                        c.append(a1.array[i][t])
                    for j in range (len(a2.array)):
                        c.append(a2.array[j][i])
                    b.append(c)

                return b

        if k==2:
            if len(a1.array)==len(a2.array[0]):
                b=[]
                for i in range (len(a1.array)):
                    for t in range (len(a1.array[i])):
                        b.append(a1.array[i][t])
                for i in range (len(a2.array)):
                    for j in range (len(a2.array[i])):
                        b.append(a2.array[i][j])

                return b

    def mm(a,word):

        if word=='min':
            m=a.array[0][0]
            for i in range (len(a.array)):
                for j in range (len(a.array[0])):
                    if a.array[i][j]<=m:
                        m=a.array[i][j]
            print('\n')
            return m
        if word=='max':
            m=a.array[0][0]
            for i in range (len(a.array)):
                for j in range (len(a.array[0])):
                    if a.array[i][j]>=m:
                        m=a.array[i][j]
            print('\n')
            return m

    def repeat(a,x):
        b=[]
        for i in range (len(a.array)):
            for j in range (len(a.array[0])):
                for t in range (x):
                    b.append(a.array[i][j])
        print('\n')
        return b

a1=Kokoc([[1,2,3],
          [4,5,6],
          [7,8,9]])

a2=Kokoc([[11,12,13],
          [14,15,16],
          [17,18,19]])
b=Kokoc.concatenate(a1,a2,0)
print(b)
c=Kokoc.mm(a2,'min')
print(c)
k=Kokoc.repeat(a1,2)
print(k)
