import sys
import os
import platform

CAMINHO_MAIN = '../codigo/'
CAMINHO_DATASETS = '../dados/datasets'

''' Função que gera um arquivo .bat de execução dos datasets
    Entrada: conjuntoDataset = letra incial dos arquivos do conjunto dos dataset ('all' para todos conjuntos)
             paramentros = string com os parametros que serão passados para a função main() para execução '''
def geraScriptExecucao(conjuntoDataset, parametros):

  extensao = ''
  script = ''
  parametros = parametros.replace('\"', '')

  if conjuntoDataset == 'all':
    datasets = [dataset for dataset in os.listdir(CAMINHO_DATASETS) if dataset[-4:] == '.vrp']
  else:
    datasets = [dataset for dataset in os.listdir(CAMINHO_DATASETS) if dataset[0] == conjuntoDataset and dataset[-4:] == '.vrp']
    conjuntoDataset = 'conj-' + conjuntoDataset

  datasets.sort()

  # Identifica o SO 
  sisOp = platform.system() 
  
  if sisOp == 'Linux':

    script = '#!/bin/bash\n'
    
    for dataset in datasets:
      comando = 'python3 main.py ' + dataset[:-4] + ' ' + parametros
      script += '\necho -e "\\n' + comando + '"\n' + comando + '\n'

    script += '\necho -e "\\nTodas instâncias foram executadas"\n'
    script += 'read -p "Pressione [Enter] para fechar..."'

    extensao = '.sh'
  
  elif sisOp == 'Windows':

    script = 'echo off\n'
    
    for dataset in datasets:
      comando = 'python main.py ' + dataset[:-4] + ' ' + parametros
      script += '\necho.\necho ' + comando + '\n' + comando + '\n'

    script += '\necho.\necho "Todas instâncias foram executadas"\n'
    script += 'pause'

    extensao = '.bat'
  
  nome = 'executa_' + sisOp + '_' + conjuntoDataset + '_' + parametros.replace(' ', '_') + extensao
  arqSaida = open (CAMINHO_MAIN + '/' + nome, 'w+')

  if arqSaida.write(script):
    print('Script ' + nome + ' criado com sucesso')
  else:
    print('[Erro]: Falha ao escrever no script' + nome)

  arqSaida.close()

  if sisOp == 'Linux':
    os.system('chmod +x ' + CAMINHO_MAIN + '/' + nome) # Permissão para o arquivo ser um executável

''' Chamada da função geraScriptExecucao()
    Parâmetros: [1]conjuntoDataset, [2]parametros '''
geraScriptExecucao(sys.argv[1], sys.argv[2])
