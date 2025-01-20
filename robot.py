# Описание задачи:
# Робот начинает своё движение из точки (0,0) на координатной плоскости. Его маршрут задаётся массивом из 100 случайных значений, где:1 — движение вверх.2 — движение вниз.3 — движение вправо.4 — движение влево.
# Ваша задача:
# Сымитировать маршрут робота, используя случайные числа.
# Найти конечное положение робота.
# Построить путь робота на графике (соединяя все пройденные точки).
# Подсчитать, сколько шагов робот сделал в каждую сторону.
# Определить расстояние от начальной точки до конечной.
import matplotlib.pyplot as plt
from random import randint
import numpy as np
fig, ax = plt.subplots()
x=y=5
length=int(input())
data=np.zeros((10,10))
for i in range(length):
    ra=randint(0,3)
    if ra==0:
        ax.plot([x,y], [x,y+1], label="")
        y+=1
    if ra==1:
        ax.plot([x,y], [x,y-1], label="")
        y-=1
    if ra==2:
        ax.plot([x,y], [x+1,y], label="")
        x+=1
    if ra==3:
        ax.plot([x,y], [x-1,y], label="")
        x-=1
plt.imshow(data, cmap='bwr')
plt.colorbar(label="")
plt.title("Шахматная доска")
plt.show()