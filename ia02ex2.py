velocidade = float(input("Qual velocidade que estava o veiculo? "))
if velocidade > 80:
    print("você ultrapassou a velocidade permitida de 80km/h.")
    print("Sua multa é de: ", (velocidade - 80) * 7,"R$")
else:
    print("Pode continuar, você não foi multado")