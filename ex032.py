dist = float(input('Qual distância da viagem? '))
if dist <= 200:
    valor1 = dist * 0.50
    print('O total da sua passagem é R${:.2f} \nVocê está pagando R$0,45 por Km rodado.'.format(valor1))
else:
    valor2 = dist * 0.45
    print('O total da sua passagem é R${:.2f} \nVocê está pagadno R$0,50 por Km rodado.'.format(valor2))