soma_brenno = 0
soma_milena = 0
soma_jayme = 0

teste_candidato_valido = True

while teste_candidato_valido:
    entrada = int(input("Digite um valor de 1 a 3 para votar nos candidatos: "))

    if entrada >= 1 and entrada <= 3:
        if entrada == 1:
            soma_brenno += 1
        elif entrada == 2:
            soma_milena += 1
        elif entrada == 3:
            soma_jayme += 1
        else:
            print("Entrada inválida.")
    else:
        print("Entrada inválida.")

    continuar = input("Deseja continuar votando? (S/N): ")
    if continuar.upper() != 'S':
        teste_candidato_valido = False

print("Votação encerrada.")
print("Total de votos para Brenno:", soma_brenno)
print("Total de votos para Milena:", soma_milena)
print("Total de votos para Jayme:", soma_jayme)
