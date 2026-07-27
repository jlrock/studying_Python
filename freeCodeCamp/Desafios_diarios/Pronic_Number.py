'''
Número Prônico (27/07/2026)

Dado um número, determine se ele é um número prônico.

Um número prônico é o produto de dois números inteiros consecutivos. Por exemplo, 6 é prônico porque 2 * 3 = 6.

Testes:
1. is_pronic(6) deve retornar True.
2. is_pronic(15) deve retornar False.
3. is_pronic(12) deve retornar True.
4. is_pronic(132) deve retornar True.
5. is_pronic(80) deve retornar False.
6. is_pronic(0) deve retornar True.
'''

def is_pronic(n):
    for i in range(n+1):
        if i*(i-1)==n:
            return True
    return False

numbers = [6, 15, 12, 132, 80, 0]
for n in numbers:
    if is_pronic(n)==True:
        resp='Sim'
    else:
        resp='Não'
    print(f'O número {n} é prônico? {resp}')