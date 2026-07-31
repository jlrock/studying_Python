'''
Classificação de Contraste 1 (28/07/2026)

Com base em uma razão de contraste e um valor booleano que indica se o texto é grande, retorne a classificação WCAG utilizando a seguinte tabela:

Classificação	Texto Normal	Texto Grande
"AAA"	7,0+	4,5+
"AA"	4,5+	3,0+
"Fail"	abaixo de 4,5	abaixo de 3,0

Testes:
1. get_contrast_rating("7.5", False) deve retornar "AAA".
2. get_contrast_rating("4.8", False) deve retornar "AA".
3. get_contrast_rating("4.2", False) deve retornar "Fail".
4. get_contrast_rating("4.5", True) deve retornar "AAA".
5. get_contrast_rating("3.0", True) deve retornar "AA".
6. get_contrast_rating("2.7", False) deve retornar "Fail".
'''

def get_contrast_rating(ratio, is_large_text):
    if is_large_text == False:
        if float(ratio) >= 7.0:
            wcag='AAA'
        elif float(ratio) >= 4.5:
            wcag='AA'
        else:
            wcag='Fail'
    else:
        if float(ratio) >= 4.5:
            wcag='AAA'
        elif float(ratio) >= 3.0:
            wcag='AA'
        else:
            wcag='Fail'
    return wcag

print(get_contrast_rating("7.5", False))
print(get_contrast_rating("4.8", False))
print(get_contrast_rating("4.2", False))
print(get_contrast_rating("4.5", True))
print(get_contrast_rating("3.0", True))
print(get_contrast_rating("2.7", False))