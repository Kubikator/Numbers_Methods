import numpy as np
import function as fun
import matplotlib.pyplot as plt

from pickle import TRUE


def findMin_Dihotomia(a, b, eps, draw_graphic):
    delta = eps / 4
    x1 = None
    x2 = None
    J1 = None
    J2 = None

    if (draw_graphic):
        counter = [0]
        intervals = [a,b]

    while (b - a > eps):

        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta

        J1 = fun.f(x1)
        J2 = fun.f(x2)

        if (J1 < J2):
            b = x2
        else:
            a = x1

        if (draw_graphic):
            counter.append(counter[-1] + 1)
            intervals += [a, b]
    return counter, intervals,(a+b)/2

def cm_to_inch(value):
    return value/2.54
x,y,x_min = findMin_Dihotomia(0,1,0.0000001,TRUE)
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(cm_to_inch(16),cm_to_inch(10)))
fig, ax = plt.subplots()
i = 0
k = 0
while (i < len(x)):
  ax.plot(y[k:k+2],[x[i],x[i]],color = 'blue', linestyle = '--')
  k+=2
  i+=1
plt.title('Рис.3: Изменение интервала неопределённости\n в зависимости от итераций для точности 0.0001\n для метода Дихотомии')
ax.set_xlabel('[a,b]')
ax.set_ylabel('ki')
plt.show()
print(x_min,fun.f(x_min))