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

# 3. CSS MAESTRO: ANCHO UNIFICADO Y HOVER GRIS MATE
st.markdown("""
    <style>
    /* 1. Reset de contenedores del Sidebar para forzar ancho total */
    [data-testid="stSidebarContent"] {
        padding: 1rem 0.5rem !important;
    }
    
    /* Forzar a cada bloque de botón a ocupar el 100% del contenedor */
    [data-testid="stVerticalBlock"] > div {
        width: 100% !important;
    }

    .stButton, .stButton button {
        width: 100% !important;
        display: block !important;
    }

    /* 2. Estilo de los Botones: Gris Oscuro Mate */
    div.stButton > button {
        background: linear-gradient(145deg, #444444, #2c2c2c) !important;
        color: white !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 8px !important;
        height: 50px !important; /* Alto uniforme */
        padding: 0px 20px !important;
        font-weight: 700 !important;
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        transition: all 0.3s ease !important;
        margin-bottom: 2px !important;
    }
    
    /* 3. HOVER: Cambio de Rojo a Gris/Blanco Minimalista */
    div.stButton > button:hover {
        background: #555555 !important; /* Gris un poco más claro */
        border-color: #ffffff !important; /* Recuadro Blanco/Plata */
        color: #ffffff !important;
        transform: translateX(4px) !important;
        box-shadow: 0 4px 12px rgba(255,255,255,0.1) !important;
    }

    /* 4. Botón de Adhesión (Diferenciado) */
    .btn-adhesion div.stButton > button {
        background: linear-gradient(145deg, #1a1a1a, #000000) !important;
        border: 1px solid #555555 !important;
        margin-top: 20px !important;
        justify-content: center !important;
        padding-left: 0 !important;
    }
    
    .btn-adhesion div.stButton > button:hover {
        border-color: #ffffff !important;
        background: #333333 !important;
    }

    /* Logo */
    [data-testid="stSidebar"] img {
        max-width: 130px !important;
        margin: 0 auto 10px auto !important;
        display: block !important;
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
    st.write("") 

    # Menú de botones
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

    # Botón de Adhesión
    st.markdown('<div class="btn-adhesion">', unsafe_allow_html=True)
    if st.button("📝 FICHA DE ADHESIÓN"):
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
