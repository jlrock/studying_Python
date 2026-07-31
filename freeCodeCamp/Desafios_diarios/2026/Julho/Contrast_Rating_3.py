'''
Classificação de Contraste 3 (30/07/2026)

Dados dois arrays que representam valores RGB e um booleano indicando se o texto é grande, retorne a classificação de contraste WCAG usando o seguinte método:

Primeiro, converta cada valor RGB em luminância relativa:

Divida cada canal [R, G, B] por 255 para obter um valor entre 0 e 1
Aplique a fórmula de correção gama a cada canal:
Se o valor do canal for menor ou igual a 0,04045: canal / 12,92
Caso contrário: ((canal + 0,055) / 1,055) ^ 2,4
Calcule a luminância: 0,2126 * R + 0,7152 * G + 0,0722 * B
Em seguida, calcule a razão de contraste adicionando 0,05 a cada valor de luminância e dividindo o valor mais claro pelo mais escuro. O valor mais claro será sempre o primeiro argumento.

Retorne a classificação com base na razão de contraste usando a seguinte tabela:

Classificação	Texto Normal	Texto Grande
"AAA"	        7,0+	        4,5+
"AA"	        4,5+	        3,0+
"Fail"	        abaixo de 4,5	abaixo de 3,0

Testes:
1. get_contrast_rating([255, 255, 255], [0, 0, 0], False) deve retornar "AAA".
2. get_contrast_rating([215, 188, 188], [55, 55, 55], False) deve retornar "AA".
3. get_contrast_rating([143, 144, 210], [46, 47, 61], False) deve retornar "Fail".
4. get_contrast_rating([167, 167, 210], [53, 10, 53], True) deve retornar "AAA".
5. get_contrast_rating([135, 147, 155], [60, 70, 90], True) deve retornar "AA".
6. get_contrast_rating([125, 210, 195], [105, 130, 90], True) deve retornar "Fail".
'''

def get_contrast_rating(rgb1, rgb2, is_large_text):
    rgb1_norm=[]
    rgb2_norm=[]
    for i in range(len(rgb1)):
        valorC1 = rgb1[i]/255
        rgb1_norm.append(valorC1)
        valorC2 = rgb2[i]/255
        rgb2_norm.append(valorC2)
    
    for i in range(len(rgb1_norm)):
        if rgb1_norm[i]<=0.04045:
            rgb1_norm[i]/=12.92
        else:
            rgb1_norm[i]=pow((rgb1_norm[i]+0.055)/1.055, 2.4)
        if rgb2_norm[i]<=0.04045:
            rgb2_norm[i]/=12.92
        else:
            rgb2_norm[i]=pow((rgb2_norm[i]+0.055)/1.055, 2.4)

    luminancia1 = (0.2126 * rgb1_norm[0]) + (0.7152 * rgb1_norm[1]) + (0.0722 * rgb1_norm[2])
    luminancia2 = (0.2126 * rgb2_norm[0]) + (0.7152 * rgb2_norm[1]) + (0.0722 * rgb2_norm[2])

    luminancia1+=0.05
    luminancia2+=0.05
    razaoContraste=luminancia1/luminancia2

    if is_large_text == False:
        if razaoContraste >= 7.0:
            wcag='AAA'
        elif razaoContraste >= 4.5:
            wcag='AA'
        else:
            wcag='Fail'
    else:
        if razaoContraste >= 4.5:
            wcag='AAA'
        elif razaoContraste >= 3.0:
            wcag='AA'
        else:
            wcag='Fail'
    return wcag

print(get_contrast_rating([255, 255, 255], [0, 0, 0], False))
print(get_contrast_rating([215, 188, 188], [55, 55, 55], False))
print(get_contrast_rating([143, 144, 210], [46, 47, 61], False))
print(get_contrast_rating([167, 167, 210], [53, 10, 53], True))
print(get_contrast_rating([135, 147, 155], [60, 70, 90], True))
print(get_contrast_rating([125, 210, 195], [105, 130, 90], True))