import streamlit as st

st.set_page_config(page_title="Teste IA Day Trade", page_icon="📈", layout="centered")

st.title("✅ Teste de Interface")
st.write("Se você está vendo esta mensagem, o Streamlit está funcionando corretamente!")

opcao = st.selectbox("Escolha uma categoria:", ["B3", "Criptomoeda", "Forex"])
st.write(f"Você escolheu: {opcao}")


