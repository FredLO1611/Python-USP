vc = 0
vp = 0

def partida():
    global vc, vp
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    if n % (m + 1) == 0:
        print('\nVocê começa!\n')
        while n > 0:
            n -= usuario_escolhe_jogada(n, m)
            if n > 0:
                n -= computador_escolhe_jogada(n, m)
    else:
        print('\nComputador começa!\n')
        while n > 0:
            n -= computador_escolhe_jogada(n, m)
            if n > 0:
                n -= usuario_escolhe_jogada(n, m)

def computador_escolhe_jogada(n, m):
    global vc
    sub = n % (m + 1)
    if sub == 0 or sub > m:
        sub = m
    print(f'O computador tirou {sub} peças.')
    n -= sub
    print(f'Agora restam {n} peças no tabuleiro.\n')

    if n == 0:
        vc += 1
        print('Fim de jogo! Computador ganhou!')
    return sub

def usuario_escolhe_jogada(n, m):
    global vp
    sub = int(input('Quantas peças você vai tirar? '))
    while sub > m or sub <= 0:
        print('\nOops! Jogada inválida! Tente de novo.\n')
        sub = int(input('Quantas peças você vai tirar? '))

    print(f'\nVocê tirou {sub} peças.')
    n -= sub
    print(f'Agora restam {n} peças no tabuleiro.\n')

    if n == 0:
        vp += 1
        print('Fim de jogo! Você ganhou!')
    return sub

def campeonato():
    global vc, vp
    print('\nVocê escolheu um campeonato!')
    print('\n**** Rodada 1 ****\n')
    partida()
    print('\n**** Rodada 2 ****\n')
    partida()
    print('\n**** Rodada 3 ****\n')
    partida()

    print('\n*** Final do campeonato! ***')
    print(f'\nPlacar Você {vp} X {vc} Computador')

print('$ > python3 jogo_nim.py\n')
print('Bem-vindo ao jogo do NIM! Escolha:\n')
esc = str(input('1 - para jogar uma partida isolada \n2 - para jogar um campeonato '))
if esc == '1':
    print('\nVocê escolheu uma partida isolada!\n')
    partida()
elif esc == '2':
    campeonato()
else:
    while esc not in '1 2':
        print('\nInválido! Tente novamente.\n')
        esc = str(input('1 - para jogar uma partida isolada \n2 - para jogar um campeonato '))
        if esc == '1':
            print('\nVocê escolheu uma partida isolada!\n')
            partida()
        elif esc == '2':
            campeonato()