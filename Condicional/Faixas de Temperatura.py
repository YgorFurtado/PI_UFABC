temp = float(input())
if(temp<-20):
    print("Muito Baixa")
elif(-20<=temp<30):
    print("Baixa")
elif(30<=temp<200):
    print("Normal")
elif(200<=temp<250):
    print("Alta")
else:
    print("Muito Alta")
