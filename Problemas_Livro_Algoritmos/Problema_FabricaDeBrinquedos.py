pi = 3.14

diametroMaior = float(input('Digite o diâmetro do círculo maior em metros: '))
raioMaior = diametroMaior/2

somaArea = 0
for i in range(1,7):
    somaArea += pi*pow((i/6)*raioMaior, 2)

totalPapelao = somaArea*5000

print(f'Serão necessários aproximadamente {int(totalPapelao)} metros quadrados de papelão para produzir 5000 alvos de {diametroMaior} metros de diâmetro máximo')