import math


def calcular_distancia(x1, y1, x2, y2):
    a = math.fabs(x2-x1)
    b = math.fabs(y2-y1)
    c = a+b
    return ("%.0f" % c)
