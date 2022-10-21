print('*'*24)
print('*** RADAR ELETRÔNICO ***')
print('*'*24)
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (velocidade - 80)*7
    print('MULTADO! Você excedeu o limite permitido de 80km/h \nVocê deve pagar uma multa de R${} '
          '\nTenha um bom dia! Dirija com segurança!'.format(multa))