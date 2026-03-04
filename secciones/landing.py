import streamlit as st

def render_landing():
    # Forzamos un estilo gris total para el fondo y texto blanco al medio
    st.markdown("""
        <style>
        /* Quitamos el padding por defecto de Streamlit */
        .main {
            background-color: #2e2e2e !important;
        }
        .stApp {
            background-color: #2e2e2e !important;
        }
        /* Centrado absoluto del Hola */
        .centered-hola {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            color: white;
            font-size: 100px;
            font-weight: bold;
            font-family: sans-serif;
        }
        </style>
        <div class="centered-hola">
            HOLA
        </div>
    """, unsafe_allow_html=True)
