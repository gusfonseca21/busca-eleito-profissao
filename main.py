import os
import pandas as pd

CAMINHO_DADOS_CANDIDATOS = "./dados/"

resultados_totais = []

for arquivo in os.listdir(CAMINHO_DADOS_CANDIDATOS):
 if arquivo.endswith('.csv'):
  
  df = pd.read_csv(os.path.join(CAMINHO_DADOS_CANDIDATOS, arquivo), encoding='latin1', delimiter=';', quotechar='"')
  
  resultados = df[df['DS_OCUPACAO'].str.contains('POLICIAL', na=False) & df['CD_SIT_TOT_TURNO'].isin([1, 2, 3])]

  resultados_totais.append(resultados)

df_final = pd.concat(resultados_totais, ignore_index=True)

df_final.to_csv('resultados.csv', index=False)