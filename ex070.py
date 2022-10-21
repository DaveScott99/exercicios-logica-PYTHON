print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)

mais18 = 0
tothomem = 0
totmulher20 = 0

while True:
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 20)

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]

    if idade > 18:
        mais18 += 1
    if sexo in 'Mm' and idade:
        tothomem += 1
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    if continuar in 'Nn':
        break

print('====== FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {tothomem} homens cadastrados')
print(f'E temos {totmulher20} mulheres com menos de 20 anos')
