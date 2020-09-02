from Entrada import CAMINHO_DATASET, EXTENSAO_DATASET

''' Função que faz a leitura dos dados de arquivo de dataset
    Entrada: nome = nome do arquivo de dataset
    Saida: qtdeNos = N quantidade de nós
           capacVeiculo = Q capacidade de garga do veículo
           coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos nós, chave = id do nó
           demandas = lista de demandas dos nós, id do nó = índice da lista '''
def leitura(nome):

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