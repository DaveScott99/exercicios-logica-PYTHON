from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opçao = 0

while opçao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opçao = int(input('>>>> Escola uma opção: '))
    if opçao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} o resultado é {}'. format(num1, num2, soma))
    elif opçao == 2:
        multi = num1 * num2
        print('A multiplicação de {} x {} o resultado é {}'.format(num1, num2, multi))
    elif opçao == 3:
        if num1 > num2:
            maior = num1
            print('O maior número entre {} e {} é {}'.format(num1, num2, maior))
        else:
            maior = num2
            print('O maior número entre {} e {} é {}'.format(num1, num2, maior))
    elif opçao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte Sempre!')
