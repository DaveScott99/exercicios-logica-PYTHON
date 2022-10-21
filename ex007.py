number = int(input('\033[1;33mDigite um número:\033[m '))

dobro = number * 2
triplo = number * 3
raiz = number ** (1/2)

print('\033[1;35mO dobro de {} é {} \nO triplo é {} \nRaiz quadrada é {:.3f}\033[m'.format(number, dobro, triplo, raiz))