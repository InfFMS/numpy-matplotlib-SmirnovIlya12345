# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import matplotlib.pyplot as plt
from random import randint
c1=c2=c3=c4=c5=c6=0
maxim=streak=0
q=[]
for i in range(1000):
    q.append(randint(1,6))
    if q[i]==1:
        c1+=1
    elif q[i]==2:
        c2+=1
    elif q[i]==3:
        c3+=1
    elif q[i]==4:
        c4+=1
    elif q[i]==5:
        c5+=1
    elif q[i]==6:
        c6+=1
    if i!=0:
        if q[i]==q[i-1]:
            streak+=1
        else:
            streak=1
        if streak>maxim:
            maxim=streak
    else:
        streak=maxim=1
print('Maximal strike of the same numbers:', maxim)
print('Probabilities of getting 1,2,3,4,5 or 6:',c1/1000,c2/1000,c3/1000,c4/1000,c5/1000,c6/1000)
categories = ["1", "2", "3", "4", "5", "6"]
values = [c1,c2,c3,c4,c5,c6]
plt.bar(categories, values, color='red')
plt.title("Столбчатая диаграмма")
plt.show()
