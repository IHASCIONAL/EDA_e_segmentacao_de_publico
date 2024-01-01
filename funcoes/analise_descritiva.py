import pandas as pd
import numpy as np

def stats_resume(numerical_df):
    """
    Realiza uma análise descritiva básica em um DataFrame contendo dados numéricos.

    Parâmetros:
        numerical_df (pandas.DataFrame): DataFrame contendo apenas dados numéricos.
        
    Retorna:
        pandas.DataFrame: Um DataFrame com as seguintes estatísticas descritivas para cada coluna:
            - Atributos: Nomes das colunas do DataFrame de entrada.
            - Media: Média dos valores em cada coluna.
            - Mediana: Mediana dos valores em cada coluna.
            - DesvioPadrao: Desvio padrão dos valores em cada coluna.
            - Min: Valor mínimo em cada coluna.
            - Q1: Primeiro quartil em cada coluna.
            - P10: Décimo percentil em cada coluna.
            - P90: Nonagésimo percentil em cada coluna.
            - Q3: Terceiro quartil em cada coluna.
            - Max: Valor máximo em cada coluna.
            - Range: Amplitude dos valores em cada coluna (diferença entre máximo e mínimo).
            - Assimetria: Medida de assimetria dos valores em cada coluna.
            - Curtose: Medida de curtose dos valores em cada coluna.
    """
    
    ct1 = pd.DataFrame(numerical_df.apply(np.mean)).T
    ct2 = pd.DataFrame(numerical_df.apply(np.median)).T
    ct3 = pd.DataFrame(numerical_df.apply(lambda x: x.quantile(0.25))).T  # Q1
    ct4 = pd.DataFrame(numerical_df.apply(lambda x: x.quantile(0.75))).T  # Q3
    ct5 = pd.DataFrame(numerical_df.apply(lambda x: x.quantile(0.10))).T  # P10
    ct6 = pd.DataFrame(numerical_df.apply(lambda x: x.quantile(0.90))).T  # P90

    d1 = pd.DataFrame(numerical_df.apply(np.std)).T
    d2 = pd.DataFrame(numerical_df.apply(min)).T
    d3 = pd.DataFrame(numerical_df.apply(max)).T
    d4 = pd.DataFrame(numerical_df.apply(lambda x: x.max() - x.min())).T
    d5 = pd.DataFrame(numerical_df.apply(lambda x: x.skew())).T
    d6 = pd.DataFrame(numerical_df.apply(lambda x: x.kurtosis())).T

    m = pd.concat([ct1, ct2, ct3, ct4, ct5, ct6, d1, d2, d3, d4, d5, d6]).T.reset_index()
    m.columns = ["Atributos", "Media", "Mediana", "Q1", "Q3", "P10", "P90", "DesvioPadrao", "Min", "Max", "Range", "Assimetria", "Curtose"]

    return m