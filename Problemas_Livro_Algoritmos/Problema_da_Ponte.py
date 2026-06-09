import math

x = float(input('Digite o comprimento da ponte em km (Deve estar entre 2 e 4): '))

if x > 4:
    x = float(4)
if x < 2:
    x = float(2)

l = x*1000 # Comprimento da ponte em metros

comp_MaiorCabo = math.sqrt(pow(l/2, 2) + pow(l/20, 2))

somaCabos = 0
for i in range(1, 6):
    somaCabos += comp_MaiorCabo*(i/5)

comp_final = somaCabos*4

print(f'Serão necessários aproximadamente {int(comp_final)} metros de cabos de aço para construir uma ponte de {x} km !')