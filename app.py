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
except ImportError as e:
    st.error(f"Error crítico de importación: {e}")
    st.stop()

# 3. CSS MAESTRO
st.markdown("""
    <style>
    .stApp { background-color: white !important; color: #31333F !important; }
    [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }

    /* LOGO CLICKABLE: Hacemos que el botón que envuelve al logo sea invisible */
    .logo-clickable button {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        width: 130px !important;
        margin: 0 auto !important;
        display: block !important;
        cursor: pointer !important;
    }
    .logo-clickable img {
        max-width: 130px !important;
        transition: transform 0.2s;
    }
    .logo-clickable img:hover {
        transform: scale(1.05);
    }

    [data-testid="stSidebarContent"] [data-testid="stVerticalBlock"] > div {
        width: 100% !important;
    }
    
    /* BOTONES MATE (FLAMA) */
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
        justify-content: flex-start !important;
        width: 100% !important;
        margin-bottom: -4px !important;
    }
    
    div.stButton > button:hover {
        background: #555555 !important;
        border-color: #ffffff !important;
    }

    .btn-adhesion div.stButton > button {
        background: linear-gradient(145deg, #1a1a1a, #000000) !important;
        justify-content: center !important;
        margin-top: 15px !important;
    }

    .sidebar-footer { color: #666666 !important; font-size: 0.75rem; margin-top: 10px; line-height: 1.4; }
    .ws-container { display: flex; justify-content: center; margin-top: 20px; }
    .ws-icon-big { width: 50px !important; transition: transform 0.3s ease; }
    .ws-icon-big:hover { transform: scale(1.1); }
    </style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Landing"

with st.sidebar:
    # LOGO QUE VUELVE A LANDING (Sin íconos de casa)
    st.markdown('<div class="logo-clickable">', unsafe_allow_html=True)
    if st.button(" ", key="logo_home"): # Botón vacío (el CSS pone el logo encima)
        st.session_state.seccion_activa = "Landing"
    st.image(LOGO_URL)
    st.markdown('</div>', unsafe_allow_html=True)
    
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

    # WHATSAPP Y CONTACTO
    st.markdown(f"""
        <div class="ws-container">
            <a href="https://wa.me/541156096283" target="_blank">
                <img src="{WS_ICON_URL}" class="ws-icon-big" alt="WhatsApp">
            </a>
        </div>
        <div class="sidebar-footer">
            <div class="footer-item"><span>📍 Av. Rivadavia 4532 - Gal. Alefa (L. 10)</span></div>
            <div class="footer-item"><span>📍 Del Cimarrón 1846 - Ituzaingo</span></div>
            <div class="footer-item"><span>📞 11 - 4847-6467</span></div>
            <div class="footer-item"><span>✉️ info@serranoturismo.com.ar</span></div>
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
    
