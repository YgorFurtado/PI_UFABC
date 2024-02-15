ano = int(input())
cod = int(input())
dis = int(input())
if(1901<ano<=2000):
    if(cod == 101 or cod == 100):
        print("SIM")
    else:
        print("NAO")
elif(2001<=ano<=2020):
    if(dis>5000):
        print("SIM")
    else:
        print("NAO")
else:
    if((cod == 200 or cod == 201) and dis>200):
        print("SIM")
    else:
        print("NAO")