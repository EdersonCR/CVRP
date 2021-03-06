import pandas as pd
from matplotlib import pyplot as plt
from EntradaSaida import CAMINHO_MELHOR_SOLUCAO, TXT_SOLUCAO, EXTENSAO_SOLUCAO, TXT_PESO, TAMANHO_PONTO, PROPORCAO_PONTO, POSICAO_ROTULO, POSICAO_ROTULO, TAMANHO_ROTULO, TAM_FONTE_LEGENDA, CAMINHO_VISUALIZACAO, DPI, TAMANHO_LINHA_ROTA, TAMANHO_BORDA_PONTO, LIMITE_PLOT_CAMINHO_DEPOSITO, CAMINHO_SOLUCAO, EXTENSAO_TABELA, CAMINHO_TABELA, TXT_TABELA, COR_DEPOSITO, COR_BORDA

''' Função que faz a leitura dos dados de arquivo que contém a melhor solução
    Entrada: nome = nome a instância
    Saida: custo = custo total da solução (distância)
           solOtima = Indicador se é a solução ótima ou não
           qtdeRotas = quantidade de rotas da solução
           rotas = {id_rota: [ nós ]} dicionário com as listas de nós das rotas '''
def leituraMelhorSolucao(nome):

  arqEntrada = open(CAMINHO_MELHOR_SOLUCAO + nome + EXTENSAO_SOLUCAO, 'r')
    
  dado = arqEntrada.readline().split()
  custo = int(dado[1])
  dado = arqEntrada.readline().split()
  solOtima = dado[1]
  
  rotas = {}

  qtdeRotas = 0
  for linha in arqEntrada:
    qtdeRotas += 1
    rotas[qtdeRotas] = [int(dado) for dado in linha.split() if dado.isdigit()]

  return (custo, solOtima, qtdeRotas, rotas)


''' Função que salva imagem com os clientes, o deposito e as rotas plotados em um gráfico 
    Entrada: coordenadas = {id: (x, y)} dicionário com as coordenas x e y dos pontos
             rotas = {id_rota: [ nós ]} dicionário com as listas de nós das rotas
             nome = nome da intânciao
             rotulo = indicador se a imagem deve ser gerada com rótulo nos nós (se rotulo = 'comRot' gera rotulos)
             pesos = lista coms os pesos (demandas) de cada ponto (assume lista vazia se não passado como argumento) '''
def plotSolucao(coordenadas, rotas, nome, rotulo, pesos = []):

  nome += '-' + TXT_PESO if pesos != [] else ''
  nome += '-' + TXT_SOLUCAO

  for rota in rotas:
    x = [coordenadas[no][0] for no in rotas[rota]]
    y = [coordenadas[no][1] for no in rotas[rota]]
    p = [pesos[no] * PROPORCAO_PONTO for no in rotas[rota]] if pesos != [] else TAMANHO_PONTO
    
    cor = f'C{rota!s}'

    # Se a quantidade de rotas é muito grande, não plota as linhas que ligam os clientes ao depósito
    if len(rotas) < LIMITE_PLOT_CAMINHO_DEPOSITO:
      plt.plot([x[0], coordenadas[0][0]], [y[0], coordenadas[0][1]], linestyle = '--', color = cor, linewidth = TAMANHO_LINHA_ROTA, zorder = 1)
      plt.plot([x[-1], coordenadas[0][0]], [y[-1], coordenadas[0][1]], linestyle = '--', color = cor, linewidth = TAMANHO_LINHA_ROTA, zorder = 1)

    # Plota os clientes e as linhas das rotas
    plt.plot(x, y, label = f'Rota {rota!s}', color = cor, linewidth = TAMANHO_LINHA_ROTA, zorder = 1)
    plt.scatter(x, y, s = p, color = COR_BORDA, facecolor = cor, marker = '.', linewidths = TAMANHO_BORDA_PONTO, zorder = 2)
    
  # Plota o ponto do depósito
  plt.scatter(coordenadas[0][0], coordenadas[0][1], s = TAMANHO_PONTO, color = COR_BORDA, facecolor = COR_DEPOSITO, marker = '.', linewidths = TAMANHO_BORDA_PONTO, zorder = 2)

  if rotulo == 'comRot':
    for no in coordenadas:
      plt.annotate(str(no), (coordenadas[no][0] + POSICAO_ROTULO, coordenadas[no][1] + POSICAO_ROTULO), fontsize = TAMANHO_ROTULO)

  plt.title(nome)
  plt.legend(loc = 'upper left', bbox_to_anchor=(1.01, 1.0125), fontsize = TAM_FONTE_LEGENDA, fancybox = False, edgecolor = 'black')

  plt.savefig(CAMINHO_VISUALIZACAO + nome, dpi=DPI, bbox_inches='tight')
  plt.clf()


''' Função que imprime dados de uma solução
    Entrada: custo = custo total (distância) da solução
             tempo = tempo gasto para calcular a solução
             rotas = {id_rota: [ nós ]} dicionário com as listas de nós das rotas '''
def printSolucao(custo, tempo, rotas):
  
  print(f'Custo: {custo!s}')
  print(f'Tempo: {tempo:.4f}')
  for rota in rotas:
    print(f'Rota #{rota!s}: ' + ' '.join(str(no) for no in rotas[rota]))


''' Função que salva em um arquivo os dados de uma solução calculada
    Entrada: custo = custo total (distância) da solução
             tempo = tempo gasto para calcular a solução
             rotas = {id_rota: [ nós ]} dicionário com as listas de nós das rotas 
             nome = nome da instância '''
def saveSolucao(custo, tempo, rotas, nome):
  
  string = f'Custo: {custo!s}\n'
  string += f'Tempo: {tempo:.4f}\n'

  for rota in rotas:
    string += f'Rota #{rota!s}: ' + ' '.join(str(no) for no in rotas[rota]) + '\n'

  nome += EXTENSAO_SOLUCAO
  arqSaida = open (CAMINHO_SOLUCAO + nome, 'w+')
  arqSaida.write(string)
  arqSaida.close()


''' Função que salva e agrega o resultado de uma solução em uma tabela em um arquivo
    Entrada: nome = nome da instância
             custo = custo total (distância) da solução calculada
             tempo = tempo gasto para calcuar a solução
             custoMelhorSol = custo da melhor solução disponível
             solOtima = indicador se a melhor solução é ótima ou não
             gap = valor percentual da distância da solução calculada em relação a melhor solução
             rotas = {id_rota: [ nós ]} dicionário com as listas de nós das rotas da solução calculada'''
def tabulacaoResultado(nome, custo, tempo, custoMelhorSol, solOtima, gap, rotas):
  
  resultado = pd.DataFrame({
    'Instância': [nome],
    'Custo': [custo],
    'Tempo (s)': [f'{tempo:.4f}'.replace('.',',')],
    'Melhor Solução': [custoMelhorSol],
    'Solução Ótima': [solOtima],
    'Gap (%)': [f'{gap:.2f}'.replace('.', ',')],
    'Rotas': [f'{rotas}']
  })

  resultado.to_csv(CAMINHO_TABELA + TXT_TABELA + EXTENSAO_TABELA, mode = 'a+', sep = ';', encoding='utf8', index = False, header = False)
 
