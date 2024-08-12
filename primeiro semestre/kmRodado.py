def kmRodado():
    km = float(input("Digite quantos KM o carro andou: "))
    litros = float(input("Digite quantos litros o carro consumiu: "))

    autonomia = km / litros
    print("O carro consumiu um total de: {:.2f} Km/L".format(autonomia))

kmRodado()
