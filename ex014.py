salario = float(input('Qual é o salário do funcionario? R$'))

novo = salario + (salario * 15 / 100)

print('O salario deste funcionário era de R${:.2f} e teve um aumento de 15%, portanto '
      '\neste será o seu novo sálario R${:.2f}'.format(salario, novo))