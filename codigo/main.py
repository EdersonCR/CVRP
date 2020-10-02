import sys
from time import *
from EntradaSaida import (dataset as dt, distancia as dist, solucao as sol)
from Preprocessamento import preprocessamento as pre
from Construcao import construcao as con
from Refinamento import refinamento as ref
from Calculo import calculo as calc

''' Função principal que executa um método heuristico de otimização em uma instância de CVRP
    Entrada: instancia = nome da instância (sem extensão)
             metodoConstrucao = indicador de qual heuristica contrutiva sera executada ('gul' ou 'ale')
             refinamento = indicador se o algortmo deve realizar metodo refinamento da solucao ('comRef' ou 'semRef')
             imagem = indicador se deve ser gerada as imagens da instância plotadas ('comImg'  ou 'semImg')
             rotulo = indicador se a imagem da instância deve ser gerada com rótulo nos nós ('comRot' ou 'semRot') '''
def main(instancia, metodoConstrucao, refinamento, imagem, rotulo):

  # Entrada de dados
  (qtdeNos, capacVeiculo, coordenadas, demandas) = dt.leituraDataset(instancia)
  (custoMelhorSol, solOtimaMelhorSol, qtdeRotasMelhorSol, rotasMelhorSol) = sol.leituraMelhorSolucao(instancia)
  
  # Preprocessamento
  distancias = pre.geraDicionarioDistancia(coordenadas)

  t_inicio = time()

  # Heristica construtiva
  rotas = con.heristicaConstrutiva(metodoConstrucao, qtdeNos, capacVeiculo, demandas, distancias)

  # Heuristica de refinamento
  if refinamento == 'comRef':
    rotas = ref.heuristicaRefinamento(qtdeNos, capacVeiculo, demandas, distancias, rotas)

  t_total = time() - t_inicio

  custo = calc.funcaoObjetivo(rotas, distancias)
  gap = calc.gap(custo, custoMelhorSol)

  # Salvar dados em arquivo
  complementoNomeArq = '_' + metodoConstrucao + '_' + refinamento
  sol.saveSolucao(custo, t_total, rotasMelhorSol, instancia + complementoNomeArq)
  sol.tabulacaoResultado(instancia, complementoNomeArq, custo, t_total, custoMelhorSol, solOtimaMelhorSol, gap, rotas)

  if imagem == 'comImg':
    dt.plotDataset(coordenadas, instancia, rotulo)
    sol.plotSolucao(coordenadas, rotas, instancia + complementoNomeArq, rotulo)
    sol.plotSolucao(coordenadas, rotasMelhorSol, instancia + '_melhor', rotulo)
    
''' Chamada da função main()
  Parâmetros: [1]nomeInstancia, [2]metodoConstrucao, [3]realizarRefinamento, [4]gerarImagens, [5]gerarRotuloImagens'''
if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
