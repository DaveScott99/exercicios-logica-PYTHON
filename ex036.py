a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if (a < b + c) and (b < c + a) and (c < a + b):
    print('É um triangulo!')
else:
    print('Não é um triangulo!') 