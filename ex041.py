nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
if media < 5:
    print('Aluno REPROVADO!! Estude mais!')
elif (media == 5) or (media <= 6.9):
    print('Aluno de RECUPERAÇÃO!!')
elif media > 7:
    print('Alundo APROVADO!!')
