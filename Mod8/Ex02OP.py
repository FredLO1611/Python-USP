def maior_elemento(lista):
    lista.sort()
    return lista[-1]

# Testes
resultado1 = maior_elemento([6, 2, 3])  # Deve retornar 6
resultado2 = maior_elemento([7, -7, 1, 5, 5, 7])  # Deve retornar 7
resultado3 = maior_elemento([-90, -27, -12])  # Deve retornar -12
resultado4 = maior_elemento([1])  # Deve retornar 1