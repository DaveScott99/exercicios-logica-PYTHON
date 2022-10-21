num = int(input('Qual tabuada você quer? '))
print('-=' * 6)
for c in range(1, 11):
    multi = num * c
    print('{} x {:2} = {}'.format(num, c, multi))
print('-=' * 6)
