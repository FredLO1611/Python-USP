lista = [2, 2, 3, 6]
def soma_elementos(lista):
    soma = 0
    for x in lista:
        soma += x
    return soma
resultado = soma_elementos(lista)
print(resultado)