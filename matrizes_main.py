def multiplicaMatriz():
    x = input('Matriz a ser multiplicada: ')
    x = eval(x.lower())
    y = int(input('Multiplicador: '))
    return x*y

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

print(multiplicaMatriz())