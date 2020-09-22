from matplotlib import pyplot as plt
from EntradaSaida import CAMINHO_MELHOR_SOLUCAO, TXT_SOLUCAO, EXTENSAO_SOLUCAO, TXT_PESO, TAMANHO_PONTO, PROPORCAO_PONTO, POSICAO_ROTULO, POSICAO_ROTULO, TAMANHO_ROTULO, TAM_FONTE_LEGENDA, CAMINHO_VISUALIZACAO, DPI, TAMANHO_LINHA_ROTA, TAMANHO_BORDA_PONTO, LIMITE_PLOT_CAMINHO_DEPOSITO, CAMINHO_SOLUCAO

''' Função que faz a leitura dos dados de arquivo de solução
    Entrada: nome = nome do arquivo de solução
    Saida: custo = custo total da solução (distância)
           solOtima = Indicador se é a soluçõ ótima ou não
           qtdeRotas = K quantidade de rotas da solução
           rotas = {id_rota: [ nós ]} dicionário com as listas de nós das K rotas '''
def leituraMelhorSolucao(nome):

  arqEntrada = open(CAMINHO_MELHOR_SOLUCAO + nome + EXTENSAO_SOLUCAO, 'r')
    
  dado = arqEntrada.readline().split()
  custo = float(dado[1])
  dado = arqEntrada.readline().split()
  solOtima = dado[1]
  dado = arqEntrada.readline().split()
  qtdeRotas = int(dado[1])
  
  rotas = {}

  for i in range(1, qtdeRotas + 1):
      rota = [int(dado) for dado in arqEntrada.readline().split() if dado.isdigit()]
      rotas[i] = rota

  return (custo, solOtima, qtdeRotas, rotas)


''' Função que salva imagem com os clientes, o deposito e as rotas plotados num gráfico 
    Entrada: coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos pontos
             nome = nome do arquivo de imagem que será criado
             rotas = {id_rota: [ nós ]} dicionário com as listas de nós das rotas
             pesos = lista coms os pesos de cada ponto (assume lista vazia se não passado como argumento) '''
def plotSolucao(coordenadas, nome, rotas, pesos = []):

  nome += TXT_PESO if pesos != [] else ''
  nome += TXT_SOLUCAO

  for rota in rotas:
    x = [coordenadas[no][0] for no in rotas[rota]]
    y = [coordenadas[no][1] for no in rotas[rota]]
    p = [pesos[no] * PROPORCAO_PONTO for no in rotas[rota]] if pesos != [] else TAMANHO_PONTO
    
    cor = f'C{rota!s}'

    if len(rotas) < LIMITE_PLOT_CAMINHO_DEPOSITO:
      plt.plot([x[0], coordenadas[0][0]], [y[0], coordenadas[0][1]], linestyle = '--', color = cor, linewidth = TAMANHO_LINHA_ROTA, zorder = 1)
      plt.plot([x[-1], coordenadas[0][0]], [y[-1], coordenadas[0][1]], linestyle = '--', color = cor, linewidth = TAMANHO_LINHA_ROTA, zorder = 1)

    plt.plot(x, y, label = f'Rota {rota!s}', color = cor, linewidth = TAMANHO_LINHA_ROTA, zorder = 1)
    plt.scatter(x, y, s = p, color = 'black', facecolor = cor, marker = '.', linewidths = TAMANHO_BORDA_PONTO, zorder = 2)
    
  plt.scatter(coordenadas[0][0], coordenadas[0][1], s = TAMANHO_PONTO, color = 'black', facecolor = 'red', marker = '.', linewidths = TAMANHO_BORDA_PONTO, zorder = 2)

  for no in coordenadas:
    plt.annotate(str(no), (coordenadas[no][0] + POSICAO_ROTULO, coordenadas[no][1] + POSICAO_ROTULO), fontsize = TAMANHO_ROTULO)

  plt.title(nome)
  plt.legend(loc = 'upper left', bbox_to_anchor=(1.01, 1.0125), fontsize = TAM_FONTE_LEGENDA, fancybox = False, edgecolor = 'black')

  plt.savefig(CAMINHO_VISUALIZACAO + nome, dpi=DPI, bbox_inches='tight')
  plt.clf()


''' Função que imprime dados de uma solução
    Entrada: custo = custo total (distância) da solução
             solOtima = Indicador se é a soluçõ ótima ou não
             qtdeRotas = K quantidade de rotas da solução
             rotas = {id_rota: [ nós ]} dicionário com as listas de nós das K rotas '''
def printSolucao(custo, solOtima, qtdeRotas, rotas):
  
  print(f'Custo: {custo!s}')
  print(f'Ótima: {solOtima}')
  print(f'Rotas: {qtdeRotas!s}')
  for rota in rotas:
    print(f'Rota #{rota!s}: ' + ' '.join(str(no) for no in rotas[rota]))

''' Função que salva em um arquivos os dados de uma solução
    Entrada: custo = custo total (distância) da solução
             solOtima = Indicador se é a soluçõ ótima ou não
             qtdeRotas = K quantidade de rotas da solução
             rotas = {id_rota: [ nós ]} dicionário com as listas de nós das K rotas '''
def saveSolucao(custo, solOtima, qtdeRotas, rotas, nome):
  
  string = f'Custo: {custo!s}\n'
  string += f'Ótima: {solOtima}\n'
  string += f'Rotas: {qtdeRotas!s}\n'

  for rota in rotas:
    string += f'Rota #{rota!s}: ' + ' '.join(str(no) for no in rotas[rota]) + '\n'

  nome += EXTENSAO_SOLUCAO
  arqSaida = open (CAMINHO_SOLUCAO + nome, 'w+')
  arqSaida.write(string)
  arqSaida.close()