arq = open("arquivo.txt", "w")

arq.write("Gravando a linha 1 no arquivo\n")
arq.write("Gravando a linha 2 no arquivo\n")
arq.write("Gravando a linha 3 no arquivo\n")

arq.close()


reader = open("arquivo.txt", "r")
print(reader.read())
reader.close()