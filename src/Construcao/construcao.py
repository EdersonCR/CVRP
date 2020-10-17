from Construcao import (guloso as gul, aleatorio as ale)

''' Função que identifica e faz a chamada das heiricas contrutivas
    Entrada: qtdeNos = quantidade de nós (clientes + depósito)
             capacVeiculo = capacidade de carga do veículo
             demandas = lista de demandas dos nós, id do nó = índice da lista
             distancias = {id: [ distancias ]} dicionario com as listas das distancias entre os pontos
             semente = valor incial passado para gerador de numeros pseudoaletório
    Saida: rota = [ nós ] listas com a ordem de visitação de nós nas rotas '''
def heuristicaConstrutiva(heuristica, qtdeNos, capacVeiculo, demandas, distancias, semente):

  rota = []

  if heuristica == 'gul':
    rota = gul.heuristicaGulosa(qtdeNos, capacVeiculo, demandas, distancias)

  elif heuristica == 'ale':
    rota = ale.heuristicaAleatoria(qtdeNos, capacVeiculo, demandas, semente)

  return rota
