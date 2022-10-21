from random import randint
print('=-' *15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' *15)

cont = 0

while True:
    n = int(input('Digite um valor: '))
    computador = randint(0, 10)
    resultado = computador + n
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar?[P/I] ')).upper().strip()[0]
    print(f'Você jogou {n} e o computador {computador}. Total de {resultado}', end=' ')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU IMPAR')
    if opcao == 'P':
        if resultado % 2 == 0:
            cont += 1
            print('Voce GANHOU')
        else:
            print('Voce PERDEU')
            break
    if opcao == 'I':
        if resultado % 2 == 1:
            cont += 1
            print('Você GANHOU')
        else:
            print('Você PERDEU')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
