import math
a=int(input('Введите 1 коэффициент = '))
b=int(input('Введите 2 коэффициент = '))
c=int(input('Введите 3 коэффициент = '))
D=b**2-4*a*c
if D>0:
    print('x1 =',(-b-(math.sqrt(D)))/(2*a))
    print('x2 =',(-b+(math.sqrt(D)))/(2*a))
elif D==0:
    print('x =',(-b/(2*a)))
else: print('Корней нет')