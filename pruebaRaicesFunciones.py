import raicesFunciones as rf
import math

def f(x):
    y = -12*math.pow(x, 5) - 6.4*math.pow(x,3) + 12
    return y

def imprimir(x):
    print(x)

bisec = rf.biseccion(f, 0, 1, 0.0001)

imprimir(bisec)

