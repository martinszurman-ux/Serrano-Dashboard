import streamlit as st

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(
    page_title="Serrano Turismo - Dashboard", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# URL DE LOGOS
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"
WS_ICON = "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"

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

# 3. CSS MAESTRO (WhatsApp Grande y Menú Blindado)
st.markdown("""
    <style>
    /* 1. LIMPIEZA Y FORZADO MODO LIGHT */
    .stAppToolbar { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    :root { --primary-color: #444444; --background-color: #ffffff; }

    /* 2. BOTONES MATE (FLAMA) */
    [data-testid="stSidebarContent"] [data-testid="stVerticalBlock"] > div {
        width: 100% !important;
    }
    div.stButton > button {
        background: linear-gradient(145deg, #444444, #2c2c2c) !important;
        color: white !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 8px !important;
        height: 52px !important;
        font-weight: 700 !important;
        font-size: 17px !important;
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
        transition: all 0.2s ease !important;
        margin-bottom: -4px !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        background: #555555 !important;
        border-color: #ffffff !important;
        transform: translateX(4px) !important;
    }

    /* 3. LOGO Y PIE DE PÁGINA */
    .logo-container { display: flex; justify-content: center; margin: -10px 0; }
    .logo-container img { max-width: 130px !important; }

    .sidebar-footer { 
        color: #666666; 
        font-size: 0.75rem; 
        margin-top: 15px; 
        line-height: 1.3; 
    }
    .footer-item { margin-bottom: 5px; }

    /* 4. BOTÓN WHATSAPP GRANDE ABAJO */
    .ws-float-container {
        display: flex;
        justify-content: center;
        margin-top: 25px;
        padding-bottom: 20px;
    }
    .ws-big-icon {
        width: 55px !important; /* TAMAÑO GRANDE */
        transition: transform 0.3s ease, filter 0.3s ease;
        filter: drop-shadow(0px 4px 6px rgba(0,0,0,0.2));
    }
    .ws-big-icon:hover {
        transform: scale(1.15) rotate(5deg);
        filter: drop-shadow(0px 6px 12px rgba(37, 211, 102, 0.4));
    }
    </style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Transporte"

with st.sidebar:
    st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}"></div>', unsafe_allow_html=True)
    st.divider()
    
    destino = st.selectbox("📍 Destino", ["Villa Carlos Paz", "San Pedro"])
    
    # Menú de botones
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

    # DATOS DE CONTACTO (Sin el teléfono de WS)
    st.markdown(f"""
        <div class="sidebar-footer">
            <div class="footer-item">📍 Av. Rivadavia 4532 - Gal. Alefa (L. 10)</div>
            <div class="footer-item">📍 Del Cimarrón 1846 - Ituzaingo</div>
            <div class="footer-item">📞 11 - 4847-6467</div>
            <div class="footer-item">✉️ info@serranoturismo.com.ar</div>
        </div>
        
        <div class="ws-float-container">
            <a href="https://wa.me/541156096283" target="_blank">
                <img src="{WS_ICON}" class="ws-big-icon" alt="WhatsApp">
            </a>
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
