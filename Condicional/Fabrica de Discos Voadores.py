def obter_prazo_entrega(c1,c2,c3):
    codigos = [c1,c2,c3]
    lenght = list(set(codigos))
    if(len(lenght) == 3):
        return 30
    elif(len(lenght) == 2):
        return 15
    else:
        return 5