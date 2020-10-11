from matplotlib import pyplot as plt
from EntradaSaida import CAMINHO_DATASET, EXTENSAO_DATASET, TAMANHO_PONTO, PROPORCAO_PONTO, CAMINHO_VISUALIZACAO, DPI, TAM_FONTE_LEGENDA, TAMANHO_ROTULO, TAMANHO_BORDA_PONTO, POSICAO_ROTULO, TXT_CLIENTE, TXT_DEPOSITO, COR_CLIENTE, COR_DEPOSITO, COR_BORDA

''' Função que faz a leitura dos dados de arquivo de dataset
    Entrada: nome = nome da instância
    Saida: qtdeNos = N quantidade de nós
           capacVeiculo = capacidade de carga do veículo
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
             nome = nome do arquivo e titulo
             tipoRotulo = indicador de qual rótulo de ser adicionado a imagem da instância ('id', 'dem' ou 'semRot')
             demandas = [] lista de demandas dos nós, id do nó = índice da lista
             pesos = lista coms os pesos (demandas) de cada ponto (assume lista vazia se não passado como argumento) '''
def plotDataset(coordenadas, nome, tipoRotulo, demandas,  pesos = []):

  pesos = TAMANHO_PONTO if pesos == [] else [p * PROPORCAO_PONTO for p in pesos[1:]]

  x = [no[0] for no in coordenadas.values()]
  y = [no[1] for no in coordenadas.values()]

  plt.scatter(x[1:], y[1:], s = pesos, label = TXT_CLIENTE, color = COR_BORDA, facecolor= COR_CLIENTE, marker = '.', linewidths = TAMANHO_BORDA_PONTO)
  plt.scatter(x[0], y[0], s = TAMANHO_PONTO, label = TXT_DEPOSITO, color = COR_BORDA, facecolor = COR_DEPOSITO, marker = '.', linewidths = TAMANHO_BORDA_PONTO)

  if tipoRotulo == 'dem':
    rotulo = [str(d) for d in demandas]
  elif tipoRotulo == 'id':
    rotulo = [str(i) for i, d in enumerate(demandas)]

  if tipoRotulo == 'dem' or tipoRotulo == 'id':
    for no in coordenadas:
      plt.annotate(rotulo[no], (coordenadas[no][0] + POSICAO_ROTULO, coordenadas[no][1] + POSICAO_ROTULO), fontsize = TAMANHO_ROTULO)
  
  plt.title(nome)
  plt.legend(loc = 'upper left', bbox_to_anchor=(1.01, 1.0125), fontsize = TAM_FONTE_LEGENDA, fancybox = False, edgecolor = 'black')

  plt.savefig(CAMINHO_VISUALIZACAO + nome, dpi=DPI, bbox_inches='tight')
  plt.clf()


''' Função que imprime dados de um dataset
    Entrada: qtdeNos = quantidade de nós (clientes + depósito)
             capacVeiculo = capacidade de carga do veículo
             coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos nós
             demandas = lista de demandas dos nós '''
def printDataset(qtdeNos, capacVeiculo, coordenadas, demandas):
  
  print('Qtde nós: ' + str(qtdeNos))
  print('Capacidade: ' + str(capacVeiculo))
  print('Coordenadas:' + str(coordenadas))
  print('Demandas: ' + str(demandas)) 
