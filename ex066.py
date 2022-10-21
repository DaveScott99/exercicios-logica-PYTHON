r = 'S'
cont = 0
num = 0
maior = menor = 0
while r == 'S':
    numero = int(input('Digite um número: '))
    cont += 1
    num += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = num / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


