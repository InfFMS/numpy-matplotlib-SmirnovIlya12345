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
print('Enter the number of steps')
fig, ax = plt.subplots()
x=y=20
length=int(input())
data=np.zeros((41,41))
c0=c1=c2=c3=0
for i in range(length):
    ra=randint(0,3)
    if ra==0:
        ax.plot([x,x], [y,y+1], label="0")
        y=y+1
        c0+=1
    if ra==1:
        ax.plot([x,x], [y,y-1], label="1")
        y=y-1
        c1+=1
    if ra==2:
        ax.plot([x,x+1], [y,y], label="2")
        x=x+1
        c2+=1
    if ra==3:
        ax.plot([x,x-1], [y,y], label="3")
        x=x-1
        c3+=1
print('The number of steps to the right, left, up and down accordingly:', c0,c1,c2,c3)
plt.imshow(data, cmap='bwr')
plt.colorbar(label="")
plt.show()