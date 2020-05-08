nome=input("Qual o seu nome?")
alt=float(input("Qual a sua altura?"))
peso=float(input("Qual o seu peso?"))
IMC = peso/(alt*alt)
temperatura=18
if (IMC<17):
    print('Muito abaixo do peso')
elif(IMC<18.49):
    print('Abaixo do peso')
elif(IMC<24.99):
    print('Peso normal')
elif(IMC<29.99):
    print('Acima do peso')
elif(IMC<34.99):
    print('Obesidade I')
elif(IMC<39.99):
    print('Obesidade II (severa)')
else:
    print('Obesidade III (mórbida)')