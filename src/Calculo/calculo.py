from math import *

''' Função que calcula a distância entre dois pontos (arredonda o valor para o inteiro mais próximo)
    Entrada: pontoA = (x, y) coordenasdas x e y do ponto A 
             pontoB = (x, y) coordenasdas x e y do ponto A 
    Saida: distancia = distância entre os pontos A e B'''
def distanciaPontos(pontoA, pontoB):
  distancia = int(round(sqrt((pontoB[0] - pontoA[0]) ** 2 + (pontoB[1] - pontoA[1]) ** 2)))
  return distancia

''' Função que calcula o somatório das distâncias de todas as rotas
    Entrada: rota = [ nós ] listas com a ordem de visitação de nós nas rotas 
             distancias = {id: [ distancias ]} dicionario com as listas das distancias entre os pontos 
    Saida: custo = somatório das distâncias de todas as rotas'''
def funcaoObjetivo(rota, distancias):

  custo = 0
  k = len(rota)

  for i in range(k-1):
    custo += distancias[rota[i]][rota[i+1]]
  
  return custo


''' Função que calcula a distância percentual de uma solução em relação a uma solução melhor
    Entrada: custo = valor de uma solução calculada
             custoMelhorSol = valor da melhor solução disponível
    Saida: gap = percentual de distância entre as soluções '''
def gap(custo, custoMelhorSol):
  gap = (custo - custoMelhorSol) / custoMelhorSol * 100
  return gap

''' Função que verifica se um rota não quebra a restrição de capacidade do veículo
    Entrada: rota = [ nós ] listas com a ordem de visitação de nós nas rotas 
             demandas = lista de demandas dos nós, id do nó = índice da lista
             capacVeiculo = capacidade de carga do veículo
    Saida: retorna True se a solução for válida, ou False, caso contŕario ''' 
def verificaRestricaoCapacidade(rota, demandas, capacVeiculo):

  demandaRota = 0

  for no in rota:
    
    if demandaRota > capacVeiculo:
        return False

    if no == 0:
      demandaRota = 0
    else:
      demandaRota += demandas[no]

  return True

''' Função que verifica e corrige a lista de rotas se houve redução no numero de rotas
    Entrada: rota = [ nós ] listas com a ordem de visitação de nós nas rotas 
    Saida: rota = [ nós ] listas com a ordem de visitação de nós nas rotas reorganizada '''
def verificaReducaoRotas(rota):
  
  reduz = True
  while reduz == True:
    reduz = False
    for i in range(0, len(rota)-1):
      if rota[i] == 0 and rota[i+1] == 0:
        del rota[i]
        reduz = True
        break
  
  return rota


  ''' Função que converte um lista com as rotas em um dicionario de rotas
    Entrada: rota = [ nós ] listas com a ordem de visitação de nós nas rotas 
    Saida: dicionario = {id_rota: [ clientes ]} dicionário com as listas de clientes de cada rota '''
def converteRotaEmDicionario(rota):
  
  dicionario = {}
  numRota = 0
  
  for no in rota[:-1]:
    if no == 0:
      numRota += 1
      dicionario[numRota] = []
    else:
      dicionario[numRota].append(no)
  
  return dicionario
