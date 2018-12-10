class Puk:
    def __init__(self,array):
        self.array=array

    def det(self):
        u=0
        if len(self.array)==2:
            k=self.array[0][0]*self.array[1][1]-self.array[0][1]*self.array[1][0]
            return k

        else:
            for i in range(len(self.array)):
                c=self.array[i][0]
                b=[]
                for t in range (len(self.array)):
                    b.append([])
                    for j in range (len(self.array)):
                        b[t].append(self.array[t][j])
                del(b[i])
                for z in range (len(b)):
                     del(b[z][0])
                # print(b)
                # print(c)
                bo = Puk(b)
                if i%2 == 0:
                    w = -1
                else:
                    w = 1
                u += w*c*bo.det()
            return u

arr = [[1,3,5,2],
       [10,9,14,2],
       [2,12,7,15],
       [2,2,7,7]]
test = Puk(arr)
print(test.det())
