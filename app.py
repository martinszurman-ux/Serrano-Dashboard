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

# 3. CSS: BOTONES GRIS OSCURO MATE, TEXTO BLANCO Y ANCHO TOTAL
st.markdown("""
    <style>
    /* Logo compacto */
    [data-testid="stSidebar"] img {
        max-width: 140px !important;
        margin: 0 auto !important;
        display: block !important;
    }
    
    /* Espaciado del sidebar */
    [data-testid="stSidebarContent"] {
        padding-top: 1rem !important;
    }

    /* ESTILO DE LOS BOTONES: GRIS OSCURO MATE */
    div.stButton > button {
        background: linear-gradient(145deg, #444444, #2c2c2c) !important;
        color: white !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 8px !important;
        
        /* FUERZA EL MISMO ANCHO Y ALTO */
        width: 100% !important;
        min-width: 100% !important;
        height: 45px !important;
        
        font-weight: 700 !important; /* Negrita */
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 20px !important;
        
        transition: all 0.2s ease-in-out !important;
        margin-bottom: 5px !important;
    }
    
    /* Efecto Hover */
    div.stButton > button:hover {
        background: #1a1a1a !important;
        border-color: #000000 !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3) !important;
        transform: scale(1.02);
    }

    /* ESTILO ESPECIAL PARA FICHA DE ADHESIÓN (Más resaltado) */
    .btn-adhesion div.stButton > button {
        background: linear-gradient(145deg, #1a1a1a, #000000) !important;
        border: 2px solid #d32f2f !important; /* Un borde sutil rojo para diferenciar */
        margin-top: 15px !important;
        justify-content: center !important;
        padding-left: 0px !important;
    }

    /* Ajuste para que los iconos no se peguen al texto */
    div.stButton > button p {
        margin: 0 !important;
        font-size: 14px !important;
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
    st.write("") # Espacio pequeño

    # Menú de botones unificados
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

    # Botón de Adhesión (Diferenciado)
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
