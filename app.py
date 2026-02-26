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

# 3. CSS PARA BOTONES MATE (Comunes y Adhesión)
st.markdown("""
    <style>
    /* Estilo para los botones de sección */
    div.stButton > button {
        background: linear-gradient(145deg, #f0f0f0, #e6e6e6) !important;
        color: #495057 !important;
        border: 1px solid #d1d1d1 !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        width: 100% !important;
        text-align: left !important;
        transition: all 0.3s ease !important;
        margin-bottom: -10px !important;
    }
    
    div.stButton > button:hover {
        border-color: #bcbcbc !important;
        background: linear-gradient(145deg, #e6e6e6, #d9d9d9) !important;
        transform: translateX(5px);
    }

    /* Estilo para el botón ACTIVO (el que está seleccionado) */
    .stButton [data-testid="baseButton-secondaryContainer"] {
        /* Streamlit usa identificadores dinámicos, pero podemos forzar vía lógica de Python */
    }

    /* Estilo especial para el botón de ADHESIÓN (Gris Oscuro) */
    .btn-adhesion > div.stButton > button {
        background: linear-gradient(145deg, #495057, #343a40) !important;
        color: white !important;
        border: 1px solid #212529 !important;
        margin-top: 20px !important;
    }
    
    .btn-adhesion > div.stButton > button:hover {
        background: linear-gradient(145deg, #343a40, #212529) !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN EN SIDEBAR
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Transporte"

with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    
    st.write("### 📂 Menú Principal")
    
    # Botones de navegación
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

    st.divider()
    
    # Botón de Adhesión con contenedor para estilo especial
    st.markdown('<div class="btn-adhesion">', unsafe_allow_html=True)
    if st.button("📝 SOLICITUD DE ADHESIÓN"):
        st.session_state.seccion_activa = "Adhesión"
    st.markdown('</div>', unsafe_allow_html=True)

# 5. RENDERIZADO DE LA SECCIÓN SELECCIONADA
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
