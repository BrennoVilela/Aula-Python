# vetor1_1 = [1,1,2,3,4,5,6,7,8,9,10,11]
# vetor2_2 = [0,9,8,7,6,5,4,3,2,1,11,12]
#
# for i in range(0, len(vetor1_1)):
#     print(vetor1_1[i])


v = [60, -99, 39, -12, 33]

exibe_negativo = [x for x in v if x < 0]
print(exibe_negativo)


# Outra maneira de fazer
def exibe_negativo(vetor):
    vetor_negativo = []
    for i in vetor:
        if i < 0:
            vetor_negativo.append(i)
    return vetor_negativo

print(exibe_negativo(v))



# Soma de vetor
def soma_vetor(vetor):
    soma = 0
    for i in range(0, len(vetor)):
        soma += vetor[i]
        return soma

print(soma_vetor(v))

def media_vetor(vetor):
    soma = sum(vetor)
    media = soma / len(vetor)
    return media

print(media_vetor(v))


def valor_impar(vetor):
    impar = [x for x in vetor if x % 2 != 0]jfjkljsajsadl
    return impar

print(valor_impar(v))


