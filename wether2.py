# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
# Чуть более реалистичная версия :)
from random import randint
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,365,365)
y=[]
for i in range(365):
    y.append(randint(-3,18))
y2=[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*30+[randint(-5,5)]*35
z=-15*np.cos(x/61)+(y)+(y2)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, z)
axs[0].set_xlabel("Days")
axs[0].set_ylabel("Temperature")
plt.show()
plt.bar(x, z, color='blue')
plt.show()