import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

import Inicializacao as init

caminhoEntrada = '../datasets'


def calculaDistancia(pontoAX, pontoAY, pontoBX, pontoBY):

    distancia = ((pontoBX - pontoAX) ** 2 + (pontoBY - pontoAY) ** 2) ** (1/2)
    return distancia


''' Função principal que executa o método heuristicos de otimização em uma instância de CVRP
    Entrada: dataset: Nome da instância
             qtdeVeiculos: qtde de veículos disponíveis na frota (valor da melhor solução disponível)'''


def main(dataset):

    print(dataset + '.vrp')

    arqEntrada = open(caminhoEntrada + '/' + dataset + '.vrp', 'r')
    print(arqEntrada)

    qtdeNos = int(arqEntrada.readline())

    print(qtdeNos)

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

    x = []
    y = []
    for i in range(qtdeNos):
        x.append(coordenadas[i][0])
        y.append(coordenadas[i][1])

    titulo = "Instância " + dataset

    plt.title(titulo)

    plt.plot(x, y, color="#000000", linestyle="")
    plt.scatter(x, y, label="Clientes", color="g",
                marker=".", s=[no*5 for no in demandas])
    plt.scatter(x[0], y[0], label="Depósito", color="r", marker=".", s=20)
    plt.legend()
    plt.show()
    plt.savefig("exemplo1.png", dpi=300)

    print(coordenadas)
    print()
    print(demandas)

    '''

  df1 = pd.read_csv('M-n101-k10.csv', sep=' ', index_col=0)
  df2 = pd.read_csv('M-n101-k102.csv', sep=' ', index_col=0)
  

  cood0 = {}

  cood1 = {}
  for i in range(len(df1)):
      cood1[i] = (df1.iloc[i]['x'], df1.iloc[i]['y'])

  cood2 = {}
  for i in range(len(df2)):
      cood2[i] = df2.iloc[i]['z']

  # for i in cood1:
  #    for j in cood2:
  #        if i == j:
  #            cood0[i] = (cood1, cood2)
  #            print(cood2[j])

  # print(cood0)

  print(cood1)

  # for i in cood1 and cood2:
  #    if cood1.'''


''' Chamada da função converte_dataset()
    Parâmetros: [1]dataset, [2]qtdeVeiculos'''
# if __name__ == '__main__':
main(sys.argv[1])
