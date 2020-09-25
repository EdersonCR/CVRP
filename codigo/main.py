import sys
from time import time, sleep
from EntradaSaida import (dataset as dt, distancia as dist, solucao as sol)
from Preprocessamento import preprocessamento as pre
from Calculo import calculo as calc

''' Função principal que executa um método heuristico de otimização em uma instância de CVRP
    Entrada: instancia = Nome da instância (sem extensão)
             imagem = Indicador se deve ser gerada as imagens da instância (se imagem = 'comImg' gera imagens)
             rotulo = Indicador se a imagem da instância de ser gerada com rótulo nos nós (se rotulo = 'comRot' gera rotulos) '''
def main(instancia, imagem, rotulo):

  # Entrada de dados
  (qtdeNos, capacVeiculo, coordenadas, demandas) = dt.leituraDataset(instancia)
  (custoMelhor, solOtimaMelhor, qtdeRotasMelhor, rotasMelhor) = sol.leituraMelhorSolucao(instancia)

  # Preprocessamento
  distancias = pre.geraDicionarioDistancia(coordenadas)

  # Calculo funcação objetivo
  t_inicio = time()

  custo = calc.funcaoObjetivo(rotasMelhor, distancias)
  sleep(qtdeNos/1000)

  gap = calc.gap(custo, custoMelhor)
  
  t_total = time() - t_inicio

  # Salvar dados em arquivo
  #sol.saveSolucao(custo, t_total, rotasMelhor, instancia)
  sol.tabulacaoResultado(instancia, custo, t_total, custoMelhor, solOtimaMelhor, gap, rotasMelhor)

  if imagem == 'comImg':
    dt.plotDataset(coordenadas, instancia, rotulo)
    dt.plotDataset(coordenadas, instancia, rotulo, demandas)
    sol.plotSolucao(coordenadas, rotasMelhor, instancia, rotulo)
    sol.plotSolucao(coordenadas, rotasMelhor, instancia, rotulo, demandas)
    
''' Chamada da função main()
  Parâmetros: [1]nomeInstancia, [2]gerarImagens, [3]gerarRotuloImagens'''
if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3])
