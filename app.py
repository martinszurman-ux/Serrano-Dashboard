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

# 3. CSS MAESTRO - FIX DE BOTONES Y SINTAXIS
st.markdown("""
<style>
    .stApp { background-color: white !important; color: #31333F !important; }
    [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }

    /* Forzar que todos los botones del sidebar sean iguales */
    div[data-testid="stSidebarContent"] .stButton button {
        width: 100% !important;
        background: linear-gradient(145deg, #444444, #2c2c2c) !important;
        color: white !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 8px !important;
        height: 52px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        text-align: left !important;
        padding-left: 10px !important;
        display: block !important;
        white-space: nowrap !important;
        margin-bottom: 2px !important;
    }

    /* Hover de botones */
    div[data-testid="stSidebarContent"] .stButton button:hover {
        background: #555555 !important;
        border-color: white !important;
        color: white !important;
    }

    /* Botón de Adhesión (Diferenciado pero igual tamaño) */
    .btn-adhesion .stButton button {
        background: linear-gradient(145deg, #1a1a1a, #000000) !important;
        text-align: center !important;
        padding-left: 0px !important;
        margin-top: 15px !important;
    }

    .logo-container { display: flex; justify-content: center; margin-bottom: 10px; }
    .logo-container img { max-width: 120px !important; }
    .sidebar-footer { color: #666666 !important; font-size: 0.75rem; margin-top: 20px; line-height: 1.2; }
</style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Transporte"

with st.sidebar:
    st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}"></div>', unsafe_allow_html=True)
    st.divider()
    
    destino = st.selectbox("📍 Seleccione Destino", ["Villa Carlos Paz", "San Pedro"])
    
    if st.button("🚌 1. Transporte"): st.session_state.seccion_activa = "Transporte"
    if st.button("🏨 2. Hotelería"): st.session_state.seccion_activa = "Hotelería"
    if st.button("🍽️ 3. Comidas"): st.session_state.seccion_activa = "Comidas"
    if st.button("🏞️ 4. Excursiones"): st.session_state.seccion_activa = "Excursiones"
    if st.button("🌙 5. Actividades Nocturnas"): st.session_state.seccion_activa = "Actividades"
    if st.button("🏥 6. Coordinación/Seguro Médico"): st.session_state.seccion_activa = "Seguro"
    if st.button("💰 7. Tarifas"): st.session_state.seccion_activa = "Tarifas"

    st.markdown('<div class="btn-adhesion">', unsafe_allow_html=True)
    if st.button("📝 FICHA DE ADHESIÓN"): st.session_state.seccion_activa = "Adhesion"
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="sidebar-footer">
            <div>📍 Av. Rivadavia 4532 - Gal. Alefa (L. 10)</div>
            <div>📍 Del Cimarrón 1846 - Ituzaingo</div>
            <div>📞 11 - 4847-6467</div>
            <div>✉️ info@serranoturismo.com.ar</div>
        </div>
    """, unsafe_allow_html=True)

# 5. RENDERIZADO
if st.session_state.seccion_activa == "Transporte":
    render_transporte(destino)
elif st.session_state.seccion_activa == "Hotelería":
    render_hoteleria(destino)
elif st.session_state.seccion_activa == "Comidas":
    render_comidas(destino)
elif st.session_state.seccion_activa == "Excursiones":
    render_excursiones(destino)
elif st.session_state.seccion_activa == "Actividades":
    render_nocturnas(destino)
elif st.session_state.seccion_activa == "Seguro":
    render_seguro(destino)
elif st.session_state.seccion_activa == "Tarifas":
    render_tarifas(destino)
elif st.session_state.seccion_activa == "Adhesion":
    render_adhesion(LOGO_URL)
