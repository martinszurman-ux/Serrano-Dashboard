import streamlit as st
import os

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# URL DEL LOGO PRINCIPAL Y RUTA DEL LOGO WHATSAPP
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"
WS_LOGO_PATH = "assets/whatsapp_logo.jpg"

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

# 3. CSS MAESTRO: LETRAS MÁS GRANDES Y ANCHOS BLINDADOS
st.markdown("""
    <style>
    /* Reset de anchos y espacios */
    [data-testid="stSidebarContent"] [data-testid="stVerticalBlock"] > div {
        width: 100% !important;
        max-width: 100% !important;
    }
    
    .stButton, .stButton > button {
        width: 100% !important;
        min-width: 100% !important;
        display: block !important;
    }

    /* DISEÑO DE BOTONES: GRIS OSCURO MATE CON LETRA MÁS GRANDE */
    div.stButton > button {
        background: linear-gradient(145deg, #444444, #2c2c2c) !important;
        color: white !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 8px !important;
        height: 52px !important; /* Un poco más alto para acompañar la letra */
        padding: 0px 20px !important;
        font-weight: 700 !important;
        font-size: 17px !important; /* LETRA MÁS GRANDE */
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        transition: all 0.2s ease-in-out !important;
        margin-bottom: -4px !important;
    }
    
    div.stButton > button:hover {
        background: #555555 !important;
        border-color: #ffffff !important;
        transform: translateX(4px) !important;
    }

    /* BOTÓN DE ADHESIÓN */
    .btn-adhesion div.stButton > button {
        background: linear-gradient(145deg, #1a1a1a, #000000) !important;
        border: 1px solid #555555 !important;
        margin-top: 15px !important;
        justify-content: center !important;
        font-size: 18px !important;
    }

    /* LOGO Y CONTACTO */
    .logo-container {
        display: flex; justify-content: center; width: 100%;
        margin-bottom: -10px !important; margin-top: -10px !important;
    }
    .logo-container img { max-width: 130px !important; }

    .sidebar-footer {
        color: #999999;
        font-size: 0.75rem;
        margin-top: 15px;
        line-height: 1.4;
    }
    .footer-item { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
    
    /* Estilo para el link de WhatsApp con Logo */
    .ws-link {
        display: flex;
        align-items: center;
        gap: 6px;
        text-decoration: none !important;
        color: #999999 !important;
        transition: all 0.3s;
    }
    .ws-link:hover {
        color: #ffffff !important;
        font-weight: bold !important;
    }
    .ws-icon-img {
        width: 18px;
        height: 18px;
        border-radius: 3px;
        object-fit: cover;
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
    
    # Botones con fuente grande
    if st.button("🚌 1. Transporte"): st.session_state.seccion_activa = "Transporte"
    if st.button("🏨 2. Hotelería"): st.session_state.seccion_activa = "Hotelería"
    if st.button("🏞️ 3. Excursiones"): st.session_state.seccion_activa = "Excursiones"
    if st.button("🌙 4. Actividades"): st.session_state.seccion_activa = "Actividades"
    if st.button("🏥 5. Seguro Médico"): st.session_state.seccion_activa = "Seguro"
    if st.button("💰 6. Tarifas"): st.session_state.seccion_activa = "Tarifas"

    st.markdown('<div class="btn-adhesion">', unsafe_allow_html=True)
    if st.button("📝 FICHA DE ADHESIÓN"): st.session_state.seccion_activa = "Adhesión"
    st.markdown('</div>', unsafe_allow_html=True)

    # CONTACTO CON LOGO DE WHATSAPP
    st.markdown(f"""
        <div class="sidebar-footer">
            <div class="footer-item">
                <span>📍 Av. Rivadavia 4532 - Galería Alefa (local 10)</span>
            </div>
            <div class="footer-item">
                <span>📍 Del Cimarrón 1846 - Ituzaingo</span>
            </div>
            <div class="footer-item">
                <span>📞 11 - 4847-6467</span>
            </div>
            <div class="footer-item">
                <a href="https://wa.me/541156096283" target="_blank" class="ws-link">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" class="ws-icon-img">
                    <span>11 - 5609-6283</span>
                </a>
            </div>
            <div class="footer-item">
                <span>✉️ <a href="mailto:info@serranoturismo.com.ar" style="text-decoration:none; color:inherit;">info@serranoturismo.com.ar</a></span>
            </div>
        </div>
    """, unsafe_allow_html=True)

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

