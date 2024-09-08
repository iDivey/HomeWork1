from matplotlib import pyplot as plt
import numpy as np
from random import randint


l1 = []
len_ = 15


while len(l1) < len_:
    a = randint(0, 1000)
    l1.append(a)
print(f'Случайный список: {l1}')


num1 = l1[len_ - 1]
num2 = l1[0]
while num1 < num2:
    num1 += 1234


random_arr = (num1 - num2 * np.random.random_sample((len_,)) + num2)
print(f'Случайный маcсив: {random_arr}')
l1_arr = np.array(l1)
l2_arr = l1_arr + random_arr
print(f'Наш рабочий массив из суммы предыдущих: {l2_arr}')
print(f'Его стандартное отклонение: {l2_arr.std()}, медиана массива: {np.median(l2_arr)}')
print(f'Все значения массива в квадрате: {l2_arr ** 2}')
matrix = l2_arr.reshape(3,5)
print(f'Матрица из массива:')
print(f'{matrix}')

p = 0
while p != 2:
    matrix = np.delete(matrix, 1, axis=1)
    p += 1
print(f'Сокращаем матрицу для визуализации:')
print(f'{matrix}')


fig, ax = plt.subplots()
x = matrix[0]
y = matrix [1]
z = matrix [2]
ax.plot(x, y)
ax.plot(x, z)
plt.show()

