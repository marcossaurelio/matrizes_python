def cadastrar_matriz_a():
    linhas_a = int(input('Quantidade de linhas da matriz A: '))
    colunas_a = int(input('Quantidade de colunas da matriz A: '))
    a = []
    for l in range(linhas_a):
        linha = []
        for c in range(colunas_a):
            linha.append(float(input(f'Digite o elemento a[{l}][{c}]: ')))
        a.append(linha)
    return a
    
def cadastrar_matriz_b():
    linhas_b = int(input('Quantidade de linhas da matriz B: '))
    colunas_b = int(input('Quantidade de colunas da matriz B: '))
    b = []
    for l in range(linhas_b):
        linha = []
        for c in range(colunas_b):
            linha.append(float(input(f'Digite o elemento b[{l}][{c}]: ')))
        b.append(linha)
    return b

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
    print(f'Resultado da multiplicação:')
    print_matriz(z)
    
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
        print('Soma das matrizes A e B:')
        print_matriz(x)
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
        print(f'O maior valor da matriz A é {maior}, na posição {posicao}')
        
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
        print(f'O menor valor da matriz B é {menor}, na posição {posicao}')
        
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
    y = int((x**2)**0.5)
    s = 0
    for i in range(1,y+1):
        if y%i == 0:
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
        for i in range(len(b)):
            for j in range(len(b[i])):
                if verifica_primo(b[i][j]) == True:
                    soma_primos += 1
        print(f'A matriz B possui {soma_primos} números primos')
        
def transformar_linha_coluna_quadrada():
    n = input('Informe a matriz a ser operada:\n0. B\n1. A\n')
    while n != '0' and n != '1':
        print('Opção inválida! Digite 0 ou 1')
        n = input('Informe a matriz a ser operada:\n0. B\n1. A\n')
    if n == '1':
        z = a.copy()
    elif n == '0':
        z = b.copy()
    if len(z) == 1:
        y = []
        for i in range(len(z[0])):
            linha = []
            for j in range(len(z[0])):
                if i == j:
                    linha.append(z[0][i])
                else:
                    linha.append(0)
            y.append(linha)
        print('Matriz quadrada a partir de vetor linha:')
        print_matriz(y)
    elif len(z[0]) == 1:
        y = []
        for i in range(len(z)):
            linha = []
            for j in range(len(z)):
                if i == j:
                    linha.append(z[i][0])
                else:
                    linha.append(0)
            y.append(linha)
        print('Matriz quadrada a partir de vetor coluna:')
        print_matriz(y)
    elif len(z) == len(z[0]):
        y = []
        for i in range(len(z)):
            linha = []
            for j in range(len(z[0])):
                if i == j:
                    linha.append(z[i][j])
            y.append(linha)
        print('Matriz coluna a partir de matriz quadrada:')
        print_matriz(y)
    else:
        soma = 0
        for i in range(len(z)):
            for j in range(len(z[0])):
                soma += z[i][j]
        y = soma
        print(f'Soma de todos os elementos da matriz: {soma}')
        
def produto_matricial():
    if len(a[0]) == len(b):
        y = []
        for i in range(len(a)):
            linha = []
            for j in range(len(b[0])):
                soma = 0
                for k in range(len(a[0])):
                    soma += a[i][k]*b[k][j]
                linha.append(soma)
            y.append(linha)
        print('Produto matricial entre A e B:')
        print_matriz(y)
    else:
        print('Número de colunas de A é diferente do número de linhas de B. Impossível operar produto matricial.')

user_option = '0'

while user_option != '00':
    try:
        if user_option == '1':
            multiplica_matriz()
        elif user_option == '2':
            c = transpor_matriz(a)
            d = transpor_matriz(b)
            print('Transposta de A:')
            print_matriz(c)
            print('Transposta de B:')
            print_matriz(d)
        elif user_option == '3':
            soma_matrizes()
        elif user_option == '4':
            diagonais_ou_maior_a()
        elif user_option == '5':
            diagonais_cima_baixo_ou_menor_b()
        elif user_option == '6':
            medias_matriz_a()
        elif user_option == '7':
            transposta_x_ou_primos_b()
        elif user_option == '8':
            transformar_linha_coluna_quadrada()
        elif user_option == '9':
            produto_matricial()
        elif user_option == '0':
            a = cadastrar_matriz_a()
            b = cadastrar_matriz_b()
        opt = input('Tecle enter para acessar o menu:\n')
        user_option = input('Selecione uma opção:\n1. Multiplicar matriz por número inteiro\n2. Exibir transposta da matriz\n3. Somar matrizes A e B\n4. Diagonais de A\n5. Elementos abaixo e acima da diagonal principal de B\n6. Média de A por linha e coluna\n7. Transposta de B multiplicada por 2,5\n8. Matriz quadrada a partir de linha/coluna\n9. Produto Matricial entre A e B\n0. Reiniciar programa\n00. Encerrar programa\n')
        while (user_option not in ['0','1','2','3','4','5','6','7','8','9','00']):
            user_option = input('Digite uma opção:\n1. Multiplicar matriz por número inteiro\n2. Exibir transposta da matriz\n3. Somar matrizes A e B\n4. Diagonais de A\n5. Elementos abaixo e acima da diagonal principal de B\n6. Média de A por linha e coluna\n7. Transposta de B multiplicada por 2,5\n8. Matriz quadrada a partir de linha/coluna\n9. Produto Matricial entre A e B\n0. Reiniciar programa\n00. Encerrar programa\n')
    except:
        print('Erro na execução do programa')
        user_option = input('Selecione uma opção:\n1. Multiplicar matriz por número inteiro\n2. Exibir transposta da matriz\n3. Somar matrizes A e B\n4. Diagonais de A\n5. Elementos abaixo e acima da diagonal principal de B\n6. Média de A por linha e coluna\n7. Transposta de B multiplicada por 2,5\n8. Matriz quadrada a partir de linha/coluna\n9. Produto Matricial entre A e B\n0. Reiniciar programa\n00. Encerrar programa\n')
        while (user_option not in ['0','1','2','3','4','5','6','7','8','9','00']):
            user_option = input('Digite uma opção:\n1. Multiplicar matriz por número inteiro\n2. Exibir transposta da matriz\n3. Somar matrizes A e B\n4. Diagonais de A\n5. Elementos abaixo e acima da diagonal principal de B\n6. Média de A por linha e coluna\n7. Transposta de B multiplicada por 2,5\n8. Matriz quadrada a partir de linha/coluna\n9. Produto Matricial entre A e B\n0. Reiniciar programa\n00. Encerrar programa\n')