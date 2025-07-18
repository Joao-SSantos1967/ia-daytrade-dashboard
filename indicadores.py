import pandas as pd

def calcular_indicadores(df):
    # Médias móveis simples
    df["MM9"] = df["Close"].rolling(window=9).mean()
    df["MM21"] = df["Close"].rolling(window=21).mean()

    # Sinal operacional
    df["Sinal"] = "lateral"
    df.loc[df["MM9"] > df["MM21"], "Sinal"] = "compra"
    df.loc[df["MM9"] < df["MM21"], "Sinal"] = "venda"

    return df


