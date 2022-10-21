metros = float(input('\033[1;32;40mQuantos Metros?\033[m '))

cent = metros * 100
mili = metros * 1000

print('\033[7;30;43mA conversão de {} metros para {} centimetros.\033[m'.format(metros, cent))
print('\033[7;30;43mA conversão de {} metros para {} milimetros.\033[m'.format(metros, mili))