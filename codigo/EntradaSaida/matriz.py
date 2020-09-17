from EntradaSaida import EXTENSAO_MATRIZ_DIST, CAMINHO_SOLUCAO

''' Função que salva a matriz de distâncias 
    Entrada: matriz = matriz de distancias
             nome = nome do arquivo que será salvo '''
def saveMatrizDistancia(matriz, nome):

  string = '\n'.join(' '.join('{:-8.3f}'.format(dado) for dado in linha) for linha in matriz)
  
  nome += EXTENSAO_MATRIZ_DIST
  arqSaida = open (CAMINHO_SOLUCAO + nome, 'w+')
  arqSaida.write(string)
  arqSaida.close()


''' Função que imprime na tela uma matriz de distâncias
    Entrada: matriz = matriz de distancias '''
def printMatrizDistancia(matriz):
  
  print('Matriz de distâncias:')
  print('\n'.join(' '.join('{:-8.3f}'.format(dado) for dado in linha) for linha in matriz))
