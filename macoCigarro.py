precoMaco = float(input("Digite o preço do maço de cigarro: "))
consumoDia = int(input("Digite a quantidade que você consome por dia: "))
tempoFumante = int(input("Digite a quantos anos você fuma cigarro: "))

gastoDiario = precoMaco * consumoDia
gastoVida = gastoDiario * 365 * tempoFumante

print("Você já gastou R$ {:.2f} em cigarros.".format(gastoVida))
