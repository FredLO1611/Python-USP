import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho médio de frase: "))
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    while True:
        texto = input(f"Digite o texto {i} (aperte enter para sair):\n")
        if not texto:
            break
        textos.append(texto)
        i += 1
    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))
    palavras = []
    for frase in frases:
        palavras.extend(separa_palavras(frase))

    n_palavras = sum(len(palavra) for palavra in palavras)
    n_total_palavras = len(palavras)
    n_palavras_diferentes_count = n_palavras_diferentes(palavras)
    n_palavras_unicas_count = n_palavras_unicas(palavras)
    n_caracteres_sentencas = sum(len(sentenca) for sentenca in sentencas)
    n_frases = len(frases)
    n_caracteres_frases = sum(len(frase) for frase in frases)
    
    wal = n_palavras / n_total_palavras
    ttr = n_palavras_diferentes_count / n_total_palavras
    hlr = n_palavras_unicas_count / n_total_palavras
    sal = n_caracteres_sentencas / len(sentencas)
    sac = n_frases / len(sentencas)
    pal = n_caracteres_frases / n_frases

    return [wal, ttr, hlr, sal, sac, pal]

def compara_assinatura(as_a, as_b):
    somatorio = sum(abs(a - b) for a, b in zip(as_a, as_b))
    return somatorio / 6

def avalia_textos(textos, ass_cp):
    assinaturas = [calcula_assinatura(texto) for texto in textos]
    similaridades = [compara_assinatura(assinatura, ass_cp) for assinatura in assinaturas]
    return similaridades.index(min(similaridades)) + 1

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    texto_infectado = avalia_textos(textos, ass_cp)
    print(f"O autor do texto {texto_infectado} está infectado com COH-PIAH")

if __name__ == "__main__":
    main()