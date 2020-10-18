from Calculo import calculo as calc

''' Função que troca de dois elementos de uma lista e retorna uma nova lista
    Entrada: lista = []
             i, j = indice dos elementos que serão trocados entre si
    Saida: novaLista = [] nova lista com elementos trocados '''
def troca2elem(lista, i, j):

  novaLista = lista.copy()
  novaLista[i] = lista[j]
  novaLista[j] = lista[i]

  return novaLista


''' Função que troca de três elementos de uma lista e retorna uma nova lista
    Entrada: lista = []
             i, j, k = indice dos elementos que serão trocados entre si
    Saida: novaLista = [] nova lista com elementos trocados '''
def troca3elem(lista, i, j, k):
  
  novaLista = lista.copy()
  novaLista[i] = lista[k]
  novaLista[j] = lista[i]
  novaLista[k] = lista[j]

  return novaLista


''' Função que executa uma heuristica first improvement para refinar uma solução para CVRP
    Entrada: capacVeiculo = capacidade de carga do veículo
             demandas = lista de demandas dos nós
             distancias = {id: [ distancias ]} dicionario com as listas das distancias entre os pontos
             iteracaoMax = limite máximo de iterações sem melhoria que a heuristica realiza
    Saida: rota = [ nós ] listas de nós a serem percorridos nas rotas
           paradaLimiteIteracao = indicador se o refinamento parou devido a atingir limite de iterações máximo ou não '''
def heuristicaRefinamento(capacVeiculo, demandas, distancias, rota, iteracaoMax):

  iteracao = 0
  paradaLimiteIteracao = False
  melhoria2elem = True
  melhoria3elem = True
  ordem = 0
  custoRota = calc.funcaoObjetivo(rota, distancias)
  novaRota = []

  while melhoria2elem == True or melhoria3elem == True:
    
    # Alterar a ordem de exploração a cada passo
    if ordem == 0:
      inicio = 1
      fim = len(rota) - 3
      passo = 1
    else:
      inicio = len(rota) - 2
      fim = 2
      passo = -1

    melhoria3elem = False

    for i in range(inicio, fim, passo):
      for j in range(i + passo, fim + passo, passo):
        for k in range(j + passo, fim + passo + passo, passo):
          
          novaRota = troca3elem(rota, i, j, k)

          if calc.verificaRestricaoCapacidade(novaRota, demandas, capacVeiculo) == 1:
            
            iteracao += 1
            if iteracao > iteracaoMax:
              break
            
            custoNovaRota = calc.funcaoObjetivo(novaRota, distancias)

            if custoNovaRota < custoRota:
              rota = novaRota.copy()
              custoRota = custoNovaRota
              melhoria3elem = True
              iteracao = 0
              break

        if iteracao > iteracaoMax or melhoria3elem == True:
          break

      if iteracao > iteracaoMax or melhoria3elem == True:
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

    melhoria2elem = False

    # Percorre os visinhos buscando uma solução melhor
    # Escolhe o primeiro vizinho que seja melhor que a solução atual
    for i in range(inicio, fim, passo):
      for j in range(i + passo, fim + passo, passo):
          
        novaRota = troca2elem(rota, i, j)

        if calc.verificaRestricaoCapacidade(novaRota, demandas, capacVeiculo) == True:
          
          iteracao += 1
          if iteracao > iteracaoMax:
            break

          custoNovaRota = calc.funcaoObjetivo(novaRota, distancias)
          
          if custoNovaRota < custoRota:
            rota = novaRota.copy()
            custoRota = custoNovaRota
            melhoria2elem = True
            iteracao = 0
            break
  
      if iteracao > iteracaoMax or melhoria2elem == True:
        break

  if iteracao > iteracaoMax:
    paradaLimiteIteracao = True

  rota = calc.verificaReducaoRotas(rota)

  return (rota, paradaLimiteIteracao)
