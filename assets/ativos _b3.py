import yfinance as yf
import pandas as pd

def carregar_ativo(ticker):
    try:
        df = yf.download(ticker, interval="5m", period="1d")
        df = df.dropna()
        return df
    except Exception as e:
        print(f"Erro ao carregar ativo {ticker}: {e}")
        return pd.DataF

