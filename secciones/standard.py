import streamlit as st
import os
import pandas as pd

def render_standard(destino, opcion):
    # Función de limpieza interna para nombres de archivos
    def limpiar_nombre(texto):
        reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", " ": "_"}
        texto = texto.lower()
        for original, reemplazo in reemplazos.items():
            texto = texto.replace(original, reemplazo)
        return texto + ".csv"

    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    file_name = limpiar_nombre(opcion)
    path = f"data/{folder}/{file_name}"

    st.markdown(f'<div class="header-container"><div class="header-text-overlay">{opcion.upper()}</div></div>', unsafe_allow_html=True)

    if os.path.exists(path):
        df = pd.read_csv(path)
        for _, row in df.iterrows():
            with st.expander(f"🔹 {row['Titulo']}", expanded=True):
                st.write(row['Contenido'])
                if 'Destacado' in row and pd.notna(row['Destacado']):
                    st.info(row['Destacado'])
    else:
        st.error(f"El archivo informativo '{file_name}' no se encuentra en la carpeta data/{folder}/")
