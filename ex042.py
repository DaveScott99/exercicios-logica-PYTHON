from datetime import date
print('-='*15)
print('-=FAIXA DE IDADE DOS ATLETAS-=')
print('-='*15)
ano = int(input('Qual é o ano de nascimento do atleta? '))
idade = (date.today().year - ano)
if idade <= 9:
    print('Este atleta tem {} anos e está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Este atleta tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Este atleta tem {} anos e está na categoria JÚNIOR'.format(idade))
elif idade <= 25:
    print('Este atleta tem {} anos e está na categoria SÊNIOR'.format(idade))
else:
    print('Este atleta tem {} anos e está na categora MASTER'.format(idade))
