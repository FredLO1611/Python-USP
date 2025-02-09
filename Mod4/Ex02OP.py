numero = input("Digite um número inteiro: ")

i = 0
encontrou = False

while i < len(numero) - 1:
    if numero[i] == numero[i + 1]:
        encontrou = True
        break
    i += 1

if encontrou:
    print("sim")
else:
    print("não")