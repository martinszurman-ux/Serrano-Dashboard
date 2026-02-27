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

# 3. CSS MAESTRO (Compactación y Reordenamiento)
st.markdown("""
    <style>
    /* FORZAR COLORES LIGHT */
    .stApp { background-color: white !important; color: #31333F !important; }
    [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }

    /* COMPACTAR SIDEBAR: Menos espacio arriba y entre elementos */
    [data-testid="stSidebarContent"] {
        padding-top: 0.2rem !important; 
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
    [data-testid="stSidebar"] hr { margin: 0.5rem 0 !important; }

    /* BOTONES MATE (FLAMA) - Un toque más chicos */
    div.stButton > button {
        background: linear-gradient(145deg, #444444, #2c2c2c) !important;
        color: white !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 8px !important;
        height: 45px !important; /* ACHICADO de 52px a 45px */
        font-weight: 700 !important;
        font-size: 15px !important; /* Letra sutilmente más chica */
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
        width: 100% !important;
        margin-bottom: -8px !important; /* Más pegados entre sí */
        transition: all 0.2s ease !important;
    }
    div.stButton > button:hover {
        background: #555555 !important;
        border-color: #ffffff !important;
        transform: translateX(4px) !important;
    }

    /* BOTÓN ADHESIÓN */
    .btn-adhesion div.stButton > button {
        background: linear-gradient(145deg, #1a1a1a, #000000) !important;
        margin-top: 5px !important;
        justify-content: center !important;
        height: 48px !important;
    }

    /* LOGO SUBIDO AL MÁXIMO */
    .logo-container {
        display: flex; justify-content: center; width: 100%;
        margin-top: -20px !important;
        margin-bottom: -15px !important;
    }
    .logo-container img { max-width: 120px !important; }

    /* WHATSAPP ARRIBA DE LAS DIRECCIONES */
    .ws-top-container {
        display: flex;
        justify-content: center;
        margin: 10px 0;
    }
    .ws-icon-small {
        width: 45px !important;
        transition: transform 0.3s ease;
    }
    .ws-icon-small:hover { transform: scale(1.1); }

    /* CONTACTO FINAL MUY COMPACTO */
    .sidebar-footer { 
        color: #666666 !important; 
        font-size: 0.7rem; 
        line-height: 1.2; 
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Transporte"

with st.sidebar:
    # Logo
    st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}"></div>', unsafe_allow_html=True)
    st.divider()
    
    destino = st.selectbox("📍 Destino", ["Villa Carlos Paz", "San Pedro"])
    
    # Botones
    if st.button("🚌 1. Transporte"): st.session_state.seccion_activa = "Transporte"
    if st.button("🏨 2. Hotelería"): st.session_state.seccion_activa = "Hotelería"
    if st.button("🍽️ 3. Comidas"): st.session_state.seccion_activa = "Comidas"
    if st.button("🏞️ 4. Excursiones"): st.session_state.seccion_activa = "Excursiones"
    if st.button("🌙 5. Actividades Nocturnas"): st.session_state.seccion_activa = "Actividades"
    if st.button("🏥 6. Seguro Médico"): st.session_state.seccion_activa = "Seguro"
    if st.button("💰 7. Tarifas"): st.session_state.seccion_activa = "Tarifas"

    st.markdown('<div class="btn-adhesion">', unsafe_allow_html=True)
    if st.button("📝 FICHA DE ADHESIÓN"): st.session_state.seccion_activa = "Adhesión"
    st.markdown('</div>', unsafe_allow_html=True)

    # WHATSAPP ARRIBA DEL TEXTO
    st.markdown(f"""
        <div class="ws-top-container">
            <a href="https://wa.me/541156096283" target="_blank">
                <img src="{WS_ICON_URL}" class="ws-icon-small" alt="WhatsApp">
            </a>
        </div>
        <div class="sidebar-footer">
            📍 Rivadavia 4532 (L. 10) - CABA<br>
            📍 Del Cimarrón 1846 - Ituzaingo<br>
            📞 11 - 4847-6467<br>
            ✉️ info@serranoturismo.com.ar
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
elif st.session_state.seccion_activa == "Adhesión":
    render_adhesion(LOGO_URL)
