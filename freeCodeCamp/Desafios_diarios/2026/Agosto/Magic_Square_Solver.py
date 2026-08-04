'''
Resolvedor de Quadrado Mágico (01/08/2026)

Dado um quadrado 3x3 com um número faltando (representado por 0), retorne o número que completa o quadrado mágico 
ou "impossible" (impossível) caso não exista um número válido.

Um quadrado mágico é uma grade na qual a soma dos números de cada linha, coluna e diagonal resulta no mesmo valor.

Testes:
1. solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]) deve retornar 5.
2. solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]) deve retornar 4.
3. solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]) deve retornar "impossible".
4. solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]) deve retornar 39.
5. solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]) deve retornar "impossible".
'''

def solve_magic_square(grid):
    somaTotal=0
    somaParcial=0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                lin = i
                col = j
    
    ids = [0,1,2]
    ids.remove(lin)
    for num in grid[ids[0]]:
        somaTotal += num

    for num in grid[lin]:
        somaParcial += num
    valor = somaTotal - somaParcial
    grid[lin][col] = valor

    somas = []
    for i in range(3):
        soma = 0
        for j in range(3):
            soma += grid[i][j]
        somas.append(soma)
    
    for j in range(3):
        soma = 0
        for i in range(3):
            soma += grid[i][j]
        somas.append(soma)

    somaD1 = grid[0][0]+grid[1][1]+grid[2][2]
    somaD2 = grid[0][2]+grid[1][1]+grid[2][0]
    somas.append(somaD1)
    somas.append(somaD2)

    count=0
    for num in somas:
        if num == somaTotal:
            count+=1
    
    if count == 8:
        return valor
    else:
        return 'impossible'

print(solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]))
print(solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]))
print(solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]))
print(solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]))
print(solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]))