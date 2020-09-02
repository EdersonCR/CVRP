from matplotlib import pyplot as plt
from Saida import TAMANHO_PONTO, TXT_PESO, PROPORCAO_PONTO, CAMINHO_IMAGEM, DPI, EXTENSAO_MATRIZ_DIST, CAMINHO_SOLUCAO

''' Função que salva imagem com os pontos plotados num gráfico 
    Entrada: coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos pontos
             nome = nome do arquivo de imagem que será criado
             pesos = lista coms os pesos de cada ponto (assume lista vazia se não passado como argumento) '''
def plotPontos(coordenadas, nome, pesos = []):

  n = len(coordenadas)

  nome += TXT_PESO if pesos != [] else ''
  pesos = TAMANHO_PONTO if pesos == [] else [p * PROPORCAO_PONTO for p in pesos[1:]]

  x = [coordenadas[i][0] for i in range(n)]
  y = [coordenadas[i][1] for i in range(n)]

  plt.title(nome)
  plt.scatter(x[1:], y[1:], color="g", marker=".", s=pesos)
  plt.scatter(x[0], y[0], color="r", marker=".", s=TAMANHO_PONTO)

  plt.savefig(CAMINHO_IMAGEM + nome, dpi=DPI)

''' Função que salva a matriz de distâncias 
    Entrada: matriz = matriz de distancias
             nome = nome do arquivo que será salvo '''
def matrizDistancia(matriz, nome):

  string = '\n'.join(' '.join('{:-8.3f}'.format(dado) for dado in linha) for linha in matriz)
  
  nome += EXTENSAO_MATRIZ_DIST
  arqSaida = open (CAMINHO_SOLUCAO + nome, 'w+')
  arqSaida.write(string)
  arqSaida.close()