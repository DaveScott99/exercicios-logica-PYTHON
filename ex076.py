num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está na posição {num.index(3)+1}')
else:
    print('Não foi encontrado nenhum número 3')
print('Os números pares foram: ', end='')
for n in num:
    if n %2 == 0:
       print(n, end=' ')
