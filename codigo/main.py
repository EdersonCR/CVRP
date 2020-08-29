import sys

''' Função principal que executa o método heuristicos de otimização em uma instância de CVRP
    Entrada: dataset: Nome da instância
             qtdeVeiculos: qtde de veículos disponíveis na frota (valor da melhor solução disponível)'''
def main(dataset, qtdeVeiculos):

  print(dataset + '.vrp ' + qtdeVeiculos)

''' Chamada da função converte_dataset()
    Parâmetros: [1]dataset, [2]qtdeVeiculos'''
if __name__ == '__main__':
  main(sys.argv[1], sys.argv[2])