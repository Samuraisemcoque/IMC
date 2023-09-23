# Solicita ao usuário que insira seu peso em quilogramas e sua altura em metros
peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print("Seu IMC é:", imc)

# Classificação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 24.9:
    print("Seu peso está normal.")
elif imc >= 25 and imc < 29.9:
    print("Você está com sobrepeso.")
elif imc >= 30 and imc < 34.9:
    print("Você está com obesidade grau I.")
elif imc >= 35 and imc < 39.9:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade grau III (obesidade mórbida).")
