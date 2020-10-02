from random import *
from Construcao import SEMENTE

''' Função que executa uma heuristica aleatoria para definir uma solução para CVRP
    Entrada: qtdeNos = quantidade de nós (clientes + depósito)
             capacVeiculo = capacidade de carga do veículo
             demandas = lista de demandas dos nós, id do nó = índice da lista
    Saida: rotas = {id_rota: [ clientes ]} dicionário com as listas de clientes das rotas '''
def heristicaAleatoria(qtdeNos, capacVeiculo, demandas):

  seed(SEMENTE)

  clientes = [c for c in range(1, qtdeNos)]
  clientes = sample(clientes, len(clientes))

  print(clientes)

  demandaRota = 0
  numRota = 1
  rotas = {}
  rotas[numRota] = []

  for cliente in clientes:
    
    if demandaRota + demandas[cliente] <= capacVeiculo:
      rotas[numRota].append(cliente)
      demandaRota += demandas[cliente]
    else:
      numRota += 1
      rotas[numRota] = [cliente]
      demandaRota = demandas[cliente]
  
  return rotas
