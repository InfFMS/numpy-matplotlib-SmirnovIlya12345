# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
import matplotlib.pyplot as plt
from random import randint
import numpy as np
fig, ax = plt.subplots()
rows=int(input())
files=int(input())
data=np.zeros((rows,files))
numberz=np.zeros((rows,files))
for i in range(int(input())):
    while True:
        a=randint(0,rows-1)
        b=randint(0,files-1)
        if data[a,b]!=-1:
            data[a,b]=-1
            circle=plt.Circle((b,a), 0.5, color="green", label="Окружность")
            ax.add_patch(circle)
            break
for i in range(rows):
    for j in range(files):
        if i!=0 and j!=0:
            numberz[i,j]+=data[i-1,j-1]
        if i!=0:
            numberz[i,j]+=data[i-1,j]
        if i!=0 and j!=files-1:
            numberz[i,j]+=data[i-1,j+1]
        if j!=0:
            numberz[i,j]+=data[i,j-1]
        if j!=files-1:
            numberz[i,j]+=data[i,j+1]
        if i!=rows-1 and j!=0:
            numberz[i,j]+=data[i+1,j-1]
        if i!=rows-1:
            numberz[i,j]+=data[i+1,j]
        if i!=rows-1 and j!=files-1:
            numberz[i,j]+=data[i+1,j+1]
plt.imshow(data, cmap='hot')
plt.colorbar(label="")
plt.title("data")
plt.imshow(numberz, cmap='hot')
plt.colorbar(label="")
plt.title("numberz")
plt.show()
plt.show()
