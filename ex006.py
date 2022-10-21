number = int(input('\033[1;31mDigite um número:\033[m '))

ante = (number - 1)
suc = (number + 1)

print('\033[1;36mVocê digitou {} e seu antecessor é {} e seu sucessor é {}\033[m'.format(number, ante, suc))