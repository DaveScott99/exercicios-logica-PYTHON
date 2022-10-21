cont = soma = 0
while True:
    numeros = int(input('Digite um valor (999 para parar): '))
    if numeros == 999:
        break
    cont += 1
    soma += numeros
print(f'Você digitou {cont} e a soma entre eles é {soma}.')