import numpy as np
import function as fun
import matplotlib.pyplot as plt

from pickle import TRUE


def findMin_GoldCut(a, b, eps, draw_graphic=TRUE):
    FIB = (1 + np.sqrt(5)) / 2
    lenght = b - a

    x1 = (a + b * (FIB - 1)) / FIB
    x2 = (b + a * (FIB - 1)) / FIB
    J1 = fun.f(x1)
    J2 = fun.f(x2)

    if (draw_graphic):
        counter = [0]
        intervals = [a,b]

    while (lenght > eps):

        if(x1 == x2):
            break

        if (J1 <= J2):
            b = x2
            x2 = x1
            J2 = J1
            x1 = (a + b * (FIB - 1)) / FIB
            J1 = fun.f(x1)
        else:
            a = x1
            x1 = x2
            J1 = J2
            x2 = (b + a * (FIB - 1)) / FIB
            J2 = fun.f(x2)
        lenght /= FIB
        if (draw_graphic):
            counter += [counter[-1] + 1]
            intervals += [a, b]
    return counter, intervals,(a+b)/2

def cm_to_inch(value):
    return value/2.54
x,y,x_min = findMin_GoldCut(0,1,10**(-17),TRUE)
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(cm_to_inch(16),cm_to_inch(10)))
fig, ax = plt.subplots()
i = 0
k = 0
while (i < len(x)):
  ax.plot(y[k:k+2],[x[i],x[i]],color = 'blue', linestyle = '--')
  k+=2
  i+=1
plt.title('Рис.8: Изменение интервала неопределённости\n в зависимости от итераций для точности 10(^-17)\n для метода Золотого сечения')
ax.set_xlabel('[a,b]')
ax.set_ylabel('ki')
plt.show()
print(x_min,fun.f(x_min),x[-1])