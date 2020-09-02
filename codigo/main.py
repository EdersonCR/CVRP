import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

caminhoEntrada = '../datasets/'
caminhoVisProblema = '../visualizacao/problemas/'

def calculaDistancia(pontoAX, pontoAY, pontoBX, pontoBY):
    distancia = ((pontoBX - pontoAX) ** 2 + (pontoBY - pontoAY) ** 2) ** (1/2)
    return distancia

''' Função principal que executa o método heuristicos de otimização em uma instância de CVRP
    Entrada: dataset: Nome da instância '''
def main(dataset):

    arqEntrada = open(caminhoEntrada + dataset + '.vrp', 'r')
    
    qtdeNos = int(arqEntrada.readline())
    capacidade = int(arqEntrada.readline())
    coordenadas = {}
    demandas = []

    for i in range(qtdeNos):
        infoNo = [d for d in arqEntrada.readline().split()]
        coordenadas[int(infoNo[0])] = [float(infoNo[1]), float(infoNo[2])]

    for i in range(qtdeNos):
        infoNo = [d for d in arqEntrada.readline().split()]
        demandas.append(int(infoNo[1]))

    matriz = []
    for i in range(qtdeNos):
        matriz.append([0.0] * qtdeNos)

    for i in range(qtdeNos):
        for j in range(qtdeNos):
            matriz[i][j] = matriz[j][i] = calculaDistancia(
                coordenadas[i][0], coordenadas[i][1], coordenadas[j][0], coordenadas[j][1])

    x = [coordenadas[i][0] for i in range(qtdeNos)]
    y = [coordenadas[i][1] for i in range(qtdeNos)]
    titulo = "Instância " + dataset

    plt.title(titulo)
    plt.scatter(x[1:], y[1:], label="Clientes", color="g", marker=".", s=15) #[no * 5 for no in demandas])
    plt.scatter(x[0], y[0], label="Depósito", color="r", marker=".", s=15)

    plt.savefig(caminhoVisProblema + dataset, dpi=300)

''' Chamada da função converte_dataset()
    Parâmetros: [1]dataset, [2]qtdeVeiculos'''
if __name__ == '__main__':
    main(sys.argv[1])
