def verificar_primo(n):
    c = 0
    total_divisores = 0
    while c != n:
        c += 1
        d = n % c
        if d == 0:
            total_divisores += 1
    return total_divisores == 2

def maior_primo(n): 
    while n > 1:
        if verificar_primo(n):
            return n
        n -= 1
    return None

# Chamando a função
numero = int(input('Informe um número: '))

resultado = maior_primo(numero)
print(resultado)