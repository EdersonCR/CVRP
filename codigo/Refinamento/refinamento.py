from Calculo import calculo as calc
from Refinamento import ITERACAO_MAX

''' Função que realiza um troca de dois elementos de uma lista
    Entrada: lista = []
             i, j = indice dos elementos que serão trocados
    Saida: lista = [] com elementos trocados '''
def troca2elem(lista, i, j):
  
  aux = lista[i]
  lista[i] = lista[j]
  lista[j] = aux

  return lista


''' Função que realiza um troca de três elementos de uma lista
    Entrada: lista = []
             i, j, k = indice dos elementos que serão trocados entre si (i <- k, j <- i, k <- j)
    Saida: lista = [] com elementos trocados '''
def troca3elem(lista, i, j, k):
  
  aux1 = lista[i]
  aux2 = lista[j]
  lista[i] = lista[k]
  lista[j] = aux1
  lista[k] = aux2

  return lista


''' Função que executa uma heuristica first improvement 2-opt para refinar uma solução para CVRP
    Entrada: capacVeiculo = capacidade de carga do veículo
             demandas = lista de demandas dos nós, id do nó = índice da lista
             distancias = {id: [ distancias ]} dicionario com as listas das distancias entre os pontos
    Saida: rota = [ nós ] listas de nós a serem percorridos nas rotas '''
def heuristicaRefinamento(capacVeiculo, demandas, distancias, rota):
  
  iteracaoMax = ITERACAO_MAX
  iteracao = 0
  troca = True
  ordem = 0
  custoRota = calc.funcaoObjetivo(rota, distancias)
  novaRota = []

  # Enquanto encontrar uma solução melhor e não atingir o limite máximo de iterações
  while troca == True:
    
    troca = False

    novaRota = rota.copy()

    if ordem == 0:
      inicio = 1
      fim = len(rota) - 3
      passo = 1
    else:
      inicio = len(rota) - 2
      fim = 2
      passo = -1

    # Percorre os visinhos buscando uma solução melhor
    # Escolhe o primeiro vizinho que seja melhor que a solução atual
    for i in range(inicio, fim, passo):
      for j in range(i + passo, fim + passo, passo):
        for k in range(j + passo, fim + passo + passo, passo):
          
          novaRota = troca3elem(novaRota, i, j, k)
          iteracao += 1

          if iteracao <= iteracaoMax:
            break
      
          # Verifica se a solução vizinha é válida
          if calc.verificaSolucaoValida(novaRota, demandas, capacVeiculo) == 1:
            custoNovaRota = calc.funcaoObjetivo(novaRota, distancias)
            
            # Se a solução vizinha for melhor, altera a solução para esse vizinho
            if custoNovaRota < custoRota:
              rota = novaRota.copy()
              custoRota = custoNovaRota
              troca = True
              break

        else:
          continue
        break
      else:
        continue
      break

    # Alterar a ordem de exploração a cada passo
    if ordem == 0:
      inicio = 1
      fim = len(rota) - 2
      ordem = 1
    else:
      inicio = len(rota) - 2
      fim = 1
      ordem = 0

    novaRota = rota.copy()

    # Percorre os visinhos buscando uma solução melhor
    # Escolhe o primeiro vizinho que seja melhor que a solução atual
    for i in range(inicio, fim, passo):
      for j in range(i + passo, fim + passo, passo):
          
        iteracao += 1
        novaRota = troca2elem(novaRota, i, j)

        if iteracao > iteracaoMax:
          break
      
        # Verifica se a solução vizinha é válida
        if calc.verificaSolucaoValida(novaRota, demandas, capacVeiculo) == 1:
          custoNovaRota = calc.funcaoObjetivo(novaRota, distancias)
          
          # Se a solução vizinha for melhor, altera a solução para esse vizinho
          if custoNovaRota < custoRota:
            rota = novaRota.copy()
            custoRota = custoNovaRota
            troca = True
            break
  
      else:
        continue
      break

  if iteracao > iteracaoMax:
    print('Limite de iterações ultrapssado.')

  # Verifica se houve redução no nº de rotas
  reduz = True
  while reduz == True:
    reduz = False
    for i in range(0, len(rota)-1):
      if rota[i] == 0 and rota[i+1] == 0:
        print(f'{i} {i+1}')
        del rota[i]
        reduz = True
        break

  return rota
