# Abrindo o arquivo para escrever coisas nele
arq = open("arquivo.txt", "w")
arq.write("Gravando a linha 1 no arquivo\n")
arq.write("Gravando a linha 2 no arquivo\n")
arq.write("Gravando a linha 3 no arquivo\n")
arq.close()

# Abrindo o arquivo para ler as coisas que estão nele
reader = open("arquivo.txt", "r")
print(reader.read())
reader.close()

#Abrindo o arquivo para editar ele
appender = open("arquivo.txt", "a")
appender.write("\n")
appender.write("Gravando a linha 8")
appender.close()

#Abrindo o arquivo para poder ler ele de novo
print(reader.read())
reader.close()

#
arq = open("arquivo2.txt", "x")
