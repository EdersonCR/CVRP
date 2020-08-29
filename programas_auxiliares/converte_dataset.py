import sys
import os

''' Função que converte os datasets para um formato simplificado
    Entrada: caminhoEntrada = caminho relativo do diretório dos datasets que serão convertidos
             caminhoSaida = caminho relativo do diretório onde serão salvos os datasets convertidos '''
def converte_dataset(caminhoEntrada, caminhoSaida):

  nomes = [nome for nome in os.listdir(caminhoEntrada)]

  for nome in nomes:
    
    arqEntrada = open(caminhoEntrada + '/' + nome, 'r')
    arqSaida = open(caminhoSaida + '/' + nome, 'w+')

    coord = 0
    demanda = 0
    depot = 0

    for line in arqEntrada:

      if line.find('DIMENSION') != -1:
        l = [s for s in line.split() if s.isdigit()]
        arqSaida.write(l[0] + '\n')

      if line.find('CAPACITY') != -1:
        l = [s for s in line.split() if s.isdigit()]
        q = l[0]
        arqSaida.write(l[0] + '\n')

      if line.find('-1') != -1:
        depot = 0

      if depot == 1:
        l = [s for s in line.split() if s.isdigit()]
        a = l[0]

      if line.find('DEPOT_SECTION') != -1:
        demanda = 0
        depot = 1

      if demanda == 1:
        l = [s for s in line.split()]
        l[0] = str(int(l[0]) - 1)
        arqSaida.write(l[0] + ' ' + l[1] + '\n')

      if line.find('DEMAND_SECTION') != -1:
        coord = 0
        demanda = 1
        
      if coord == 1:
        l = [s for s in line.split()]
        l[0] = str(int(l[0]) - 1)
        arqSaida.write(l[0] + ' ' + l[1] + ' ' + l[2] + '\n')

      if line.find('NODE_COORD_SECTION') != -1:
        coord = 1

    if(a == '1'):
      print('Arquivo' + nome + ' convertido com sucesso')
    else:
      print('[Erro]: Arquivo ' + nome + ' possui um armazem diferente de 1')

    arqEntrada.close()
    arqSaida.close()

# Chamada da função converte_dataset()
# Parãmetros: [1]caminhoEntrada, [2]caminhoSaida
converte_dataset(sys.argv[1], sys.argv[2])

'''
Formato do dataset de entrada:
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

Formato do dataset convertido:
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
