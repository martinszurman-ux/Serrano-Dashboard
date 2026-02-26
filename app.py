import streamlit as st

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# URL DEL LOGO
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# 2. IMPORTACIÓN DE MÓDULOS
try:
    from secciones.transporte import render_transporte
    from secciones.hoteleria import render_hoteleria
    from secciones.excursiones import render_excursiones
    from secciones.actividades_nocturnas import render_nocturnas
    from secciones.seguro import render_seguro
    from secciones.tarifas import render_tarifas
    from secciones.adhesion import render_adhesion
except ImportError as e:
    st.error(f"Error crítico de importación: {e}")
    st.stop()

# 3. CSS PARA BOTONES PLATEADOS, ICONOS Y ANCHO UNIFICADO
st.markdown("""
    <style>
    /* Achicar el logo y subir el menú */
    [data-testid="stSidebar"] img {
        max-width: 140px !important;
        margin: 0 auto !important;
        display: block !important;
    }
    
    /* Contenedor del sidebar más compacto */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.4rem !important;
        padding-top: 0.5rem !important;
    }

    /* Estilo para los botones: Plateado Minimalista con Ancho Fijo */
    div.stButton > button {
        background: linear-gradient(145deg, #e0e0e0, #f5f5f5) !important;
        color: #333333 !important;
        border: 1px solid #cccccc !important;
        border-radius: 8px !important;
        padding: 8px 15px !important;
        font-weight: 500 !important;
        
        /* Forzamos el ancho para que todos sean iguales */
        width: 100% !important; 
        min-width: 100% !important;
        
        text-align: left !important;
        transition: all 0.2s ease !important;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.05) !important;
        display: flex !important;
        align-items: center !important;
        white-space: nowrap !important;
    }
    
    div.stButton > button:hover {
        background: linear-gradient(145deg, #f5f5f5, #ffffff) !important;
        border-color: #999999 !important;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.1) !important;
    }

    /* Botón de ADHESIÓN (Gris Carbón Mate) */
    .btn-adhesion > div.stButton > button {
        background: linear-gradient(145deg, #444444, #222222) !important;
        color: #ffffff !important;
        border: 1px solid #111111 !important;
        margin-top: 15px !important;
        font-weight: 700 !important;
        text-align: center !important;
        justify-content: center !important;
    }
    
    .btn-adhesion > div.stButton > button:hover {
        background: linear-gradient(145deg, #222222, #000000) !important;
        color: #ffffff !important;
    }

    /* Iconos originales sin filtro de escala de grises */
    button p {
        margin-bottom: 0px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Transporte"

with st.sidebar:
    st.image(LOGO_URL)
    st.divider()
    
    destino = st.selectbox("📍 Destino", ["Villa Carlos Paz", "San Pedro"])
    
    # Volvemos a los iconos anteriores y aseguramos el ancho 100%
    if st.button("🚌 1. Transporte"):
        st.session_state.seccion_activa = "Transporte"
    
    if st.button("🏨 2. Hotelería"):
        st.session_state.seccion_activa = "Hotelería"
        
    if st.button("🏞️ 3. Excursiones"):
        st.session_state.seccion_activa = "Excursiones"
        
    if st.button("🌙 4. Actividades"):
        st.session_state.seccion_activa = "Actividades"
        
    if st.button("🏥 5. Seguro Médico"):
        st.session_state.seccion_activa = "Seguro"
        
    if st.button("💰 6. Tarifas"):
        st.session_state.seccion_activa = "Tarifas"

    # Botón de Adhesión (CTA Final)
    st.markdown('<div class="btn-adhesion">', unsafe_allow_html=True)
    if st.button("FICHA DE ADHESIÓN"):
        st.session_state.seccion_activa = "Adhesión"
    st.markdown('</div>', unsafe_allow_html=True)

# 5. RENDERIZADO
if st.session_state.seccion_activa == "Transporte":
    render_transporte(destino)
elif st.session_state.seccion_activa == "Hotelería":
    render_hoteleria(destino)
elif st.session_state.seccion_activa == "Excursiones":
    render_excursiones(destino)
elif st.session_state.seccion_activa == "Actividades":
    render_nocturnas(destino)
elif st.session_state.seccion_activa == "Seguro":
    render_seguro(destino)
elif st.session_state.seccion_activa == "Tarifas":
    render_tarifas(destino)
elif st.session_state.seccion_activa == "Adhesión":
    render_adhesion(LOGO_URL)
