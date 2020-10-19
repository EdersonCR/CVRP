import pandas as pd

CAMINHO_RESULTADO = '../resultados/'
ALE_SEM_REF = 'resultado_ale_semRef.csv'
ALE_COM_REF = 'resultado_ale_comRef.csv'
GUL_SEM_REF = 'resultado_gul_semRef.csv'
GUL_COM_REF = 'resultado_gul_comRef.csv'

def gap(custo, custoMelhorSol):
  gap = (custo - custoMelhorSol) / custoMelhorSol * 100
  return gap


with open(CAMINHO_RESULTADO + ALE_SEM_REF) as arquivo:
  df_ale_sem = pd.read_csv(arquivo, sep = ';', encoding = 'utf8')
with open(CAMINHO_RESULTADO + ALE_COM_REF) as arquivo:
  df_ale_com = pd.read_csv(arquivo, sep = ';', encoding = 'utf8')
with open(CAMINHO_RESULTADO + GUL_SEM_REF) as arquivo:
  df_gul_sem = pd.read_csv(arquivo, sep = ';', encoding = 'utf8')
with open(CAMINHO_RESULTADO + GUL_COM_REF) as arquivo:
  df_gul_com = pd.read_csv(arquivo, sep = ';', encoding = 'utf8')

df_ale_sem.rename(columns = {'Sol.': 'Sol. AS', 'T (s)': 'T (s) AS', '%gap': '%gap AS', 'Lim. Iter.': 'Lim. Iter. AS' }, inplace = True)
df_ale_com.rename(columns = {'Sol.': 'Sol. AC', 'T (s)': 'T (s) AC', '%gap': '%gap AC', 'Lim. Iter.': 'Lim. Iter. AC' }, inplace = True)
df_gul_sem.rename(columns = {'Sol.': 'Sol. GS', 'T (s)': 'T (s) GS', '%gap': '%gap GS', 'Lim. Iter.': 'Lim. Iter. GS' }, inplace = True)
df_gul_com.rename(columns = {'Sol.': 'Sol. GC', 'T (s)': 'T (s) GC', '%gap': '%gap GC', 'Lim. Iter.': 'Lim. Iter. GC' }, inplace = True)

resultado = pd.concat([
  df_ale_sem.iloc[:,0:5], df_ale_sem.iloc[:,[7]], df_ale_sem.iloc[:,5:7],
  df_ale_com.iloc[:,[4]], df_ale_com.iloc[:,[7]], df_ale_com.iloc[:,5:7],  
  df_gul_sem.iloc[:,[4]], df_gul_sem.iloc[:,[7]], df_gul_sem.iloc[:,5:7], 
  df_gul_com.iloc[:,[4]], df_gul_com.iloc[:,[7]], df_gul_com.iloc[:,5:7]
], axis = 1)

resultado = pd.concat([
  resultado.iloc[0:27],
  resultado.iloc[28:51],
  resultado.iloc[[27]],
  resultado.iloc[52:151],
  resultado.iloc[[51]],
])

conjuntos = {
  'A': resultado[resultado['Instância'].str.contains("A")],
  'P':resultado[resultado['Instância'].str.contains("P")],
  'X':resultado[resultado['Instância'].str.contains("X")]
}

sumTotal = pd.DataFrame(
  
)

with open(CAMINHO_RESULTADO + 'resultado_total.csv', mode = 'w+') as arquivoTotal:

  sumTotalMelSol = 0
  sumTotalSolAS = 0
  sumTotalSolAC = 0
  sumTotalSolGS = 0
  sumTotalSolGC = 0
  sumTotalTempoAS = 0
  sumTotalTempoAC = 0
  sumTotalTempoGS = 0
  sumTotalTempoGC = 0

  arquivoTotal.write('Conjunto;Melhor Sol.;Sol. AS;T (s) AS;%gap AS;Sol. AC;T (s) AC;%gap AC;Sol. GS;T (s) GS;%gap GS;Sol. GC;T (s) GC;%gap GC\n')
  
  for i, conj in enumerate(conjuntos.values()):

    totalMelSol = conj['Melhor Sol.'].sum()
    sumTotalMelSol += totalMelSol

    totalSolAS = conj['Sol. AS'].sum()
    totalSolAC = conj['Sol. AC'].sum()
    totalSolGS = conj['Sol. GS'].sum()
    totalSolGC = conj['Sol. GC'].sum()
    sumTotalSolAS += totalSolAS
    sumTotalSolAC += totalSolAC
    sumTotalSolGS += totalSolGS
    sumTotalSolGC += totalSolGC

    totalTempoAS = 0
    totalTempoAC = 0
    totalTempoGS = 0
    totalTempoGC = 0
    for n in range(len(conj)):
      totalTempoAS += float(conj.iloc[n,6].replace(',', '.'))
      totalTempoAC += float(conj.iloc[n,10].replace(',', '.'))
      totalTempoGS += float(conj.iloc[n,14].replace(',', '.'))
      totalTempoGC += float(conj.iloc[n,18].replace(',', '.'))
    sumTotalTempoAS += totalTempoAS
    sumTotalTempoAC += totalTempoAC
    sumTotalTempoGS += totalTempoGS
    sumTotalTempoGC += totalTempoGC

    totalGapAS = gap(totalSolAS, totalMelSol)
    totalGapAC = gap(totalSolAC, totalMelSol)
    totalGapGS = gap(totalSolGS, totalMelSol)
    totalGapGC = gap(totalSolGC, totalMelSol)

    c = 'A' if i == 0 else 'P' if i == 1 else 'X' if i == 2 else ''

    with open(CAMINHO_RESULTADO + 'resultado_conj-'+ c + '.csv', mode = 'w+') as arquivo:
      conj.to_csv(arquivo, sep = ';', encoding='utf8', index = False)
      arquivo.write(f';Total;{totalMelSol:d};;'
                    + f'{totalSolAS:d};;{totalTempoAS:.2f};{totalGapAS:.2f};'.replace('.',',')
                    + f'{totalSolAC:d};;{totalTempoAC:.2f};{totalGapAC:.2f};'.replace('.',',')
                    + f'{totalSolGS:d};;{totalTempoGS:.2f};{totalGapGS:.2f};'.replace('.',',')
                    + f'{totalSolGC:d};;{totalTempoGC:.2f};{totalGapGC:.2f}\n'.replace('.',',')
                  )

    arquivoTotal.write(f'{c};{totalMelSol:d};'
                      + f'{totalSolAS:d};{totalTempoAS:.2f};{totalGapAS:.2f};'.replace('.',',')
                      + f'{totalSolAC:d};{totalTempoAC:.2f};{totalGapAC:.2f};'.replace('.',',')
                      + f'{totalSolGS:d};{totalTempoGS:.2f};{totalGapGS:.2f};'.replace('.',',')
                      + f'{totalSolGC:d};{totalTempoGC:.2f};{totalGapGC:.2f}\n'.replace('.',',')
                    )
  
  sumTotalGapAS = gap(sumTotalSolAS, sumTotalMelSol)
  sumTotalGapAC = gap(sumTotalSolAC, sumTotalMelSol)
  sumTotalGapGS = gap(sumTotalSolGS, sumTotalMelSol)
  sumTotalGapGC = gap(sumTotalSolGC, sumTotalMelSol)

  arquivoTotal.write(f'Total;{sumTotalMelSol:d};'
                      + f'{sumTotalSolAS:d};{sumTotalTempoAS:.2f};{sumTotalGapAS:.2f};'.replace('.',',')
                      + f'{sumTotalSolAC:d};{sumTotalTempoAC:.2f};{sumTotalGapAC:.2f};'.replace('.',',')
                      + f'{sumTotalSolGS:d};{sumTotalTempoGS:.2f};{sumTotalGapGS:.2f};'.replace('.',',')
                      + f'{sumTotalSolGC:d};{sumTotalTempoGC:.2f};{sumTotalGapGC:.2f}\n'.replace('.',',')
                    )

  