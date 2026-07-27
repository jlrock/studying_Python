'''
Distância entre Letras (26/07/2026)

Dadas duas strings de mesmo comprimento, retorne a soma das menores distâncias entre cada par de caracteres.

A entrada conterá apenas letras minúsculas.
O alfabeto é tratado como um círculo; portanto, a distância entre 'a' e 'z' é 1.

Testes:
Aprovado: 1. letter_distance("abc", "bcd") deve retornar 3.
Aprovado: 2. letter_distance("abc", "xyz") deve retornar 9.
Aprovado: 3. letter_distance("encrypt", "decrypt") deve retornar 10.
Aprovado: 4. letter_distance("algorithm", "codeblock") deve retornar 43.
Aprovado: 5. letter_distance("lobster", "penguin") deve retornar 47.
Aprovado: 6. letter_distance("alligator", "crocodile") deve retornar 55.
'''

def letter_distance(str1, str2):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    tamAlfabeto = len(alfabeto)
    tamStrings = len(str1)
    count = 0
    for i in range(tamStrings):
        for j in range(tamAlfabeto):
            if str1[i] == alfabeto[j]:
                pos1 = j
            if str2[i] == alfabeto[j]:
                pos2 = j
        dist = abs(pos1 - pos2)
        count += min(dist, tamAlfabeto - dist)
    return count

print(letter_distance("abc", "bcd"))
print(letter_distance("abc", "xyz"))
print(letter_distance("encrypt", "decrypt"))
print(letter_distance("algorithm", "codeblock"))
print(letter_distance("lobster", "penguin"))
print(letter_distance("alligator", "crocodile"))