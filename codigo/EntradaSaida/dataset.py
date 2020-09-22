from matplotlib import pyplot as plt
from EntradaSaida import CAMINHO_DATASET, EXTENSAO_DATASET, TAMANHO_PONTO, TXT_PESO, PROPORCAO_PONTO, CAMINHO_VISUALIZACAO, DPI, TAM_FONTE_LEGENDA, TAMANHO_ROTULO, TAMANHO_BORDA_PONTO, POSICAO_ROTULO

''' Função que faz a leitura dos dados de arquivo de dataset
    Entrada: nome = nome do arquivo de dataset
    Saida: qtdeNos = N quantidade de nós
           capacVeiculo = Q capacidade de garga do veículo
           coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos nós, chave = id do nó
           demandas = lista de demandas dos nós, id do nó = índice da lista '''
def leituraDataset(nome):

  arqEntrada = open(CAMINHO_DATASET + nome + EXTENSAO_DATASET, 'r')
    
  qtdeNos = int(arqEntrada.readline())
  capacVeiculo = int(arqEntrada.readline())
  
  coordenadas = {}
  demandas = []

  for i in range(qtdeNos):
      infoNo = [float(dado) for dado in arqEntrada.readline().split()]
      coordenadas[int(infoNo[0])] = (infoNo[1], infoNo[2])

  for i in range(qtdeNos):
      infoNo = [int(dado) for dado in arqEntrada.readline().split()]
      demandas.append(infoNo[1])

  return (qtdeNos, capacVeiculo, coordenadas, demandas)


''' Função que salva imagem com os clientes e deposito plotados num gráfico 
    Entrada: coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos pontos
             nome = nome do arquivo de imagem que será criado
             pesos = lista coms os pesos de cada ponto (assume lista vazia se não passado como argumento) '''
def plotDataset(coordenadas, nome, pesos = []):

  nome += TXT_PESO if pesos != [] else ''
  pesos = TAMANHO_PONTO if pesos == [] else [p * PROPORCAO_PONTO for p in pesos[1:]]

  x = [no[0] for no in coordenadas.values()]
  y = [no[1] for no in coordenadas.values()]

  plt.scatter(x[1:], y[1:], s = pesos, label = 'Cliente', color = 'black', facecolor='blue', marker = '.', linewidths = TAMANHO_BORDA_PONTO)
  plt.scatter(x[0], y[0], s = TAMANHO_PONTO, label = 'Depósito', color = 'black', facecolor='red', marker = '.', linewidths = TAMANHO_BORDA_PONTO)

  for no in coordenadas:
    plt.annotate(str(no), (x[no] + POSICAO_ROTULO, y[no] + POSICAO_ROTULO), fontsize = TAMANHO_ROTULO)
  
  plt.title(nome)
  plt.legend(loc = 'upper left', bbox_to_anchor=(1.01, 1.0125), fontsize = TAM_FONTE_LEGENDA, fancybox = False, edgecolor = 'black')

  plt.savefig(CAMINHO_VISUALIZACAO + nome, dpi=DPI, bbox_inches='tight')
  plt.clf()


''' Função que imprime dados de um dataset
    Entrada: qtdeNos = N quantidade de nós
             capacVeiculo = Q capacidade de garga do veículo
             coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos nós
             demandas = lista de demandas dos nós '''
def printDataset(qtdeNos, capacVeiculo, coordenadas, demandas):
  
  print('Qtde nós: ' + str(qtdeNos))
  print('Capacidade: ' + str(capacVeiculo))
  print('Coordenadas:' + str(coordenadas))
  print('Demandas: ' + str(demandas)) 
