import streamlit as st
from assets.ativos_b3 import ativos_b3
from assets.ativos_cripto import ativos_cripto
from assets.ativos_forex import ativos_forex

st.set_page_config(page_title="IA Day Trade", page_icon="📈", layout="centered")
st.title("📊 IA Assistente para Day Trade Manual")

tipo_ativo = st.selectbox("Tipo de ativo", ["B3", "Criptomoeda", "Forex"])

if tipo_ativo == "B3":
    ativos = ativos_b3
elif tipo_ativo == "Criptomoeda":
    ativos = ativos_cripto
else:
    ativos = ativos_forex

ticker = st.selectbox("Escolha o ativo", ativos)

st.write(f"Você selecionou: {ticker}")



