import streamlit as st
from secciones import landing_sanpedro, landing_carlospaz

# 1. Configuración de la página (esto debe ir PRIMERO)
st.set_page_config(
    page_title="Portal Turístico: San Pedro & Carlos Paz",
    page_icon="📍",
    layout="wide"
)

# 2. Estilos personalizados (opcional, para darle onda)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar para Navegación
st.sidebar.image("https://www.gstatic.com/images/branding/product/2x/maps_96in128dp.png", width=100)
st.sidebar.title("📍 Guía de Destinos")
st.sidebar.markdown("Seleccioná la ciudad que querés explorar:")

# Diccionario de rutas para mantener el código limpio
PAGINAS = {
    "Carlos Paz ☀️": landing_carlospaz,
    "San Pedro 🍊": landing_sanpedro
}

# Selector de radio en el sidebar
seleccion = st.sidebar.radio("Navegar a:", list(PAGINAS.keys()))

# 4. Renderizado dinámico
st.sidebar.divider()
st.sidebar.caption("Proyecto Landing Pages 2026")

# Ejecutamos la función render() del archivo seleccionado
if seleccion in PAGINAS:
    PAGINAS[seleccion].render()

# 5. Footer simple
st.divider()
st.center = st.markdown(
    "<p style='text-align: center; color: grey;'>© 2026 - Todos los derechos reservados</p>", 
    unsafe_allow_html=True
)
