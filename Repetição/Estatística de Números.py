from statistics import mean
n = int(input())
d = 0
grupo = [] 
while(d<n):
    grupo.append(int(input()))
    d = d +1
print(sum(grupo))
print("%.2f"%mean(grupo))
print(min(grupo))
print(max(grupo))