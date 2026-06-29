import math

#Supondo que o ângulo padrão que a escada forma com o chão é 60 graus 

h = float(input('Digite a altura dos pregos em metros: '))

tamanhoEscada = 2*h/math.sqrt(3)
tamanhoEscada_cm = tamanhoEscada*100

qtd_degraus = tamanhoEscada_cm/30

print(f'Serão necessários aproximadamente {math.ceil(qtd_degraus)} degraus na escada')