class num:
    def __init__(self,array):
        self.array=array
        self.column=len(array[0])
        self.ros=len(array)

    def min(a):
        m=a.array[0][0]
        for i in range (len(a.array)):
            for j in range (len(a.array[0])):
                if a.array[i][j]<=m:
                    m=a.array[i][j]
        print('\n')
        return m

    def max(a):
        m=a.array[0][0]
        for i in range (len(a.array)):
            for j in range (len(a.array[0])):
                if a.array[i][j]>=m:
                    m=a.array[i][j]
        print('\n')
        return m

    def mean(a):
        k=1
        z=0
        for i in range(len(a.array)):
            for j in range (len(a.array[0])):
                k=k+1
                z=z+a.array[i][j]
                b=z/k
        print('\n')
        return b

z=num([[1,2],
        [4,5]])
c=num.max(z)
print(c)
i=num.min(z)
print(i)
k=num.mean(z)
print(k)
