algo = input('Digite algo: ')

cores = {'azul':'\033[1;36m',
         'limpa':'\033[m',
         'downblue':'\033[1;34m'}

print('{}O tipo primitivo desse valor é{} '.format(cores['azul'], cores['limpa']), type(algo))
print('{}Só tem espaços?{} '.format(cores['downblue'], cores['limpa']), algo.isspace())
print('{}É um número?{} '.format(cores['azul'], cores['limpa']), algo.isnumeric())
print('{}É alfabético?{} '.format(cores['downblue'], cores['limpa']), algo.isalpha())
print('{}É alfanumérico?{} '.format(cores['azul'], cores['limpa']), algo.isalnum())
print('{}Está em maiúsculas?{} '.format(cores['downblue'], cores['limpa']), algo.isupper())
print('{}Está em minúsculas?{} '.format(cores['azul'], cores['limpa']), algo.islower())
print('{}Está capitalizado?{} '.format(cores['downblue'], cores['limpa']), algo.istitle())

