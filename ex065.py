numeros = parada = cont = 0
while parada != 999:
    parada = int(input('Digite um número (999 para parar): '))
    if parada != 999:
        numeros += parada
        cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, numeros))