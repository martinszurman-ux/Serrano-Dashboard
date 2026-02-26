import streamlit as st
import pandas as pd
import os

# Configuración de página y Estilo Serrano
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

st.markdown("""
    <style>
    .stRadio > label { font-weight: bold; color: #1E3A8A; }
    .stSelectbox > label { font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Logo
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# --- SIDEBAR ---
with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    st.subheader("📂 Menú del Viaje")
    opcion = st.radio("Información disponible:", [
        "Transporte", "Hotelería", "Régimen de Comidas", 
        "Excursiones de Día", "Actividades Nocturnas", 
        "Seguro Médico", "Coordinación", "Regalos y Promociones",
        "Tarifas y Formas de Pago"
    ])
    
    st.divider()
    st.caption("Serrano Turismo - 29 años de trayectoria")

# --- CONTENIDO PRINCIPAL ---
# Convertimos la opción del radio al nombre del archivo csv
file_name = opcion.lower().replace(" ", "_").replace("í", "i").replace("ó", "o") + ".csv"
path = f"data/{folder}/{file_name}"

st.title(f"{opcion}")
st.subheader(f"Destino: {destino}")

if os.path.exists(path):
    df = pd.read_csv(path)
    
    # Mostramos cada fila del CSV como una tarjeta informativa
    for index, row in df.iterrows():
        with st.expander(f"🔹 {row['Titulo']}", expanded=True):
            st.write(row['Contenido'])
            if pd.notna(row['Destocado']) if 'Destocado' in row else False: # Manejo de errores de tipeo
                st.info(row['Destocado'])
            elif 'Destacado' in row:
                st.info(row['Destacado'])
else:
    st.warning(f"🚧 El archivo `{file_name}` aún no ha sido creado en la carpeta `data/{folder}/` de GitHub.")
    st.info("Subí el archivo a tu repositorio para que la información aparezca aquí automáticamente.")
