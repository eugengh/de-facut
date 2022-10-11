import random
import math
b = round(random.randint(1, 10))
n = round(random.random()*1000)
m = round(random.random()*1000)
print(m)
print(n)
print('baza = ', b)
if b> 1 and b<=10:
    def verify(x, y):
        c=0
        l1 = []
        l2 = []
        global b
        for i in str(x):
            l1.append(int(i))
        if max(l1)<b:
            return c
        if max(l1)>b:
            return c+1
        for z in str(y):
            l2.append(int(z))
        if max(l2)<b:
            return c
        if max(l2)>b:
            return c+1

c =verify(n,m)
if c == 0:
    print('numere sunt scrise corect in baza ', b)
else:
    print('numere nu sunt scrise corect in baza ', b)
    
def din10inalta(num, baza):
    if baza <2 or baza > 10:
        return 'baza inadmisibila'
    if baza == 10:
        return 'Conversia nu este necesara'
    val = ''
    rest = ''
    while rest > 0:
        val = str(rest % baza) + val
        rest = math.floor(rest/baza)
    return val

def zecimal(x, y):
    n1 = 0
    n2 = 0
    x = str(x)
    y = str(y)
    a=len(x) - 1
    v = len(y) - 1
    global b

    if verify(x, y) == 0:
        if b == 10:
            return print('(',x+y,')','in baza ', 10, '\n(',x-y,')','sau','(',y-x,')','in baza ', 10, '\n(',x*y,')','in baza ', 10)
        while(a>=0):
            for z in range(0,len(x)):
                n1+=(int(x[z]) * (b**a))
                a=a-1
        while(v>=0):
            for f in range(0, len(y)):
                n2+=(int(y[f]) * (b**v))
                v=v-1
        Suma = n1+n2
        Dif1 = n1-n2
        Dif2 = n2-n1
        Prod = n1*n2
        return print('(',n1+n2,')','in baza ', 10, '\n(',n1-n2,')','sau','(',n2-n1,')','in baza ', 10, '\n(',n1*n2,')','in baza ', 10, '\n', 'Operatiile in baza ',b, ' sunt: \n', n,'+',m, '=', din10inalta(Suma, b),'\n',n,'-',m, '=', din10inalta(Dif1, b),'\n', m,'-',n, '=', din10inalta(Dif2, b), '\n', n,'*',m, '=', din10inalta(Prod, b))
        


zecimal(n,m)


