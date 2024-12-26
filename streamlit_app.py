import streamlit as st

st.title("Somma e Moltiplicazione")
num1 = st.number_input("Inserisci il primo numero:", value=0.0)
num2 = st.number_input("Inserisci il secondo numero:", value=0.0)

if st.button("Calcola"):
    somma = num1 + num2
    prodotto = num1 * num2
    st.write("Somma:", somma)
    st.write("Moltiplicazione:", prodotto)
