def ler_lista():
    lista = []
    while True:
        entrada = input('Digite um número (ou pressione Enter para parar): ')
        if entrada == '':
            break
        lista.append(int(entrada))
    return lista

def imprimir_lista_inversa(lista):
    for numero in reversed(lista):
        print(numero)

# Programa principal
lista = ler_lista()
imprimir_lista_inversa(lista)