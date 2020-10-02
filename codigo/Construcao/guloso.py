import sys

''' Função que executa uma heuristica gulosa para definir uma solução para CVRP
    Entrada: qtdeNos = quantidade de nós (clientes + depósito)
             capacVeiculo = capacidade de carga do veículo
             demandas = lista de demandas dos nós, id do nó = índice da lista
             distancias = {id: [ distancias ]} dicionario com as listas das distancias entre os pontos
    Saida: rotas = {id_rota: [ clientes ]} dicionário com as listas de clientes das rotas '''
def heristicaGulosa(qtdeNos, capacVeiculo, demandas, distancias):

  rotas = {}
  visitados = [0] * qtdeNos
  visitados[0] = 1

  numRota = 0
  proximoLocal = 0
  demandaRota = 0

  while 0 in visitados:

    localAtual = proximoLocal
    
    if proximoLocal == 0:
      numRota += 1
      demandaRota = 0
      rotas[numRota] = []
    else:
      rotas[numRota].append(proximoLocal)
      visitados[proximoLocal] = 1
      demandaRota += demandas[proximoLocal]

    proximoLocal = 0
    menorDistancia = sys.maxsize

    for i in range(1, qtdeNos):
      if visitados[i] == 0 and distancias[localAtual][i] < menorDistancia and demandaRota + demandas[i] <= capacVeiculo and (demandaRota == 0 or distancias[0][rotas[numRota][0]]):
          proximoLocal = i
          menorDistancia = distancias[localAtual][i]

  return rotas
