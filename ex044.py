alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso!!'.format(imc))
elif (imc <= 18.5) or (imc < 25):
    print('Seu IMC é {:.2f} e você está no peso ideal!!'.format(imc))
elif (imc <= 25) or (imc < 30):
    print('Seu IMC é {:.2f} e você acima do peso!!'.format(imc))
elif (imc <= 30) or (imc < 40):
    print('Seu IMC é {:.2f} e você tem obesidade!!'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.2f} e você está com obesidade morbida!!'.format(imc))
