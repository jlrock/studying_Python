# Consiste em calcular o custo final da mão de obra de um condomínio

pi= 3.14
salario_min = 1621
L = float(input('Digite o valor do comprimento L padrão para as casas: '))

area_retangular = 12*pow(L, 2)
area_triangular = pow(L, 2)/2
area_circular = 4*(pi*pow((L/4), 2))
area_trapezio = 3*pow(L, 2)*0.7/2

area_total = area_trapezio+area_circular+area_retangular+area_triangular

custo_total = area_total*162.1*40

print(f'Para a medida de {L:.1f} metros, o custo total da mão de obra do condomínio será R$ {custo_total:.2f}')