import random
import numpy as np
m = random.randint(2, 5)  # столбец
n = random.randint(2, 5)  # строка
list = []
mat = np.random.randint(0, 15, (m, n))  # столбец, строка
print(mat)
col_mtx = tuple(zip(*mat)) # разбиваем матрицу на столбцы
col_sum = tuple(map(lambda col: sum(map(abs, col)), col_mtx)) # ищем максимальную
# сумму абсолютных значений столбцов
g = max(col_mtx[col_sum.index(max(col_sum))]) # получаем максимальный элемент
# столбца с максимальной суммой
list.append(g)
for i in range(0,n):
    list.append(" ")
del(list[-1])
new_row = np.array(list)
mat = np.vstack([mat, new_row]) # склеивание матрицы с результатом обработки
np.savetxt('test_3.txt', mat, fmt="%.18s") # сохранение файла
print("Наибольшее число из суммы абсолютных значений стобца: ",g)