from Construcao import (guloso as gul, aleatorio as ale)

''' Função que identifica e faz a chamada das heiricas contrutivas
    Entrada: qtdeNos = quantidade de nós (clientes + depósito)
             capacVeiculo = capacidade de carga do veículo
             demandas = lista de demandas dos nós, id do nó = índice da lista
             distancias = {id: [ distancias ]} dicionario com as listas das distancias entre os pontos
    Saida: rotas = {id_rota: [ clientes ]} dicionário com as listas de clientes das rotas '''
def heristicaConstrutiva(heuristica, qtdeNos, capacVeiculo, demandas, distancias):

  if heuristica == 'gul':
    rotas = gul.heristicaGulosa(qtdeNos, capacVeiculo, demandas, distancias)

  elif heuristica == 'ale':
    rotas = ale.heristicaAleatoria(qtdeNos, capacVeiculo, demandas)

  return rotas