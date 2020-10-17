import pandas as pd

CAMINHO_RESULTADO = '../resultados/'
ALE_SEM_REF = 'resultado_ale_semRef.csv'
ALE_COM_REF = 'resultado_ale_comRef.csv'
GUL_SEM_REF = 'resultado_gul_semRef.csv'
GUL_COM_REF = 'resultado_gul_comRef.csv'

with open(CAMINHO_RESULTADO + ALE_SEM_REF) as arquivo:
  df_ale_sem = pd.read_csv(arquivo, sep = ';', encoding = 'utf8')
with open(CAMINHO_RESULTADO + ALE_COM_REF) as arquivo:
  df_ale_com = pd.read_csv(arquivo, sep = ';', encoding = 'utf8')
with open(CAMINHO_RESULTADO + GUL_SEM_REF) as arquivo:
  df_gul_sem = pd.read_csv(arquivo, sep = ';', encoding = 'utf8')
with open(CAMINHO_RESULTADO + GUL_COM_REF) as arquivo:
  df_gul_com = pd.read_csv(arquivo, sep = ';', encoding = 'utf8')

resultado = pd.concat([
  df_ale_sem.iloc[:,0:7],
  df_ale_com.iloc[:,4:7],  
  df_gul_sem.iloc[:,4:7], 
  df_gul_com.iloc[:,4:7]
], axis=1)

resultado = pd.concat([
  resultado.iloc[0:27],
  resultado.iloc[28:51],
  resultado.iloc[[27]],
  resultado.iloc[52:151],
  resultado.iloc[[51]],
])

with open(CAMINHO_RESULTADO + 'resultado.csv', mode = 'w+') as arquivo:
  arquivo.write(';;;;Heurística aleatória;;;;;;Heurítica gulosa;;;;;\n')
  arquivo.write(';;Melhor solução;;Sem refinamento;;;Com refinamento;;;Sem refinamento;;;Com refinamento;;\n')
  arquivo.write('Instância;n;Sol.;Opt;Sol.;T (s);%gap;Sol.;T (s);%gap;Sol.;T (s);%gap;Sol.;T (s);%gap\n')
  resultado.to_csv(arquivo, sep = ';', encoding='utf8', index = False, header = False)
