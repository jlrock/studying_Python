'''
Classificação de Contraste 2 (29/07/2026)

Dados dois valores de luminância relativa e um valor booleano indicando se o texto é grande, retorne a classificação de contraste WCAG utilizando o seguinte método:

Calcule a razão de contraste somando 0,05 a cada valor de luminância e, em seguida, dividindo o valor mais claro pelo mais escuro. O valor mais claro será sempre o primeiro argumento.

Retorne a classificação com base na razão de contraste, utilizando a seguinte tabela:

Classificação	Texto Normal	Texto Grande
"AAA"	        7,0+	        4,5+
"AA"	        4,5+	        3,0+
"Fail"	        abaixo de 4,5	abaixo de 3,0

Testes:
1. get_contrast_rating(1.0, 0.0, False) deve retornar "AAA".
2. get_contrast_rating(0.9015, 0.1364, False) deve retornar "AA".
3. get_contrast_rating(0.8965, 0.1628, False) deve retornar "Fail".
4. get_contrast_rating(0.7469, 0.0957, True) deve retornar "AAA".
5. get_contrast_rating(0.7489, 0.2018, True) deve retornar "AA".
6. get_contrast_rating(0.6571, 0.1974, True) deve retornar "Fail".
'''

def get_contrast_rating(l1, l2, is_large_text):
    taxa = (l1+0.05)/(l2+0.05)
    if is_large_text == False:
        if taxa >= 7.0:
            wcag = 'AAA'
        elif taxa >= 4.5:
            wcag = 'AA'
        else:
            wcag = 'Fail'
    else:
        if taxa >= 4.5:
            wcag = 'AAA'
        elif taxa >= 3.0:
            wcag = 'AA'
        else:
            wcag = 'Fail'
    return wcag

print(get_contrast_rating(1.0, 0.0, False))
print(get_contrast_rating(0.9015, 0.1364, False))
print(get_contrast_rating(0.8965, 0.1628, False))
print(get_contrast_rating(0.7469, 0.0957, True))
print(get_contrast_rating(0.7489, 0.2018, True))
print(get_contrast_rating(0.6571, 0.1974, True))