import numpy as np

def f(x):
    return np.exp((x**4 + 2*x**3 -5*x +6)/5) + np.cosh(1/(-15*x**3 + 10*x + 5*np.sqrt(10))) - 3

def InitVMatrix3X3(x1,x2,x3):
    V = np.arange(9, dtype=np.double).reshape(3, 3)
    V[0, 0] = x1 * x1
    V[0, 1] = x1
    V[0, 2] = 1
    V[1, 0] = x2 * x2
    V[1, 1] = x2
    V[1, 2] = 1
    V[2, 0] = x3 * x3
    V[2, 1] = x3
    V[2, 2] = 1
    return V

def findMin_SquareAproximation(a, b, eps):
    step = (b-a)/4
    x1 = a + step
    x2 = a + 2*step
    x3 = a + 3*step

    vec_J = np.arange(3, dtype=np.double).reshape(3, 1)

    vec_J[0, 0] = f(x1)
    vec_J[1, 0] = f(x2)
    vec_J[2, 0] = f(x3)

    top = None
    J_top = None
    n=0
    while b-a > eps :
        n+=1
        V = InitVMatrix3X3(x1,x2,x3)
        vec_abc = np.linalg.solve(V, vec_J)

        if (vec_abc[0] == 0):
            print('a = 0')
            top = x2
            J_top = vec_J[1]
            break
        top = - vec_abc[1] / (2 * vec_abc[0])

        if (top <= a):
            top = a
        elif (top >= b):
            top = b
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
        print(n,'\n')

    print(top)


findMin_SquareAproximation(0,1,0.01)





