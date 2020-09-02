''' Função que imprime dados de um dataset
    Entrada: qtdeNos = N quantidade de nós
             capacVeiculo = Q capacidade de garga do veículo
             coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos nós
             demandas = lista de demandas dos nós '''
def printDadosDataset(qtdeNos, capacVeiculo, coordenadas, demandas):
  
  print('Qtde nós: ' + str(qtdeNos))
  print('Capacidade: ' + str(capacVeiculo))
  print('Coordenadas:' + str(coordenadas))
  print('Demandas: ' + str(demandas)) 

''' Função que imprime na tela uma matriz de distâncias
    Entrada: matriz = matriz de distancias '''
def printMatrizDistancia(matriz):
  
  print('Matriz de distâncias:')
  print('\n'.join(' '.join('{:-8.3f}'.format(dado) for dado in linha) for linha in matriz))  