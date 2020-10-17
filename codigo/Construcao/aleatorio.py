from random import *

''' Função que executa uma heuristica aleatoria para definir uma solução para CVRP
    Entrada: qtdeNos = quantidade de nós (clientes + depósito)
             capacVeiculo = capacidade de carga do veículo
             demandas = lista de demandas dos nós, id do nó = índice da lista
             semente = valor incial passado para gerador de numeros pseudoaletório
    Saida: rota = [ nós ] listas com a ordem de visitação de nós nas rotas '''
def heuristicaAleatoria(qtdeNos, capacVeiculo, demandas, semente):

  seed(semente)

  clientes = [c for c in range(1, qtdeNos)]
  clientes = sample(clientes, len(clientes))

  demandaRota = 0
  rota = [0]

  for cliente in clientes:
    
    if demandaRota + demandas[cliente] <= capacVeiculo:
      demandaRota += demandas[cliente]
    else:
      rota.append(0)
      demandaRota = demandas[cliente]

    rota.append(cliente)

  rota.append(0)
  
  return rota
