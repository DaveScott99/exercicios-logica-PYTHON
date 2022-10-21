number1 = int(input('\033[1;36mPrimeiro Número:\033[m '))
number2 = int(input('\033[1;36mSegundo Número:\033[m '))

soma = number1 + number2
print('\033[1;31mA soma entre {} e {} vale {}\033[m'.format(number1, number2, soma))