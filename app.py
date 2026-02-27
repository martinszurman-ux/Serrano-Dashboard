import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(
    page_title="Serrano Turismo - Dashboard", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# URL DEL LOGO
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

# 3. CSS MAESTRO (Fix botones simétricos y sintaxis)
st.markdown("""
<style>
    .stApp { background-color: white !important; color: #31333F !important; }
    [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }

    /* FORZAR QUE LOS CONTENEDORES OCUPEN TODO EL ANCHO */
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
        text-align: left !important;
        padding-left: 15px !important;
        display: block !important;
        white-space: nowrap !important;
    }

    .stButton > button:hover {
        background: #555555 !important;
        border-color: white !important;
        color: white !important;
    }

    /* BOTÓN ADHESIÓN: Negro total pero mismo tamaño */
    .btn-adhesion .stButton > button {
        background: linear-gradient(145deg, #1a1a1a, #000000) !important;
        text-align: center !important;
        padding-left: 0px !important;
        margin-top: 10px !important;
    }

    .logo-container { display: flex;
