import sys

''' Função que executa uma heuristica gulosa para definir uma solução para CVRP
    Entrada: qtdeNos = quantidade de nós (clientes + depósito)
             capacVeiculo = capacidade de carga do veículo
             demandas = lista de demandas dos nós, id do nó = índice da lista
             distancias = {id: [ distancias ]} dicionario com as listas das distancias entre os pontos
    Saida: rota = [ nós ] listas com a ordem de visitação de nós nas rotas '''
def heuristicaGulosa(qtdeNos, capacVeiculo, demandas, distancias):

  rota = []
  visitados = [0] * qtdeNos

  proximoLocal = 0
  demandaRota = 0

  while 0 in visitados:

    localAtual = proximoLocal
    
    rota.append(proximoLocal)
    visitados[proximoLocal] = 1
    demandaRota += demandas[proximoLocal]

    proximoLocal = 0
    menorDistancia = sys.maxsize

    for i in range(1, qtdeNos):
      if visitados[i] == 0 and distancias[localAtual][i] < menorDistancia:
          proximoLocal = i
          menorDistancia = distancias[localAtual][i]
    
    if demandaRota + demandas[proximoLocal] > capacVeiculo:
      proximoLocal = 0
      demandaRota = 0

  rota.append(0)

  return rota
