print('*'*21)
print('*FORMAS DE PAGAMENTO*')
print('*'*21)
produto = float(input('Valor do produto: '))

print('''FORMAS DE PAGAMENTO
[1] À Vista no dinheiro/cheque
[2] À Vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
pag = int(input('Escolha a forma de pagamento: '))

if pag == 1:
    dinheiro = produto - (produto * 10/100)
    print('O valor do seu produto é R${:.2f} com o desconto aplicado de 10%!!'.format(dinheiro))
elif pag == 2:
    cartao = (produto - (produto * 5/100))
    print('O valor do seu produto é R${:.2f} com o desconto aplicado de 5%!!'.format(cartao))
elif pag == 3:
    parc = produto / 2
    print('O valor do seu produto é R${:.2f} parcelado em 2x o senhor pagará cada parcela de R${:.2f}!!'.format(produto, parc))
elif pag == 4:
    juros = (produto + (produto * 20/100))
    parc = juros / 2
    totparc = int(input('Quantas parcelas? '))
    parcela = juros / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
    print('O valor do seu produto R${:.2f} com um juros de 20% e a parcela será de R${:.2f}!!'.format(juros, parc))
else:
    total = produto
    print('OPÇÃO INVALIDA de pagamento. Tente novamente.')
