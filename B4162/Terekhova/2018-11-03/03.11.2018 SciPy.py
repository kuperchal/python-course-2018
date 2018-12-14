class Sci:
    def __init__(self,array):
        self.array=array
        self.column=len(array[0])
        self.ros=len(array)

    def dot(a1,a2):
        if len(a1.array[0])==len(a2.array):
            b = []
            for i in range (len(a1.array)):
                b.append([])
                for j in range (len(a2.array[0])):
                    b[i].append(0)

            for i in range (len(a1.array)):
                for j in range (len(a1.array[0])):
                    for k in range(len(a2.array)):
                        for l in range (len(a2.array[0])):
                            if(j==k):
                                b[i][l]+=a1.array[i][j]*a2.array[k][l]

            return b
        else:
            print('Prou3BedeHue He Bo3MoIIIHo')

a1=Sci([[2,0,4,-1],
        [1,-1,1,0]])
a2=Sci([[2],
        [1],
        [0],
        [-2]])
b=Sci.dot(a1,a2)
print(b)
