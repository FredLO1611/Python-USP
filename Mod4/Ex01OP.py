numero = int(input("Digite um número inteiro: "))

if numero > 1:
    eh_primo = True
    i = 2

    while i <= numero // 2:
        if numero % i == 0:
            eh_primo = False
            break
        i += 1

    if eh_primo:
        print('primo')
    else:
        print('não primo')
else:
    print('não primo')