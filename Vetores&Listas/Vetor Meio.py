import math as m

n = int(input())
inteiro = [0]*n
for i in range(0,n):
    inteiro[i] = int(input())

metade1 = inteiro[:m.ceil(len(inteiro)/2)]
metade2 = inteiro[len(inteiro)//2:]
metade2.reverse()
if(metade1 == metade2):
    print("SIM")
else:
    print("NAO")
