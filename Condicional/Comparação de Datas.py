import datetime


def comparar_datas(d1, m1, a1, d2, m2, a2):
    t1 = datetime.date(a1, m1, d1)
    t2 = datetime.date(a1, m2, d2)
    if (t1 < t2):
        return -1
    elif (t1 > t2):
        return 1
    else:
        return 0
