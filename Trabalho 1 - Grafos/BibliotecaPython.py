# extras

def abrirArquivo(NomeArq):
    arquivo = open(NomeArq, 'r')

    return arquivo


def fecharArquivo(Arq):
    Arq.close()


def converteEmListaSimples(G):
    aux = []
    for i in range(len(G)):
        aux2 = []
        for j in range(len(G[i])):
            aux2.append(int(G[i][j][0]))

        aux.append(aux2)

    return aux


# Representação

def converte_matriz1(arq):
    arq.seek(0)
    tamanhoArq = int(arq.readline().split()[0])
    matriz = [[0 for _ in range(tamanhoArq)] for _ in range(tamanhoArq)]

    linha = arq.readline()

    while linha != '':
        matriz[int(linha.split()[0])][int(linha.split()[1])] = int(linha.split()[2])
        matriz[int(linha.split()[1])][int(linha.split()[0])] = int(linha.split()[2])
        linha = arq.readline()

    return matriz


def converteLista(arq):
    arq.seek(0)
    linha1 = arq.readline()

    lista = [[] for i in range(int(linha1.split()[0]))]

    linha1 = arq.readline()
    while linha1 != '':
        el1 = linha1.split()[0]
        el2 = linha1.split()[1]
        el3 = linha1.split()[2]
        lista[int(el1)].append((int(el2), int(el3)))
        lista[int(el2)].append((int(el1), int(el3)))
        linha1 = arq.readline()

    return lista


# Informações


def grauMaior(arq, listOrMatriz):
    maiorGrau = 0
    vertice = 0

    if listOrMatriz == 1:
        listAux = converteLista(arq)
        for i in range(len(listAux)):
            if maiorGrau < len(listAux[i]):
                vertice = i
                maiorGrau = len(listAux[i])
    if listOrMatriz == 2:

        matrizAux = converte_matriz1(arq)
        for i in range(len(matrizAux)):
            aux = []
            for j in range(len(matrizAux)):
                if matrizAux[i][j] != 0:
                    aux.append(matrizAux[i][j])
            if maiorGrau < len(aux):
                vertice = i
                maiorGrau = len(aux)

    return maiorGrau, vertice


def grauMenor(arq, listOrMatriz):
    listAux = converteLista(arq)
    menorGrau = len(listAux) + 1
    vertice = 0

    if listOrMatriz == 1:

        for i in range(len(listAux)):
            if menorGrau > len(listAux[i]):
                vertice = i
                menorGrau = len(listAux[i])

    if listOrMatriz == 2:
        matrizAux = converte_matriz1(arq)
        for i in range(len(matrizAux)):
            aux = []
            for j in range(len(matrizAux)):
                if matrizAux[i][j] != 0:
                    aux.append(matrizAux[i][j])
            if menorGrau > len(aux):
                vertice = i
                menorGrau = len(aux)

    return menorGrau, vertice


def grauMedio(arq, listOrMatriz):

    medioGrau = 0

    if listOrMatriz == 1:
        listAux = converteLista(arq)
        for i in range(len(listAux)):
            medioGrau += len(listAux[i])

        medioGrau = medioGrau / len(listAux)

    if listOrMatriz == 2:
        matrizAux = converte_matriz1(arq)
        for i in range(len(matrizAux)):
            aux = []
            for j in range(len(matrizAux)):
                if matrizAux[i][j] != 0:
                    aux.append(matrizAux[i][j])

            medioGrau += len(aux)

        medioGrau = medioGrau / len(matrizAux)

    return medioGrau


def frequenciaRelativa(arq, listOrMatriz):

    Lista = []
    if listOrMatriz == 1:
        listAux = converteLista(arq)

        for i in range(len(listAux)):
            somaGraus = 0
            for j in range(len(listAux)):

                if i == len(listAux[j]):
                    somaGraus += 1
            Lista.append((i, somaGraus / len(listAux)))
        for chave in range(len(Lista) - 1, -1, -1):
            if Lista[chave][1] == 0.0:
                Lista.pop(chave)

    if listOrMatriz == 2:

        aux = []
        matrizAux = converte_matriz1(arq)
        for i in range(len(matrizAux)):
            somaGraus = 0

            for j in range(len(matrizAux)):

                if matrizAux[i][j] != 0:
                    somaGraus += 1
            aux.append(somaGraus)

        for i in range(len(matrizAux)):
            Lista.append((i, aux.count(i) / len(matrizAux)))
        for chave in range(len(Lista) - 1, -1, -1):
            if Lista[chave][1] == 0.0:
                Lista.pop(chave)

    return Lista


# Busca em Grafos: Largura e Profundidade


def buscaLargura(G, num):
    tuplaInicial = (num, num)

    visitados = []
    queue = []

    visitados.append(tuplaInicial[0])
    queue.append(tuplaInicial[0])

    file = open('buscaLarguraResult.txt', 'w')
    indice = [None for i in range(len(G))]
    indice[tuplaInicial[0]] = 0
    while len(queue) > 0:
        u = queue.pop(0)
        for v in G[u]:

            nodeV = v[0]

            if nodeV not in visitados:
                visitados.append(nodeV)
                indice[nodeV] = indice[u] + 1
                queue.append(nodeV)
        file.write(f'{u} :{indice[u]}\n')


def BuscaProfundidade(G, num):
    desc = [0 for i in range(len(G))]
    S = [num]
    R = [num]
    desc[num] = 1

    indice = [None for i in range(len(G))]
    indice[num] = 0

    arquivo = open('buscaProfundidadeResult.txt', 'w')
    arquivo.write(f'{num} :{indice[num]}\n')
    desc[num] = 1
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for v in G[u]:

            if desc[int(v[0])] == 0:
                indice[int(v[0])] = indice[u] + 1
                desempilhar = False
                S.append(int(v[0]))
                R.append(int(v[0]))
                desc[int(v[0])] = 1
                arquivo.write(f'{int(v[0])} :{indice[int(v[0])]}\n')
                break
        if desempilhar:
            S.pop()

    return R


# Componentes Conexos


def descobreComponentesConexos(G):
    comp = [0 for i in range(len(G))]
    componentes_conexas(G, comp)
    maior = 0
    for i in range(len(comp)):
        if comp[i] > maior:
            maior = comp[i]
    print(f"Componentes conexas: {maior}")
    for i in range(len(comp)):
        contador = 0
        for j in range(len(comp)):
            if comp[j] == i:
                contador += 1
        if contador != 0:
            print(f"- {contador} vertices")


def componentes_conexas(G, comp):
    marca = 0

    for u in range(len(G)):
        if comp[u] == 0:
            marca += 1
            busca_profundidade_rec(G, u, marca, comp)

    return comp


def busca_profundidade_rec(G, s, marca, comp):
    comp[s] = marca

    for v in G[s]:
        y = int(v[0])
        if comp[y] == 0:
            busca_profundidade_rec(G, y, marca, comp)
