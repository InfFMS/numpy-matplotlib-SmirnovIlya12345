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
from random import randint
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,365,365)
y=[]
hot=cold=maxcold=y_10=y_5=y0=y5=y10=y15=y20=y25=y30=0
for i in range(365):
    y2=randint(-10,35)
    y.append(y2)
    if y2>25:
        hot+=1
for i in range(len(y)):
    if y[i]>=30:
        y30+=1
    elif y[i]>=25:
        y25+=1
    elif y[i]>=20:
        y20+=1
    elif y[i]>=15:
        y15+=1
    elif y[i]>=10:
        y10+=1
    elif y[i]>=5:
        y5+=1
    elif y[i]>=0:
        y0+=1
    elif y[i]>=-5:
        y_5+=1
    elif y[i]>=-10:
        y_10+=1
    if y[i]<0:
        cold+=1
        if cold>maxcold:
            maxcold=cold
    else:
        cold=0
print('There was',hot,'hot days')
print('Longest cold days break:',maxcold)
plt.plot(x,y)
plt.show()
temp=['-10','-5','0','5','10','15','20','25','30']
yes=[y_10,y_5,y0,y5,y10,y15,y20,y25,y30]
plt.bar(temp,yes,color='red')
plt.show()
