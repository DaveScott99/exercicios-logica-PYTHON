s = 0
cont = 0
for impar in range(1, 501, 2):
        if impar %3 == 0:
            cont += 1
            s += impar
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
