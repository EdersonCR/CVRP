import sys
from time import *
from EntradaSaida import (dataset as dt, solucao as sol)
from Preprocessamento import preprocessamento as pre
from Construcao import construcao as con
from Refinamento import refinamento as ref
from Calculo import calculo as calc

SEMENTE = 1968
ITERACAO_MAX = 100000

''' Função principal que executa um método heuristico de otimização em uma instância de CVRP
    Entrada: instancia = nome da instância (sem extensão)
             metodoConstrucao = indicador de qual heuristica contrutiva sera executada ('gul' ou 'ale')
             refinamento = indicador se o algortmo deve realizar metodo refinamento da solucao ('comRef' ou 'semRef')
             imagem = indicador se deve ser gerada as imagens da instância plotadas ('comImg' ou 'semImg')
             rotulo = indicador de qual rótulo de ser adicionado a imagem da instância ('id', 'dem' ou 'semRot') '''
def main(instancia, metodoConstrucao, refinamento, imagem, rotulo):
  
  (qtdeNos, capacVeiculo, coordenadas, demandas) = dt.leituraDataset(instancia)
  (custoMelhorSol, solOtimaMelhorSol, rotaMelhorSol) = sol.leituraMelhorSolucao(instancia)

  distancias = pre.geraDicionarioDistancia(coordenadas)

  t_inicio = time()

  rota = con.heuristicaConstrutiva(metodoConstrucao, qtdeNos, capacVeiculo, demandas, distancias, SEMENTE)
  
  if refinamento == 'comRef':
    rota = ref.heuristicaRefinamento(capacVeiculo, demandas, distancias, rota, ITERACAO_MAX)

  t_total = time() - t_inicio

  custo = calc.funcaoObjetivo(rota, distancias) 
  gap = calc.gap(custo, custoMelhorSol)

  complementoNomeArq = '_' + metodoConstrucao + '_' + refinamento
  rota = calc.converteRotaEmDicionario(rota)
  sol.tabulacaoResultado(instancia, qtdeNos, custoMelhorSol, solOtimaMelhorSol, custo, t_total, gap, rota, complementoNomeArq)

  if imagem == 'comImg':
    dt.plotDataset(coordenadas, instancia, rotulo, demandas)
    sol.plotSolucao(coordenadas, rota, custo, instancia + complementoNomeArq, rotulo, demandas)
    sol.plotSolucao(coordenadas, rotaMelhorSol, custoMelhorSol, instancia + '_melhor', rotulo, demandas)
    sol.saveSolucao(custo, t_total, rota, instancia + complementoNomeArq)
  
  sol.printResultadoExecução(custo, t_total)


''' Chamada da função main()
  Parâmetros: [1]nomeInstancia, [2]metodoConstrucao, [3]realizarRefinamento, [4]gerarImagens, [5]gerarRotuloImagens'''
if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
