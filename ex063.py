print('GERADOR DE PA')
print('-=' * 7)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostras a mais? '))
print('Prograssão finalizada com {} termos mostrados.'.format(total))
