import math
ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())

dist = math.sqrt((bx-ax)**2 +(by - ay)**2)
print("%.2f"%dist)