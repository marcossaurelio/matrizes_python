def print_matriz(x):
    for i in range(len(x)):
        print(x[i])

def multiplica_matriz():
    w = input('Matriz a ser multiplicada: ')
    x = eval(w.lower())
    y = int(input(f'Multiplicador: '))
    z = x.copy()
    for i in range(len(z)):
        for j in range(len(z[i])):
            elemento = x[i][j]
            z[i][j] = elemento*y
    print(f'Resultado da multiplicação: {print_matriz(z)}')
    
def transpor_matriz(x):
    #w = input('Matriz a ser transposta: ')
    #x = eval(w.lower())
    y = []
    for i in range(len(x[0])):
        linha = []
        for j in range(len(x)):
            linha.append(x[j][i])
        y.append(linha)
    return y

def soma_matrizes():
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        x = []
        for i in range(len(a)):
            linha = []
            for j in range(len(a[i])):
                linha.append(a[i][j] + b[i][j])
        x.append(linha)
        return x
    else:
        print('Não é possível realizar a soma matricial, pois as matrizes não são de mesma ordem.')
        
def diagonais_ou_maior_a():
    if len(a) == len(a[0]):
        d_principal = []
        d_secundaria = []
        for i in range(len(a)):
            for j in range(len(a[i])):
                if i == j:
                    d_principal.append(a[i][j])
                if i+j == len(a)-1:
                    d_secundaria.append(a[i][j])
        print(f'Diagonal principal: {d_principal}')
        print(f'Diagonal secundária: {d_secundaria}')
    else:
        maior = a[0][0]
        posicao = f'a[0][0]'
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] > maior:
                    maior = a[i][j]
                    posicao = f'a[{i}][{j}]'
        print(f'O maior valor da matriz é {maior}, na posição {posicao}')
        
def diagonais_cima_baixo_ou_menor_b():
    if len(b) == len(b[0]):
        d_principal = []
        acima_d_principal = []
        abaixo_d_principal = []
        for i in range(len(a)):
            for j in range(len(a[i])):
                if i == j:
                    d_principal.append(a[i][j])
                if i < j:
                    acima_d_principal.append(a[i][j])
                if i > j:
                    abaixo_d_principal.append(a[i][j])
        print(f'Elementos na diagonal principal: {d_principal}')
        print(f'Elementos acima da diagonal principal: {acima_d_principal}')
        print(f'Elementos abaixo da diagonal princial: {abaixo_d_principal}')
    else:
        menor = a[0][0]
        posicao = f'a[0][0]'
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] < menor:
                    menor = a[i][j]
                    posicao = f'a[{i}][{j}]'
        print(f'O menor valor da matriz é {menor}, na posição {posicao}')
        
def medias_matriz_a():
    if len(a) == 1 or len(a[0]) == 1:
        soma = 0
        elementos = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                soma += a[i][j]
                elementos += 1
        media = soma/elementos
        print(f'A média dos elementos da matriz A é {media:.2f}')
    else:
        media_linhas = []
        soma = 0
        elementos = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                soma += a[i][j]
                elementos += 1
            media_linhas.append([round(soma/elementos, 2)])
            soma = 0
            elementos = 0
        media_colunas = []
        for i in range(len(a[0])):
            for j in range(len(a)):
                soma += a[j][i]
                elementos += 1
            media_colunas.append(round(soma/elementos, 2))
            soma = 0
            elementos = 0
        print(f'Média de cada linha em A:')
        print_matriz(media_linhas)
        print(f'Média de cada coluna em A:')
        print(media_colunas)
        
        
def verifica_primo(x):
    x = int((x**2)**0.5)
    s = 0
    for i in range(1,x+1):
        if x%i == 0:
            s += 1
    if s == 2:
        return True
    else:
        return False
            
        
def transposta_x_ou_primos_b():
    if len(b)!=len(b[0]) and len(b) != 1 and len(b[0]) != 1:
        t = transpor_matriz(b)
        x = t.copy()
        for i in range(len(x)):
            for j in range(len(x[i])):
                elemento = t[i][j]
                x[i][j] = elemento*2.5
        print(f'Transposta de B multiplicada por 2,5:')
        print_matriz(x)
    else:
        soma_primos = 0
        for i in range(len(x)):
            for j in range(len(x[i])):
                if verifica_primo(b[i][j]) == True:
                    soma_primos += 1
        print(f'A matriz B possui {soma_primos} números primos')
        
        

linhas_a = int(input('Quantidade de linhas da matriz A: '))
colunas_a = int(input('Quantidade de colunas da matriz A: '))
a = []
for l in range(linhas_a):
    linha = []
    for c in range(colunas_a):
        linha.append(float(input(f'Digite o elemento a[{l}][{c}]: ')))
    a.append(linha)
    
    
linhas_b = int(input('Quantidade de linhas da matriz B: '))
colunas_b = int(input('Quantidade de colunas da matriz B: '))
b = []
for l in range(linhas_b):
    linha = []
    for c in range(colunas_b):
        linha.append(float(input(f'Digite o elemento b[{l}][{c}]: ')))
    b.append(linha)
    
c = transpor_matriz(a)
d = transpor_matriz(b)