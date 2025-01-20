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
for i in range(1000):
    q=randint(1,6)
    if q==1:
        c1+=1
    elif q==2:
        c2+=1
    elif q==3:
        c3+=1
    elif q==4:
        c4+=1
    elif q==5:
        c5+=1
    elif q==6:
        c6+=1
categories = ["1", "2", "3", "4", "5", "6"]
values = [c1,c2,c3,c4,c5,c6]
plt.bar(categories, values, color='red')
plt.title("Столбчатая диаграмма")
plt.show()