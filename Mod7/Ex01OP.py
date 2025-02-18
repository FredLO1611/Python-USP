def n_primos(x):
    def eh_primo(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    c = 0
    con = 2
    while con <= x:
        if eh_primo(con):
            c += 1
        con += 1

    return c

print(n_primos(6))