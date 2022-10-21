casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
prest = float(input('Em quantos anos você quer pagar? '))
parcela = prest * 12
valor_parcela = casa / parcela
if (salario * 30/100) > valor_parcela:
   print('PARABÉNS!! O seu empréstimo foi aprovado. '
          '\nO senhor(a) deverá pagar R${:0.2f} por mês. '
          '\nEm um total de {:.0f} parcelas.' .format(valor_parcela, parcela))
elif (salario * 30/100) < valor_parcela:
    print('INFELIZMENTE o senhor(a) não pode financiar esta casa. '
          '\nPor que o valor da parcela é de R${:0.2f} '
          'e excedeu 30% do seu salario de R${:0.2f}'.format(valor_parcela, salario))