sal = int(input())
ven = int(input())
com = 0.2
comt = ven*com
print("%.2f"%comt)
if(comt>=(0.5*sal)):
    print("Atingiu meta de vendas")
else:
    print("Nao atingiu meta de vendas")