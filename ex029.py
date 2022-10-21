from random import randint
from time import sleep
print('-=-'*7)
print('JOGO DA ADIVINHAÇÃO')
print('-=-'*7)
numero = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-'*21)
tentativa = int(input('Tente adivinhar qual número o computador está pensando: '))
print('PROCESSANDO...')
sleep(2)
if tentativa == numero:
    print('PARABÉNS! você conseguiu me vencer!!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(numero, tentativa))
