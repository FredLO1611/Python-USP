import math

a = float(input('Informe o parâmetro a: '))
b = float(input('Informe o parâmetro b: '))
c = float(input('Informe o parâmetro c: '))

delta = b**2 - 4*a*c

if delta < 0:
    print('esta equação não possui raízes reais')
else:
    raiz1 = (-b - math.sqrt(delta)) / (2*a)
    raiz2 = (-b + math.sqrt(delta)) / (2*a)

    if raiz1 == raiz2:
        print(f'a raiz desta equação é {raiz1}')
    else:
        if raiz1 > raiz2:
            print(f'as raízes da equação são {raiz1*-1} e {raiz2*-1}')
        else:
            print(f'as raízes da equação são {raiz2*-1} e {raiz1*-1}')