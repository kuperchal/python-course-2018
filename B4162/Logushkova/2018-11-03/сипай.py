#Обратная матрица
x = [[3, 5], 
     [-7, 2]]
#обратный детерминант
obr_det= 1/(x[0][0]*x[1][1]-x[0][1]*x[1][0])
#детерминант на транспонированную матрицу для нахождения обратной матрицы
det_na_trans = [[x[1][1]*obr_det, -x[0][1]*obr_det],[-x[1][0]*obr_det, x[0][0]*obr_det]]
print (det_na_trans)