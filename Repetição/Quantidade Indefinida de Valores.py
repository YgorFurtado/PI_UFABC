from statistics import mean
grupo = []
g = 2
while(g!=0):
    g = int(input())
    grupo.append(g)
grupo.remove(0)
print("%.2f"%mean(grupo))