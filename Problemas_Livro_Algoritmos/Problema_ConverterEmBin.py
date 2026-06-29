# Problema de conversão de números da forma decimal para a binária
num = int(input('Digite um número inteiro na forma decimal para ser convertido na binária: '))
lista = [num]

x=num
while x > 1:
    x = int(x/2)
    lista.append(x)
print('Lista principal:', lista, '\n')

lista.sort()
print('Lista em ordem crescente:', lista, '\n')

for i in range(len(lista)):
    lista[i]= lista[i]%2
print('Lista em binário:', lista, '\n')

emStr = ''
for i in lista:
    emStr += str(i)

numBin = int(emStr)
print(f'O número {num} em decimal é igual a {numBin} em binário')