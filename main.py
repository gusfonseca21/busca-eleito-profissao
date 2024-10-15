import os
import pandas as pd

# Filtragem específica para vereadores eleitos em capitais que são policiais

CAMINHO_DADOS_CANDIDATOS = "../../dados/consulta_cand_2024/consulta_cand_2024_BRASIL.csv"

PROFISSAO = 'POLICIAL'

CAPITAIS = ["RIO BRANCO", "MACEIÓ", "MACAPÁ", "MANAUS", "SALVADOR", "FORTALEZA", "VITÓRIA", "GOIÂNIA", "SÃO LUÍS", "CUIABÁ", "CAMPO GRANDE", "BELO HORIZONTE", "BELÉM", "JOÃO PESSOA", "CURITIBA", "RECIFE", "TERESINA", "RIO DE JANEIRO", "NATAL", "PORTO ALEGRE", "PORTO VELHO", "BOA VISTA", "FLORIANÓPOLIS", "SÃO PAULO", "ARACAJU", "PALMAS"]

ESTADOS = ["AC", "AL", "AP", "AM", "BA", "CE", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

resultados_totais = []

df = pd.read_csv(CAMINHO_DADOS_CANDIDATOS, encoding='latin1', delimiter=';', quotechar='"')

resultados = df[df['DS_OCUPACAO'].str.contains(PROFISSAO, na=False) & df['CD_SIT_TOT_TURNO'].isin([2, 3]) & df['NM_UE'].isin(CAPITAIS) & df['SG_UF'].isin(ESTADOS)]

resultados.to_csv('policiais_eleitos_vereadores_capitais_2024_2.csv')