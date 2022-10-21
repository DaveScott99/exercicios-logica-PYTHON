preço = float(input('Qual o valor do produto? R$'))

calc = preço - (preço * 5 / 100)

print('O produdo que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, calc))