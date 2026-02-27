import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(
    page_title="Serrano Turismo - Dashboard", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# 2. IMPORTACIÓN DE MÓDULOS
try:
    from secciones.transporte import render_transporte
    from secciones.hoteleria import render_hoteleria
    from secciones.comidas import render_comidas
    from secciones.excursiones import render_excursiones
    from secciones.actividades_nocturnas import render_nocturnas
    from secciones.seguro import render_seguro
    from secciones.tarifas import render_tarifas
    from secciones.adhesion import render_adhesion
except ImportError as e:
    st.error(f"Error crítico de importación: {e}")
    st.stop()

# 3. CSS MAESTRO - FIX TOTAL DE SINTAXIS Y BOTONES
st.markdown("""
    <style>
    .stApp { background-color: white !important; color: #31333F !important; }
    [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }

    /* Forzar que el contenedor del botón ocupe todo el ancho */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] > div {
        width: 100% !important;
    }

    /* ESTILO DE BOTONES: Bloques idénticos */
    .stButton > button {
        width: 100% !important;
        background: linear-gradient(145deg, #444444, #2c2c2c) !important;
        color: white !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 8px !important;
        height: 52px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        text-align
