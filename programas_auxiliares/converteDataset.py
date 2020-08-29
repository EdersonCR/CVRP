import sys
import os

''' 
Função que converte os arquivo para um formato simplificado
Entrada: caminhoEntrada = caminho do diretório dos arquivos que serão convertidos
         caminhoSaida = caminho do diretório onde serão salvos os arquivos convertidos

Formato do arquivo de entrada:
  NAME : <nome_do_arquivo>
  COMMENT : <comentário_sobre_a_instancia>
  TYPE : <tipo_de_problema>
  DIMENSION : <N>
  EDGE_WEIGHT_TYPE : <tipo_dado_da_coordenada> 
  CAPACITY : <capacidade>
  NODE_COORD_SECTION 
  <id_no_1> <coord_x_no_1> <coord_y_no_1>
  <id_no_2> <coord_x_no_2> <coord_y_no_2>
  ...
  <id_no_N> <demanda_no_N> <coord_y_no_N>
  DEMAND_SECTION 
  <id_no_1> <demanda_no_1>
  <id_no_2> <demanda_no_2>
  ...
  <id_no_N> <demanda_no_N>
  DEPOT_SECTION 
  <id_no_deposito>  
  -1  
  EOF 

Formato do arquivo convertido:
  <N>
  <capacidade>
  <id_no_1> <coord_x_no_1> <coord_y_no_1>
  <id_no_2> <coord_x_no_2> <coord_y_no_2>
  ...
  <id_no_N> <coord_x_no_N> <coord_y_no_N>
  <id_no_1> <demanda_no_1>
  <id_no_2> <demanda_no_2>
  ...   
  <id_no_N> <demanda_no_N> 
'''
def converteDataset(caminhoEntrada, caminhoSaida):

  nomes = [nome for nome in os.listdir(caminhoEntrada) if nome[-4:] == '.vrp']
  nomes.sort()

  for nome in nomes:

    arqEntrada = open(caminhoEntrada + '/' + nome, 'r')
    arqSaida = open(caminhoSaida + '/' + nome, 'w+')

    coord = 0
    demanda = 0
    deposito = 0
    dados = ''

    for linha in arqEntrada:

      if linha.find('DIMENSION') != -1:
        l = [s for s in linha.split() if s.isdigit()]
        dados += l[0] + '\n'

      if linha.find('CAPACITY') != -1:
        l = [s for s in linha.split() if s.isdigit()]
        dados += l[0] + '\n'

      if linha.find('-1') != -1:
        deposito = 0

      if deposito == 1:
        l = [s for s in linha.split() if s.isdigit()]
        d = l[0]

      if linha.find('DEPOT_SECTION') != -1:
        demanda = 0
        deposito = 1

      if demanda == 1:
        l = [s for s in linha.split()]
        l[0] = str(int(l[0]) - 1)
        dados += l[0] + ' ' + l[1] + '\n'

      if linha.find('DEMAND_SECTION') != -1:
        coord = 0
        demanda = 1
        
      if coord == 1:
        l = [s for s in linha.split()]
        l[0] = str(int(l[0]) - 1)
        dados += l[0] + ' ' + l[1] + ' ' + l[2] + '\n'

      if linha.find('NODE_COORD_SECTION') != -1:
        coord = 1

    if d != '1':
      print('[Erro]: Arquivo ' + nome + ' possui mais de um deposito')
    elif arqSaida.write(dados):
      print('Arquivo ' + nome + ' convertido com sucesso')
    else:
      print('[Erro]: Falha ao escrever no ' + nome + ' convertido')
      
    arqEntrada.close()
    arqSaida.close()

''' Chamada da função converteDataset()
    Parâmetros: [1]caminhoEntrada, [2]caminhoSaida '''
converteDataset(sys.argv[1], sys.argv[2])