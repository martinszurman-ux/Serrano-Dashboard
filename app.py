import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Serrano Turismo", layout="wide")

# Logo
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    opcion = st.radio("📂 Información del Viaje", [
        "Transporte", "Hotelería", "Régimen de Comidas", 
        "Excursiones de Día", "Actividades Nocturnas", 
        "Seguro Médico", "Coordinación", 
        "Tarifas y Formas de Pago", "Regalos y Promociones"
    ])

# --- CORRECCIÓN DE TILDES Y FORMATO ---
# Esta función limpia el nombre de la opción para que coincida con el archivo real
def limpiar_nombre_archivo(texto):
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        " ": "_"
    }
    texto = texto.lower()
    for original, reemplazo in reemplazos.items():
        texto = texto.replace(original, reemplazo)
    return texto + ".csv"

file_name = limpiar_nombre_archivo(opcion)
path = f"data/{folder}/{file_name}"

st.title(f"{opcion}")

if os.path.exists(path):
    df = pd.read_csv(path)
    for index, row in df.iterrows():
        with st.expander(f"🔹 {row['Titulo']}", expanded=True):
            st.write(row['Contenido'])
            if 'Destacado' in row:
                st.info(row['Destacado'])
else:
    st.error(f"No se encontró el archivo: `{file_name}`")
    st.info(f"Asegurate de que en GitHub el archivo se llame exactamente: **{file_name}**")
