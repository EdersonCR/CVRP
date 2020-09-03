import sys
from Entrada import dataset as dt
from Preprocessamento import distancia as dist
from Saida import (salvar as save, visualizar as vis)

''' Função principal que executa um método heuristico de otimização em uma instância de CVRP
    Entrada: dataset: Nome da instância '''
def main(dataset):

  # Entrada de dados
  (qtdeNos, capacVeiculo, coordenadas, demandas) = dt.leitura(dataset)

  # Preprocessamento
  distancias = dist.geraMatrizDistancia(coordenadas) 

  # Saida de dados
  save.plotPontos(coordenadas, dataset)
  #save.plotPontos(coordenadas, dataset, demandas)
  save.matrizDistancia(distancias, dataset)
  #vis.printDadosDataset(qtdeNos, capacVeiculo, coordenadas, demandas)
  #vis.printMatrizDistancia(distancias)

''' Chamada da função main()
    Parâmetros: [1]nomeDataset'''
if __name__ == '__main__':
  main(sys.argv[1])