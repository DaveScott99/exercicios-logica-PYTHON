from datetime import date
print('-='*15)
print('-=-=-=ALISTAMENTO MILITAR-=-=-')
print('-='*15)
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
anos = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, anos, atual))
if anos < 18:
    falta = 18 - anos
    print('Ainda faltam {} anos para o alistamento.'.format(falta))
    ano = atual + falta
    print('Seu alistammento será em {}'.format(ano))
elif anos == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif anos > 18:
    falta = anos - 18
    ano = atual -falta
    print('Você já deveria ter se alistado há {} anos.'.format(falta))
    print('Seu alistamento foi em {}'.format(ano))
