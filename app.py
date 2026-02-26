import streamlit as st
from secciones.seguro import render_seguro
from secciones.adhesion import render_adhesion
from secciones.tarifas import render_tarifas
from secciones.standard import render_standard

# Configuración de página
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# Logo y Sidebar
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    opcion = st.radio("📂 Navegación", [
        "Tarifas y Formas de Pago", 
        "Transporte", "Hotelería", "Excursiones", 
        "Solicitud de Adhesión", "Seguro Médico"
    ])
    st.sidebar.divider()
    st.sidebar.caption("Serrano Turismo - 29 años")

# Lógica de Navegación Modular
if opcion == "Seguro Médico":
    render_seguro()
elif opcion == "Solicitud de Adhesión":
    render_adhesion(LOGO_URL)
elif opcion == "Tarifas y Formas de Pago":
    render_tarifas(destino)
else:
    render_standard(destino, opcion)
