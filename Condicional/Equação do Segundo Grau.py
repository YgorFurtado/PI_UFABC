import math
a = float(input())
b = float(input())
c = float(input())
delta = (b**2)-4*a*c
if(delta < 0):
    print("Sem solucao real!")
    print("Delta = %.2f"%delta)
elif(delta == 0):
    x = -b/(2*a)
    if(x == -0.00):
        x = -x
    else:
        x = x
    print("x = %.2f"%x)
else:
    sqd = (math.sqrt(float(("%.2f")%delta)))
    xa = (sqd-b)/(2*a)
    xb = ((b+sqd)*-1)/(2*a)
    xl = sorted([xa,xb])
    print("x1 = %.2f"%xl[0])
    print("x2 = %.2f"%xl[1])