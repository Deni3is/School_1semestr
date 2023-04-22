#сплитить данные из файла и формировать достаточно удобно
def WAIT():
    f = open('file.txt', 'r')
    b = f.read().split('\n')
    d=[]
    for i in range(len(b)):
        print('b',b[i])
        c=b[i].split(' ')
        print('c',c)
        for j in range(len(c)):
            d.append(c[j])
    print('d',d)
    id=[]  # № элемента в таблице
    key=[] # Ключь на занятие
    uid=[] # id пользователя
    l=0
    for m in range(len(d)):
        l=l+1
        if l == 0:
            id.append(d[m])
        if l == 1:
            key.append(d[m])
        if l == 2:
            uid.append(d[m])
        else:
            l=0
    print('id',id)
    print('key',key)
    print('uid',uid)
WAIT()