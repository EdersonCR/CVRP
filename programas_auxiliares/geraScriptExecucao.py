import sys
import os
import platform

''' Função que gera um arquivo .bat de execução dos datasets
    Entrada: caminhoDatasets = caminho do diretório dos datasets que serão excutados
             caminhoMain = caminho do diretório do arquivo main.py
             conjuntoDataset = letra incial dos arquivos do conjunto dos dataset ('all' para todos conjuntos) '''
def geraScriptExecucao(caminhoDatasets, caminhoMain, conjuntoDataset):

  if conjuntoDataset == 'all':
    datasets = [dataset for dataset in os.listdir(caminhoDatasets) if dataset[-4:] == '.vrp']
  else:
    datasets = [dataset for dataset in os.listdir(caminhoDatasets) if dataset[0] == conjuntoDataset and dataset[-4:] == '.vrp']
    conjuntoDataset = 'conj-' + conjuntoDataset

  datasets.sort()

  # Identifica o SO 
  sisOp = platform.system() 
  
  if sisOp == 'Linux':

    script = '#!/bin/bash\n'
    
    for dataset in datasets:
      comando = 'python3 main.py ' + dataset[:-4] + ' semImg semRot'
      script += '\necho -e "\\n' + comando + '"\n' + comando + '\n'

    script += '\necho -e "\\nTodas instâncias foram executadas"\n'
    script += 'read -p "Pressione [Enter] para fechar..."'

    extensao = '.sh'
  
  elif sisOp == 'Windows':

    script = 'echo off\n'
    
    for dataset in datasets:
      comando = 'python main.py ' + dataset[:-4] + ' semImg semRot'
      script += '\necho.\necho "' + comando + '"\n' + comando + '\n'

    script += '\necho.\necho "Todas instâncias foram executadas"\n'
    script += 'pause'

    extensao = '.bat'
  
  nome = 'executa_' + sisOp + '_' + conjuntoDataset + extensao
  arqSaida = open (caminhoMain + '/' + nome, 'w+')

  if arqSaida.write(script):
    print('Script ' + nome + ' criado com sucesso')
  else:
    print('[Erro]: Falha ao escrever no script' + nome)

  arqSaida.close()

  if sisOp == 'Linux':
    os.system('chmod +x ' + caminhoMain + '/' + nome) # Permissão para o arquivo ser um executável

''' Chamada da função geraScriptExecucao()
    Parâmetros: [1]caminhoDatasets, [2]caminhoMain, [3]conjuntoDataset '''
geraScriptExecucao(sys.argv[1], sys.argv[2], sys.argv[3])
