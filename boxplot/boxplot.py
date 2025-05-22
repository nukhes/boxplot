import math

def mediana(x):
    if x == []: x = [0]
    x = sorted(x)
    comprimento = len(x)
    meio = comprimento // 2
    
    if comprimento % 2 == 0:
        return (x[meio] + x[meio -1])/2
    return x[meio]

def quartis(x, largura=50):
    comprimento = len(x)
    meio = comprimento // 2
    
    q2 = mediana(x)
    q1 = mediana(x[:meio])
    q3 = mediana(x[meio:])
    
    if comprimento % 2 != 0:
        q3 = mediana(x[meio+1:])
    
    print(f"lista{x}")
    
    minimo = x[0]
    maximo = x[-1]

    # mapeia valores para posições numa linha de largura
    def escala(valor):
        return int((valor - minimo) / (maximo - minimo) * (largura - 1)) if maximo != minimo else largura // 2

    linha = [' '] * largura
    linha[escala(minimo)] = '['
    linha[escala(q1)] = '|'
    linha[escala(q2)] = '|'
    linha[escala(q3)] = '|'
    linha[escala(maximo)] = ']'

    print(''.join(linha))
    print(f"[{minimo}] {q1} {q2} {q3} [{maximo}]\n")
    

