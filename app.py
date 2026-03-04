import streamlit as st

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(
    page_title="Serrano Turismo - Dashboard", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# URL DEL LOGO Y WHATSAPP
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"
WS_ICON_URL = "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"

# 2. IMPORTACIÓN DE MÓDULOS
try:
    from secciones.landing import render_landing
    from secciones.transporte import render_transporte
    from secciones.hoteleria import render_hoteleria
    from secciones.comidas import render_comidas
    from secciones.excursiones import render_excursiones
    from secciones.actividades_nocturnas import render_nocturnas
    from secciones.seguro import render_seguro
    from secciones.tarifas import render_tarifas
    from secciones.adhesion import render_adhesion
    from secciones.admin import render_admin
except ImportError as e:
    st.error(f"Error crítico de importación: {e}")
    st.stop()

# 3. CSS MAESTRO (Look & Feel Slim Optimizado para Mobile)
st.markdown("""
    <style>
    /* FORZAR COLORES LIGHT */
    .stApp { background-color: white !important; color: #31333F !important; }
    [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }

    /* LOGO SUBIDO AL MÁXIMO */
    .logo-container {
        display: flex; justify-content: center; width: 100%;
        margin-top: -35px !important;
        margin-bottom: -15px !important;
    }
    .logo-container img { max-width: 110px !important; }

    /* BOTONES SLIM OPTIMIZADOS PARA DEDO Y PANTALLA CHICA */
    [data-testid="stSidebarContent"] [data-testid="stVerticalBlock"] > div {
        width: 100% !important;
        padding-left: 8px !important;
        padding-right: 8px !important;
    }
    
    div.stButton > button {
        background: linear-gradient(145deg, #444444, #2c2c2c) !important;
        color: white !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 6px !important;
        height: 40px !important; /* Altura optimizada */
        font-weight: 600 !important;
        font-size: 13px !important; /* Fuente para evitar saltos de línea */
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        margin-bottom: -10px !important;
        white-space: nowrap !important; /* Fuerza una sola línea */
        overflow: hidden !important;
        transition: all 0.3s ease !important;
    }
    
    div.stButton > button:hover {
        background: #555555 !important;
        border-color: #ffffff !important;
        transform: translateX(3px) !important;
    }

    /* BOTÓN ADHESIÓN Y ADMIN (Estilo especial) */
    .btn-adhesion div.stButton > button, .btn-admin div.stButton > button {
        background: linear-gradient(145deg, #1a1a1a, #000000) !important;
        justify-content: center !important;
        margin-top: 5px !important;
        height: 44px !important;
        border: 1px solid #4A90E2 !important;
    }

    /* WHATSAPP ANIMADO */
    .ws-container {
        display: flex;
        justify-content: center;
        margin-top: 15px;
        margin-bottom: 20px;
    }
    .ws-icon-animated {
        width: 55px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .ws-icon-animated:hover {
        transform: scale(1.15) rotate(8deg);
    }

    /* CONTACTO COMPACTO */
    .sidebar-footer { 
        color: #666666 !important; 
        font-size: 0.65rem; 
        line-height: 1.3; 
        text-align: center;
        padding-top: 10px;
        border-top: 1px solid #e0e0e0;
        margin: 0 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Landing"

with st.sidebar:
    # Logo
    st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}"></div>', unsafe_allow_html=True)
    st.divider()
    
    destino = st.selectbox("📍 Destino", ["Villa Carlos Paz", "San Pedro"])
    
    # Menú de navegación
    if st.button("🚌 1. Transporte"): st.session_state.seccion_activa = "Transporte"
    if st.button("🏨 2. Hotelería"): st.session_state.seccion_activa = "Hotelería"
    if st.button("🍽️ 3. Comidas"): st.session_state.seccion_activa = "Comidas"
    if st.button("🏞️ 4. Excursiones"): st.session_state.seccion_activa = "Excursiones"
    if st.button("🌙 5. Actividades"): st.session_state.seccion_activa = "Actividades"
    # BOTÓN ACTUALIZADO
    if st.button("🏥 6. Coordinación/Seguro"): st.session_state.seccion_activa = "Seguro"
    if st.button("💰 7. Tarifas"): st.session_state.seccion_activa = "Tarifas"

    # Botón Ficha de Adhesión
    st.markdown('<div class="btn-adhesion">', unsafe_allow_html=True)
    if st.button("📝 FICHA DE ADHESIÓN"): st.session_state.seccion_activa = "Adhesión"
    st.markdown('</div>', unsafe_allow_html=True)

    # Lógica de Botón Admin Oculto
    if st.query_params.get("admin") == "true":
        st.markdown('<div class="btn-admin">', unsafe_allow_html=True)
        if st.button("⚙️ Configuración"): 
            st.session_state.seccion_activa = "Admin"
        st.markdown('</div>', unsafe_allow_html=True)

    # WhatsApp y Contacto
    st.markdown(f"""
        <div class="ws-container">
            <a href="https://wa.me/541156096283" target="_blank">
                <img src="{WS_ICON_URL}" class="ws-icon-animated" alt="WhatsApp">
            </a>
        </div>
        <div class="sidebar-footer">
            📍 Rivadavia 4532 (L. 10) - CABA<br>
            📍 Del Cimarrón 1846 - Ituzaingo<br>
            📞 11 - 4847-6467 | ✉️ info@serranoturismo.com.ar
        </div>
    """, unsafe_allow_html=True)

# 5. RENDERIZADO
if st.session_state.seccion_activa == "Landing":
    render_landing()
elif st.session_state.seccion_activa == "Transporte":
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
elif st.session_state.seccion_activa == "Adhesión":
    render_adhesion(LOGO_URL)
elif st.session_state.seccion_activa == "Admin":
    render_admin()
