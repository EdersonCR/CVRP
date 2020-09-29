import sys
import os

''' 
Função que converte os arquivo para um outro simplificado
Entrada: caminhoEntrada = caminho do diretório dos arquivos que serão convertidos
         caminhoSaida = caminho do diretório onde serão salvos os arquivos convertidos

Formato do arquivo de entrada:
  Route #1: <id_no_1.1> <id_no_1.2> ... <id_no_1.N>
  Route #2: <id_no_2.1> <id_no_2.2> ... <id_no_2.N>
  ...
  Route #M: <id_no_M.1> <id_no_M.2> ... <id_no_M.N>
  Cost: <distancia>

Formato do arquivo convertido:
  Custo: <distancia>
  Otima: <solOtima>
  Rota 1: <id_no_1.1> <id_no_1.2> ... <id_no_1.N>
  Rota 2: <id_no_2.1> <id_no_2.2> ... <id_no_2.N>
  ...
  Rota K: <id_no_K.1> <id_no_K.2> ... <id_no_K.N>
'''
def converteSolucao(caminhoEntrada, caminhoSaida):

  nomes = [nome for nome in os.listdir(caminhoEntrada) if nome[-4:] == '.sol']
  nomes.sort()

  for nome in nomes:

    arqEntrada = open(caminhoEntrada + '/' + nome, 'r')
    arqSaida = open(caminhoSaida + '/' + nome, 'w+')

    dados = ''
    qtdeVeiculos = 0

    n = [s for s in nome[3:].split('-') if s.isdigit()]
    n = int(n[0])
    listaOtima = [655, 548, 524, 469, 439, 420, 393, 376, 331, 322, 317, 298, 289, 284, 275, 270, 266]

    # Verifica se a solução do conjunto X é uma solucão otima 
    solOtima = 'não' if nome[0] == 'X' and n >= 256 and n not in listaOtima else 'sim'

    for linha in arqEntrada:

      if linha.find('Route') != -1:
        nos = [s for s in linha.split() if s.isdigit()]
        qtdeVeiculos += 1
        dados += 'Rota #' + str(qtdeVeiculos) + ': ' + ' '.join(no for no in nos) + '\n'

      if linha.find('Cost') != -1:
        custo = [s for s in linha.split() if s.isdigit()] 
        dados = 'Ótima: ' + solOtima + '\n' + dados 
        dados = 'Custo: ' + custo[0] + '\n' + dados

    if arqSaida.write(dados):
      print('Arquivo ' + nome + ' convertido com sucesso')
    else:
      print('[Erro]: Falha ao escrever no ' + nome + ' convertido')
      
    arqEntrada.close()
    arqSaida.close()

''' Chamada da função converteDataset()
    Parâmetros: [1]caminhoEntrada, [2]caminhoSaida '''
converteSolucao(sys.argv[1], sys.argv[2])
