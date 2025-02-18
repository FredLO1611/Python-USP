def é_hipotenusa(h):
    i = 1
    while i < h:
        j = i
        while j < h:
            if h ** 2 == i ** 2 + j ** 2:
                return True
            j += 1
        i += 1
    return False

def soma_hipotenusas(n):
    soma = 0
    num = 1
    while num <= n:
        if é_hipotenusa(num):
            soma += num
        num += 1
    return soma

print(soma_hipotenusas(25))