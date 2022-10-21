numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze'
           , 'Catorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    elif num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

    print(f'Voce digitou o número {numeros[num]}')

    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
print('FIM DO PROGRAMA')
