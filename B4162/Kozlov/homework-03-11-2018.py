import numpy as np
from scipy.sparse import issparse, csr_matrix
from numpy.core import Inf, sqrt, abs

def _sparse_frobenius_norm(x):
    if np.issubdtype(x.dtype, np.complexfloating):
        sqnorm = abs(x).power(2).sum()
    else:
        sqnorm = x.power(2).sum()
    return sqrt(sqnorm)


def norm(x, ord=None, axis=None):
    if not issparse(x):
        raise TypeError("Входной параметр не разреженный. Используем numpy.linalg.norm")

    # Сначала проверяем стандартный случай и сразу же обрабатываем его
    if axis is None and ord in (None, 'fro', 'f'):
        return _sparse_frobenius_norm(x)

    # Нормирование некоторых элементов требует функций, которые не реализованы для всех типов.
    x = x.tocsr()

    if axis is None:
        axis = (0, 1)
    elif not isinstance(axis, tuple):
        msg = "'оси' должны быть None, integer или tuple of integers"
        try:
            int_axis = int(axis)
        except TypeError:
            raise TypeError(msg)
        if axis != int_axis:
            raise TypeError(msg)
        axis = (int_axis,)

    nd = 2
    if len(axis) == 2:
        row_axis, col_axis = axis
        if not (-nd <= row_axis < nd and -nd <= col_axis < nd):
            raise ValueError('Неправильная ось %r для массива %r' %
                             (axis, x.shape))
        if row_axis % nd == col_axis % nd:
            raise ValueError('Переданы одинаковые оси.')
        if ord == 1:
            return abs(x).sum(axis=row_axis).max(axis=col_axis)[0,0]
        elif ord == Inf:
            return abs(x).sum(axis=col_axis).max(axis=row_axis)[0,0]
        elif ord == -1:
            return abs(x).sum(axis=row_axis).min(axis=col_axis)[0,0]
        elif ord == -Inf:
            return abs(x).sum(axis=col_axis).min(axis=row_axis)[0,0]
        elif ord in (None, 'f', 'fro'):
            # Порядок оси не имеет значения для этой нормы.
            # https://youtu.be/vfiMx9AOYyM
            return _sparse_frobenius_norm(x)
        else:
            raise ValueError("Неверный порядок нормирования матрицы.")
    elif len(axis) == 1:
        a, = axis
        if not (-nd <= a < nd):
            raise ValueError('Неправильная ось %r для массива %r' %
                             (axis, x.shape))
        if ord == Inf:
            M = abs(x).max(axis=a)
        elif ord == -Inf:
            M = abs(x).min(axis=a)
        elif ord == 0:
            # Нулевая норма
            M = (x != 0).sum(axis=a)
        elif ord in (2, None):
            M = sqrt(abs(x).power(2).sum(axis=a))
        else:
            try:
                ord + 1
            except TypeError:
                raise ValueError('Неверный порядок нормирования векторов.')
            M = np.power(abs(x).power(ord).sum(axis=a), 1 / ord)
        return M.A.ravel()
    else:
        raise ValueError("Неверное количество измерений до нормы.")

# Пример использования (нормируем матрицу)
a = np.arange(9) - 4
b = a.reshape((3, 3))
b = csr_matrix(b)
print(norm(b))
