#в списке значений поменять левую и правую половину местами
a = [1,5,3,4,2,5]
#количество элементов в списке деленное на 2
length2 = int (len(a)/2)
for i in range(length2):
  #временная перменная
  t = a[i]
  a[i] = a[length2+i]
  a[length2+i] = t
print(a)