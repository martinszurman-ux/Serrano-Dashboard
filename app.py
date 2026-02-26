import streamlit as st
# Importamos la función desde la carpeta secciones
from secciones.tarifas import render_tarifas

# Configuración básica
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# Estilos globales que aplican a todas las secciones
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    /* Estilo compartido para los widgets 3D */
    .widget-3d-inner {
        background: linear-gradient(145deg, #f0f0f0, #ffffff);
        border-radius: 15px; padding: 20px; text-align: center;
        border: 1px solid #ddd;
        box-shadow: inset 3px 3px 6px #d1d1d1, inset -3px -3px 6px #ffffff;
        min-height: 180px; display: flex; flex-direction: column; 
        justify-content: center; align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.image("https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png", use_container_width=True)
    st.divider()
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    opcion = st.radio("📂 Navegación", ["Tarifas", "Solicitud de Adhesión", "Seguro Médico"])

# Lógica de navegación
if opcion == "Tarifas":
    render_tarifas(destino)
elif opcion == "Solicitud de Adhesión":
    st.info("Sección en desarrollo por tu compañero...")
elif opcion == "Seguro Médico":
    st.info("Sección de Seguro Médico...")
