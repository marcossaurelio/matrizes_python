def multiplicaMatriz():
    w = input('Matriz a ser multiplicada: ')
    x = eval(w.lower())
    y = int(input(f'Multiplicador: '))
    z = x.copy()
    for i in range(len(z)):
        for j in range(len(z[i])):
            elemento = x[i][j]
            z[i][j] = elemento*y
    print(f'Resultado da multiplicação: {z}')
    
def transpor():
    w = input('Matriz a ser transposta: ')
    x = eval(w.lower())
    y = []
    for i in range(len(x[i])):
        linha = []
        for j in range(len(x)):
            linha.append(x[j][i])
        y.append(linha)
            

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