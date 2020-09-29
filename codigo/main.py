import sys
from time import time
from EntradaSaida import (dataset as dt, distancia as dist, solucao as sol)
from Preprocessamento import preprocessamento as pre
from Calculo import calculo as calc

''' Função principal que executa um método heuristico de otimização em uma instância de CVRP
    Entrada: instancia = nome da instância (sem extensão)
             imagem = indicador se deve ser gerada as imagens da instância plotadas (se imagem = 'comImg' gera imagens)
             rotulo = indicador se a imagem da instância deve ser gerada com rótulo nos nós (se rotulo = 'comRot' gera rotulos) '''
def main(instancia, imagem, rotulo):

  # Entrada de dados
  (qtdeNos, capacVeiculo, coordenadas, demandas) = dt.leituraDataset(instancia)
  (custoMelhorSol, solOtimaMelhorSol, qtdeRotasMelhorSol, rotasMelhorSol) = sol.leituraMelhorSolucao(instancia)
  
  # Preprocessamento
  distancias = pre.geraDicionarioDistancia(coordenadas)

  # Calculo funcação objetivo
  t_inicio = time()

  custo = calc.funcaoObjetivo(rotasMelhorSol, distancias)

  gap = calc.gap(custo, custoMelhorSol)
  
  t_total = time() - t_inicio

  # Salvar dados em arquivo
  sol.saveSolucao(custo, t_total, rotasMelhorSol, instancia)
  sol.tabulacaoResultado(instancia, custo, t_total, custoMelhorSol, solOtimaMelhorSol, gap, rotasMelhorSol)

  if imagem == 'comImg':
    dt.plotDataset(coordenadas, instancia, rotulo)
    dt.plotDataset(coordenadas, instancia, rotulo, demandas)
    sol.plotSolucao(coordenadas, rotasMelhorSol, instancia, rotulo)
    sol.plotSolucao(coordenadas, rotasMelhorSol, instancia, rotulo, demandas)
    
''' Chamada da função main()
  Parâmetros: [1]nomeInstancia, [2]gerarImagens, [3]gerarRotuloImagens'''
if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3])
