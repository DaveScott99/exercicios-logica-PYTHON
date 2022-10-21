soma = tot1000 = menor = cont = 0
barato = ' '

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco

    if preco > 1000:
        tot1000 += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    pergunta = ' '
    while pergunta not in 'SsNn':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))

print(f'O total da compra foi R${soma:.2f} ')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
