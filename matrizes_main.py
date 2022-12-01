linhas_a = int(input('Quantidade de linhas do vetor A: '))
colunas_a = int(input('Quantidade de colunas do vetor A: '))

a = []

for l in range(linhas_a):
    linha = []
    for c in range(colunas_a):
        linha.append(float(input(f'Digite o elemento a[{l}][{c}]: ')))
    a.append(linha)
    
    
linhas_b = int(input('Quantidade de linhas do vetor B: '))
colunas_b = int(input('Quantidade de colunas do vetor B: '))

b = []

for l in range(linhas_b):
    linha = []
    for c in range(colunas_b):
        linha.append(float(input(f'Digite o elemento b[{l}][{c}]: ')))
    b.append(linha)
    
