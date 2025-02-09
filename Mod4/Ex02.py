n = int(input('Digite o valor de n: '))
c = 0
numero = 1

while c < n:
    if numero % 2 != 0:
        print(numero)
        c += 1
    numero += 1