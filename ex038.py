print('-='*15)
print('-=-=-Conversão de Números-=-=-')
print('-='*15)
number = int(input('Digite um número: '))
print('-'*25)
print('[1] para Binário')
print('[2] para Octal')
print('[3] para Hexadecimal')
print('-'*25)
pergunta = int(input('Digite a opção que deseja converter: '))
if pergunta == 1:
    bina = bin(number)[2:]
    print('Este é o número em BINÁRIO: {}'.format(bina))
elif pergunta == 2:
    octa = oct(number)[2:]
    print('Este é o número em OCTAL: {}'.format(octa))
elif pergunta == 3:
    hexa = hex(number)[2:]
    print('Este é o número em HEXADECIMAL: {}'.format(hexa))
else:
    print('Opção invalida! Tente novamente.')

