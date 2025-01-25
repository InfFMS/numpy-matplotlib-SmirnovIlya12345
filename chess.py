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
circle = plt.Circle((file, row), 0.5, color= "white", label="Окружность")
ax.add_patch(circle)
data[:,file]=data[:,file]=4
data[row,:]=data[row,:]=4
for i in range(row-8, 8-row):
    if file+i<=7 and file+i>=0 and row+i<=7 and row+i>=0:
        data[row+i,file+i]=data[row+i,file+i]=4
for i in range(file-100, 100-file):
    if file-i<=7 and file-i>=0 and row+i<=7 and row+i>=0:
        data[row+i,file-i]=data[row+i,file-i]=4
data[row,file]=data[row,file]
plt.imshow(data, cmap='hot')
plt.colorbar(label="")
plt.title("Шахматная доска")
plt.show()
