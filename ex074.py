times = (
    'Cruzeiro',
    'Sport',
    'Vasco',
    'Bahia',
    'Grêmio',
    'Novorizontino',
    'Operário-PR',
    'CSA',
    'Sampaio Corrêa',
    'Londrina',
    'CRB',
    'Chapecoense',
    'Brusque',
    'Ituano',
    'Criciúma',
    'Vila Nova',
    'Náutico',
    'Ponte Preta',
    'Tombense',
    'Guarani'
)
print(f'Lista de times do Brasileirão SERIE B {times}')
print('-=' * 20)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {times[16:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Chapecoense está na {len(times[11])}º posição')