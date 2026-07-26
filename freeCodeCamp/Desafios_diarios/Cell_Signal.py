'''
Sinal de Celular (25/07/2026)

Dado um grid contendo três leituras de torres de celular, determine a localização do telefone.

Cada célula no grid é 0 (sem torre) ou um inteiro positivo representando o número de células até o telefone, 
medido em linha reta: horizontal, vertical ou diagonal.

Retorne a [linha, coluna] da célula que corresponde ao número correto de células até todas as três torres.

Há sempre exatamente uma solução.

Testes:
Aprovado:1. find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]) deve retornar [1, 2].

Aprovado:2. find_signal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]) deve retornar [2, 1].

Aprovado:3. find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]) deve retornar [2, 2].

Aprovado:4. find_signal([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) 
deve retornar [3, 4].

Aprovado:5. find_signal([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], 
[0, 2, 0, 0, 0, 2]]) deve retornar [3, 3].
'''

def find_signal(grid):
    torres=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0:
                torres.append([grid[i][j], i, j])
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count=0
            for torre in torres:
                dr = abs(i - torre[1])
                dc = abs(j - torre[2])
                if max(dr, dc) == torre[0]:
                    count+=1
            if count == len(torres):
                return [i, j]

print(find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]))
print(find_signal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]))
print(find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]))
print(find_signal([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(find_signal([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 2]]))