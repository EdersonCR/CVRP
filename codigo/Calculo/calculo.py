from math import *

''' Função que calcula a distância entre dois pontos (arredonda o valor para o inteiro mais próximo)
    Entrada: pontoA = (x, y) coordenasdas x e y do ponto A 
             pontoB = (x, y) coordenasdas x e y do ponto A 
    Saida: distancia = distância entre os pontos A e B'''
def distanciaPontos(pontoA, pontoB):
  distancia = int(round(sqrt((pontoB[0] - pontoA[0]) ** 2 + (pontoB[1] - pontoA[1]) ** 2)))
  return distancia


''' Função que calcula o somatório das distâncias de todas as rotas
    Entrada: rotas = {id_rota: [ nós ]} dicionário com as listas de nós das rotas 
             distancias = {id: [ distancias ]} dicionario com as listas das distancias entre os pontos 
    Saida: custo = somatório das distâncias de todas as rotas'''
def funcaoObjetivo(rotas, distancias):

  custo = 0

  for rota in rotas.values():
    k = len(rota)
    for i in range(k-1):
      custo += distancias[rota[i]][rota[i+1]]

    custo += distancias[0][rota[0]]
    custo += distancias[rota[-1]][0]
  
  return custo


''' Função que calcula a distância percentual de uma solução em relação a uma solução melhor
    Entrada: custo = valor de uma solução calculada
             custoMelhorSol = valor da melhor solução disponível
    Saida: gap = percentual de distância entre as soluções '''
def gap(custo, custoMelhorSol):
  gap = (custo - custoMelhorSol) / custoMelhorSol * 100
  return gap