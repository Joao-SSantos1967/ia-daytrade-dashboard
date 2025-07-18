import streamlit as st
import pandas as pd
from assets.ativos_b3 import ativos_b3
from assets.ativos_cripto import ativos_cripto
from assets.ativos_forex import ativos_forex
import yfinance as yf
import pandas as pd
from assets.b3 import carregar_ativo as carregar_b3
from assets.cripto import carregar_ativo as carregar_cripto
from assets.forex import carregar_ativo as carregar_forex
from assets.indicadores import calcular_indicadores

st.set_page_config(page_title="IA Day Trade", page_icon="📈", layout="centered")
st.title("📈 IA Assistente para Day Trade Manual")

tipo_ativo = st.selectbox("Tipo de ativo", ["B3", "Criptomoeda", "Forex"])

if tipo_ativo == "B3":
    ativos = ativos_b3
    carregar = carregar_b3
elif tipo_ativo == "Criptomoeda":
    ativos = ativos_cripto
    carregar = carregar_cripto
else:
    ativos = ativos_forex
    carregar = carregar_forex

ticker = st.selectbox("Escolha o ativo", ativos)

st.write(f"Você selecionou: {ticker}")
from assets.indicadores import calcular_indicadores

# Carregar dados do ativo
df = carregar(ticker)

if df is not None and not df.empty:
    # Calcular indicadores técnicos
    df = calcular_indicadores(df)

    # Exibir gráfico de velas
    import plotly.graph_objects as go

    st.subheader("🕯️ Gráfico de Velas")

    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    )])

    fig.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)

    # Exibir sinal operacional
    sinal = df["Sinal"].iloc[-1]
    proximo_candle = df.index[-1] + pd.Timedelta(minutes=5)

    if sinal == "compra":
        st.success(f"🟢 Sinal de COMPRA às {proximo_candle.time()}")
    elif sinal == "venda":
        st.error(f"🔴 Sinal de VENDA às {proximo_candle.time()}")
    else:
        st.info(f"⚪ Tendência LATERAL às {proximo_candle.time()}")
else:
    st.warning("Não foi possível carregar os dados do ativo.")









