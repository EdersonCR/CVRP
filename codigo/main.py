import sys
from EntradaSaida import (dataset as dt, matriz as mt)
from Preprocessamento import distancia as dist

''' Função principal que executa um método heuristico de otimização em uma instância de CVRP
    Entrada: dataset: Nome da instância (sem extensão)'''
def main(dataset):

  (qtdeNos, capacVeiculo, coordenadas, demandas) = dt.leituraDataset(dataset)

  distancias = dist.geraMatrizDistancia(coordenadas)

  dt.plotDataset(coordenadas, dataset)
  dt.plotDataset(coordenadas, dataset, demandas)
  mt.saveMatrizDistancia(distancias, dataset)
  
  dt.printDataset(qtdeNos, capacVeiculo, coordenadas, demandas)
  # mt.printMatrizDistancia(distancias)
    
''' Chamada da função main()
  Parâmetros: [1]nomeDataset'''
if __name__ == '__main__':
  main(sys.argv[1])
