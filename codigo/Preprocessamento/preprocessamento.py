from Calculo import calculo as calc

''' Função que cria uma matriz de distâncias
    Entrada: coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos pontos
    Saída: matriz quadratica com as distancias entre os pontos '''
def geraMatrizDistancia(coordenadas):

  n = len(coordenadas)
  matriz = [[0.0] * n for i in range(n)]

  for i in range(n):
      for j in range(i, n):
          matriz[i][j] = matriz[j][i] = calc.distanciaPontos(coordenadas[i], coordenadas[j])

  return matriz


''' Função que cria uma matriz de distâncias
    Entrada: coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos pontos
    Saída: dicionario = {id: [ distancias ]} dicionario com as listas das distancias entre os pontos'''
def geraDicionarioDistancia(coordenadas):

  dicionario = {}

  for i in coordenadas:
    dicionario[i] = [calc.distanciaPontos(coordenadas[i], coordenadas[j]) for j in coordenadas]

  return dicionario
  