import numpy as np
import pandas as pd
import sys

caminhoEntrada = '../datatest'

''' Função principal que executa o método heuristicos de otimização em uma instância de CVRP
    Entrada: dataset: Nome da instância
             qtdeVeiculos: qtde de veículos disponíveis na frota (valor da melhor solução disponível)'''


def main(dataset):

    print(dataset + '.vrp')

    arqEntrada = open(caminhoEntrada + '/' + dataset + '.vrp', 'r')

    qtdeNos = int(arqEntrada.readline(1))
    capacidade = int(arqEntrada.readline(1))
    coordenadas = {}
    demandas = []

    for i in range(qtdeNos):
        infoNo = [d for d in arqEntrada.readline(1).split()]
        coordenadas[int(infoNo[0])] = (int(infoNo[1]), int(infoNo[2]))

    for i in range(qtdeNos):
        infoNo = [d for d in arqEntrada.readline(1).split()]
        demandas.append(int(infoNo[1]))

    print(coordenadas)
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
if __name__ == '__main__':
    main(sys.argv[1])
