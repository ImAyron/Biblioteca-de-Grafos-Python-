import BibliotecaPython
import time

# Testes Biblioteca

nomeDoArquivo = input("\n Digite o Nome do arquivo:")

print("\nAbrindo o grafo do arquivo " + nomeDoArquivo)
arq = BibliotecaPython.abrirArquivo(nomeDoArquivo)

listOrMatriz = int(input(
    "\nDigite 1 para utilizar o grafo como lista de adjacências \nDigite 2 para utilizar o grafo como matriz de adjacências\n"))


if listOrMatriz == 1:

    print('\n' + "Representação do Grafo em Lista de Adjacências-----------------" + '\n')
    ini = time.time()
    BibliotecaPython.converteLista(arq)
    fim = time.time()
    print("Tempo de execução(s): ", fim - ini)

elif listOrMatriz == 2:
    print('\n' + "Representação do Grafo em Matriz de Adjacências----------------" + "\n")
    ini = time.time()
    BibliotecaPython.converte_matriz1(arq)
    fim = time.time()
    print("Tempo de execução(s): ", fim - ini)
execut=-1
while execut!=0:
        execut = int(input(
            "\nDigite 1 para para imprimir o maior grau do grafo"
            "\nDigite 2 para para imprimir o menor grau do grafo"
            "\nDigite 3 para para imprimir o grau medio do grafo"
            "\nDigite 4 para imprimir a frequência relativa"
            "\nDigite 5 para imprimir as buscas"
            "\nDigite 6 para imprimir as componentes conexas"
            "\nDigite 0 para encerrar o programa:"))

        if int(execut) == 1:
            print('\n' + 'Maior Grau do grafo(grau,vertice)-------------------------------' + '\n')
            ini = time.time()
            grauMaior = BibliotecaPython.grauMaior(arq, listOrMatriz)
            print(grauMaior)
            fim = time.time()
            print("Tempo de execução(s): ", fim - ini)



        elif int(execut) == 2:
            print('\n' + 'Menor Grau do grafo(grau,vertice)------------------------------' + '\n')
            ini = time.time()
            grauMenor = BibliotecaPython.grauMenor(arq, listOrMatriz)
            print(grauMenor)
            fim = time.time()
            print("Tempo de execução: ", fim - ini)

        elif int(execut) == 3:
            print('\n' + 'Grau medio do grafo--------------------------------------------' + '\n')
            ini = time.time()
            grauMedio = BibliotecaPython.grauMedio(arq, listOrMatriz)
            print(grauMedio)
            fim = time.time()
            print("Tempo de execução: ", fim - ini)

        elif int(execut) == 4:
            print('\n' + 'Frequência Relativa(Grau,frequencia)--------------------------' + '\n')
            ini = time.time()
            print(BibliotecaPython.frequenciaRelativa(arq, listOrMatriz))
            fim = time.time()
            print("Tempo de execução: ", fim - ini)

        elif int(execut) == 5:
            print('\n' + 'A busca será expressa no arquivo com o seguinte nome buscaProfundidadeResult.txt' + '\n')
            ini = time.time()
            BibliotecaPython.BuscaProfundidade(BibliotecaPython.converteLista(arq), 0)
            profundidade = open('buscaProfundidadeResult.txt', 'r')
            linhas2 = profundidade.readlines()
            for linha in linhas2:
                print(linha)

            print('\n' + 'A busca será expressa no arquivo com o seguinte nome buscalarguraResult.txt' + '\n')
            BibliotecaPython.buscaLargura(BibliotecaPython.converteLista(arq), 500)
            largura = open('buscaLarguraResult.txt', 'r')
            linhas = largura.readlines()
            for linha in linhas:
                print(linha)
            fim = time.time()
            print("Tempo de execução: ", fim - ini)

        elif int(execut) == 6:

            ini = time.time()
            comp = [0 for i in range(len(BibliotecaPython.converteLista(arq)))]
            print(BibliotecaPython.descobreComponentesConexos(BibliotecaPython.converteLista(arq)))
            fim = time.time()
            print("Tempo de execução: ", fim - ini)

BibliotecaPython.fecharArquivo(arq)
print("Fechando o grafo do arquivo " + nomeDoArquivo)
