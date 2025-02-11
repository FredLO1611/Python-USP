def vogal(letra):
    if letra in 'aeiouAEIOU':
        return True
    else:
        return False

letra = 'g'
resultado = vogal(letra)
print(resultado) 