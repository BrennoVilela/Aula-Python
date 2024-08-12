# def saudacoes(teste):
#     print(teste)

# saudacoes("lalalalalal")

# def media():
#     nota1 = 10
#     nota2 = 10
#     nota3 = 10
#     media = (nota1 + nota2 + nota3) / 3
#     print(f"A média é {media}")

# media()


# def apresenta_media(nome:str, nota1:float, nota2:float):
#     media = (nota1 + nota2) /2
#     print(f"Olá {nome}, a média é: {media}")

# apresenta_media("Brenno", 10, 8)

def media_funcao(*args):
    soma = 0
    for nota in args:
        soma += nota
    media = soma / len(args)
    return media

media_funcao(10, 30, 20, 5, 2, 3, 3)