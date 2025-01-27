# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import matplotlib.pyplot as plt
import numpy as np
file=int(input())
row=int(input())
fig, ax = plt.subplots()
data = np.array(([0,10,0,10,0,10,0,10],[10,0,10,0,10,0,10,0],[0,10,0,10,0,10,0,10],[10,0,10,0,10,0,10,0],[0,10,0,10,0,10,0,10],[10,0,10,0,10,0,10,0],[0,10,0,10,0,10,0,10],[10,0,10,0,10,0,10,0]))
queen=[row,file]
circle = plt.Circle((row, file), 0.5, color="orange", label="Окружность")
ax.add_patch(circle)
for i in range(8):
    for j in range(8):
        if i==row or j==file:
            circle=plt.Circle((i,j),0.3, color="red", label="Окружность")
            ax.add_patch(circle)
for i in range(row-8, 8-row):
    if file+i<=7 and file+i>=0 and row+i<=7 and row+i>=0:
        circle=plt.Circle((row+i,file+i),0.3,color="red",label="Окружность")
        ax.add_patch(circle)
for i in range(file-100, 100-file):
    if file-i<=7 and file-i>=0 and row+i<=7 and row+i>=0:
        circle=plt.Circle((row+i,file-i),0.3,color="red",label="Окружность")
        ax.add_patch(circle)
data[row,file]=data[row,file]
plt.imshow(data, cmap='hot')
plt.colorbar(label="")
plt.title("Шахматная доска")
plt.show()
