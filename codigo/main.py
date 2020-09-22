import sys
from EntradaSaida import (dataset as dt, distancia as dist, solucao as sol)
from Preprocessamento import preprocessamento as pre

''' Função principal que executa um método heuristico de otimização em uma instância de CVRP
    Entrada: dataset: Nome da instância (sem extensão)'''
def main(dataset):

  (qtdeNos, capacVeiculo, coordenadas, demandas) = dt.leituraDataset(dataset)
  (custoMelhor, solOtimaMelhor, qtdeRotasMelhor, rotasMelhor) = sol.leituraMelhorSolucao(dataset)

  distancias = pre.geraDicionarioDistancia(coordenadas)

  dt.plotDataset(coordenadas, dataset)
  dt.plotDataset(coordenadas, dataset, demandas)
  sol.plotSolucao(coordenadas, dataset, rotasMelhor)
  sol.plotSolucao(coordenadas, dataset, rotasMelhor, demandas)

  dist.saveDicionarioDistancia(distancias, dataset)
  sol.saveSolucao(custoMelhor, solOtimaMelhor, qtdeRotasMelhor, rotasMelhor, dataset)

  # dt.printDataset(qtdeNos, capacVeiculo, coordenadas, demandas)
  # dist.printDicionarioDistancia(distancias)
  # sol.printSolucao(custoMelhor, solOtimaMelhor, qtdeRotasMelhor, rotasMelhor)
    
''' Chamada da função main()
  Parâmetros: [1]nomeDataset'''
if __name__ == '__main__':
  main(sys.argv[1])
