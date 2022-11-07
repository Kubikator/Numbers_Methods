import numpy as np
import matplotlib.pyplot as plt
from pickle import TRUE

import function


def f(x):
    return np.exp((x**4 + 2*x**3 -5*x +6)/5) + np.cosh(1/(-15*x**3 + 10*x + 5*np.sqrt(10))) - 3

def InitVMatrix3X3(x1,x2,x3):
    V = np.arange(9, dtype=np.double).reshape(3, 3)
    V[0] = [x1 ** 2, x1, 1]
    V[1] = [x2 ** 2, x2, 1]
    V[2] = [x3 ** 2, x3, 1]
    return V

def findMin_GC_and_SA(a, b, eps,draw_graphic = TRUE):
    FIB = (1 + np.sqrt(5)) / 2

    x1 = (a + b * (FIB - 1)) / FIB
    x2 = (b + a * (FIB - 1)) / FIB
    J1 = f(x1)
    J2 = f(x2)

    if (J1 <= J2):
        x3 = x2
        J3 = J2
        x2 = x1
        J2 = J1
        x1 = (a + x3 * (FIB - 1)) / FIB
        J1 = f(x1)
    else:
        x3 = (b + x1 * (FIB - 1)) / FIB
        J3 = f(x3)

    vec_J = np.arange(3, dtype=np.double).reshape(3, 1)
    vec_J = [J1,J2,J3]
    top = 0
    top_prev = -10

    if (draw_graphic):
        counter = [0]
        intervals = [a,b]

    while np.abs(top - top_prev) > eps :
        top_prev = top
        V = InitVMatrix3X3(x1,x2,x3)
        vec_abc = np.linalg.solve(V, vec_J)

        top = - vec_abc[1] / (2 * vec_abc[0])

        if (top <= a):
            if (a - top > eps):
                top = a
            else:
                break
        elif (top >= b):
            if (top - b > eps):
                top = b
            else:
                break
        J_top = f(top)

        if (vec_J[0] < vec_J[2]):
            b = x3
            if (top < x1):
                x3 = x2
                x2 = x1
                x1 = top

                vec_J[2] = vec_J[1]
                vec_J[1] = vec_J[0]
                vec_J[0] = J_top
            elif (top < x2):
                x3 = x2
                x2 = top

                vec_J[2] = vec_J[1]
                vec_J[1] = J_top
            elif (top < x3):
                x3 = top
                vec_J[2] = J_top

        elif (vec_J[0] > vec_J[2]):
            a = x1
            if (top > x3):
                x1 = x2
                x2 = x3
                x3 = top

                vec_J[0] = vec_J[1]
                vec_J[1] = vec_J[2]
                vec_J[2] = J_top
            elif (top > x2):
                x1 = x2
                x2 = top

                vec_J[0] = vec_J[1]
                vec_J[1] = J_top
            elif (top > x1):
                x1 = top
                vec_J[0] = J_top

        if (draw_graphic):
            counter += [counter[-1] + 1]
            intervals += [a,b]
    return counter, intervals, top

def cm_to_inch(value):
    return value/2.54
x,y,top = findMin_GC_and_SA(0,1,0.0000001,TRUE)
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(cm_to_inch(16),cm_to_inch(10)))
fig, ax = plt.subplots()
i = 0
k = 0
while (i < len(x)):
  ax.plot(y[k:k+2],[x[i],x[i]],color = 'blue', linestyle = '--')
  k+=2
  i+=1
plt.title('Рис.14: Изменение интервала неопределённости\n в зависимости от итераций для точности 0.0000001\n для МЗС + МПКА')
ax.set_xlabel('[a,b]')
ax.set_ylabel('ki')
plt.show()
print(top,function.f(top),x[-1])
