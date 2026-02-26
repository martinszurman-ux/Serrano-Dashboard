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

# 3. CSS MAESTRO: LOGO CENTRADO, SUBIR MENÚ Y NOTAS DISCRETAS
st.markdown("""
    <style>
    /* Eliminar espacios superiores del sidebar */
    [data-testid="stSidebarContent"] {
        padding-top: 0.5rem !important; 
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }

    /* CONTENEDOR PARA CENTRADO ABSOLUTO DEL LOGO */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-bottom: -10px !important;
        margin-top: -10px !important;
    }
    
    .logo-container img {
        max-width: 130px !important;
    }

    /* Reducir espacio de divisores */
    [data-testid="stSidebar"] hr {
        margin: 0.4rem 0 !important;
    }

    /* BOTONES MATE (SE MANTIENEN IGUAL) */
    [data-testid="stVerticalBlock"] > div {
        width: 100% !important;
        gap: 0.1rem !important;
    }

    .stButton, .stButton button {
        width: 100% !important;
    }

    div.stButton > button {
        background: linear-gradient(145deg, #444444, #2c2c2c) !important;
        color: white !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 8px !important;
        height: 46px !important;
        padding: 0px 20px !important;
        font-weight: 700 !important;
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        transition: all 0.3s ease !important;
        margin-bottom: -6px !important;
    }
    
    div.stButton > button:hover {
        background: #555555 !important;
        border-color: #ffffff !important;
        transform: translateX(4px) !important;
    }

    /* Botón de Adhesión */
    .btn-adhesion div.stButton > button {
        background: linear-gradient(145deg, #1a1a1a, #000000) !important;
        border: 1px solid #555555 !important;
        margin-top: 8px !important;
        justify-content: center !important;
    }

    /* ESTILO PARA LAS NOTAS DISCRETAS AL FINAL */
    .sidebar-notes {
        color: #888888;
        font-size: 0.7rem;
        text-align: center;
        margin-top: 20px;
        line-height: 1.2;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Transporte"

with st.sidebar:
    # LOGO CENTRADO USANDO DIV
    st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}"></div>', unsafe_allow_html=True)
    st.divider()
    
    destino = st.selectbox("📍 Destino", ["Villa Carlos Paz", "San Pedro"])
    
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

    # NOTAS DISCRETAS (No pusiste el texto, así que puse ejemplos de Serrano)
    st.markdown("""
        <div class="sidebar-notes">
            Serrano Turismo ® 2026<br>
            Legajo N° 12345 - Disp. 678/20<br>
            Todos los derechos reservados.
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
