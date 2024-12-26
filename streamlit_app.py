import streamlit as st
import tkinter as tk
from tkinter import ttk

def calcola_somma_e_moltiplicazione():
    """
    Legge i valori dalle Entry, calcola somma e moltiplicazione,
    e li mostra nelle Label corrispondenti.
    """
    try:
        # Prende i valori di input
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        # Calcola i risultati
        somma = num1 + num2
        prodotto = num1 * num2
        
        # Aggiorna le label
        label_somma_result.config(text=f"{somma}")
        label_molt_result.config(text=f"{prodotto}")
    except ValueError:
        # Se il valore non è convertibile in float, mostra un messaggio di errore
        label_somma_result.config(text="Errore input")
        label_molt_result.config(text="Errore input")

# Creazione finestra principale
root = tk.Tk()
root.title("Calcolo Somma e Moltiplicazione")

# Frame per contenere gli elementi
frame = ttk.Frame(root, padding="20 20 20 20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label e Entry per il primo numero
label_num1 = ttk.Label(frame, text="Numero 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_num1 = ttk.Entry(frame, width=10)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# Label e Entry per il secondo numero
label_num2 = ttk.Label(frame, text="Numero 2:")
label_num2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
entry_num2 = ttk.Entry(frame, width=10)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Pulsante di calcolo
btn_calcola = ttk.Button(frame, text="Calcola", command=calcola_somma_e_moltiplicazione)
btn_calcola.grid(row=2, column=0, columnspan=2, pady=10)

# Label di output per somma e moltiplicazione
label_somma = ttk.Label(frame, text="Somma:")
label_somma.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
label_somma_result = ttk.Label(frame, text="–")
label_somma_result.grid(row=3, column=1, padx=5, pady=5)

label_molt = ttk.Label(frame, text="Moltiplicazione:")
label_molt.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
label_molt_result = ttk.Label(frame, text="–")
label_m
