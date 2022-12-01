linhas_a = int(input('Quantidade de linhas do vetor A: '))
colunas_a = int(input('Quantidade de colunas do vetor A: '))
#linhas_b = int(input('Quantidade de linhas do vetor B: '))
#colunas_b = int(input('Quantidade de colunas do vetor B: '))

a = [[None]*colunas_a]*linhas_a
#b = [[None]*colunas_b]*linhas_b

for i in range(linhas_a):
    for j in range(colunas_a):
        a[i][j] = int(input())
        
bp=1
