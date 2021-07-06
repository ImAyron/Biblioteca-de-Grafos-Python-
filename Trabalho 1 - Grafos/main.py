import sys

#nameArq=input("Digite o nome do arquivo:")


arquivo=open('dinamaique.txt')

arestasEvertices=[]


linha1=arquivo.readline().rstrip()
print(linha1)
vertices=""
peso=""
for caractere in linha1:
    if caractere !=" " and caractere !="":
        peso = peso + caractere
    else:
        vertices=int(peso)
        peso=""


arestas=int(peso)

print(vertices)
print(arestas)
#lista de adjacencias
desc = [0 for i in range(vertices)]

print(desc)

#matriz de adjacencias
descMatriz = [[0 for i in range(vertices)]for i in range(vertices)]

print(descMatriz)


for linha in arquivo:

    sys.stdout.write(linha)



arquivo.close()