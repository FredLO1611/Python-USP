fatorial = 0
n = int(input("Digite o valor de n: "))
if n == 0:
    print(1)
elif n!= 0:
    fatorial = 1
    while n >= 1:
        fatorial = fatorial * n
        n = n - 1
print(fatorial)