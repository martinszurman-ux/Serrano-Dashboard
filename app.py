import streamlit as st
from secciones.adhesion import render_adhesion

# 1. Definir la URL o ruta del logo una sola vez para evitar errores
LOGO_RECURSO = "https://tu-link-del-logo.com/logo.png" # <--- CAMBIÁ ESTO POR TU LINK REAL

# 2. Configuración del Menú Lateral
st.sidebar.image(LOGO_RECURSO, width=150)
st.sidebar.title("Serrano Turismo")
st.sidebar.divider()

menu_opciones = [
    "🚌 TRANSPORTE",
    "🏨 HOTELERIA",
    "☀️ EXCURSIONES DIURNAS",
    "🌙 ACTIVIDADES NOCTURNAS",
    "🏥 SEGURO MEDICO",
    "💰 TARIFAS Y FORMAS DE PAGO",
    "📋 SOLICITUD DE ADHESION"
]

seleccion = st.sidebar.radio("Navegación", menu_opciones)

# 3. Lógica de pantallas
if seleccion == "🚌 TRANSPORTE":
    st.title("🚌 Información de Transporte")
    st.info("Aquí cargaremos las unidades y choferes.")

elif seleccion == "🏨 HOTELERIA":
    st.title("🏨 Hotelería")
    st.info("Detalle de los hoteles confirmados.")

elif seleccion == "☀️ EXCURSIONES DIURNAS":
    st.title("☀️ Excursiones Diurnas")

elif seleccion == "🌙 ACTIVIDADES NOCTURNAS":
    st.title("🌙 Actividades Nocturnas")

elif seleccion == "🏥 SEGURO MEDICO":
    st.title("🏥 Seguro Médico")

elif seleccion == "💰 TARIFAS Y FORMAS DE PAGO":
    st.title("💰 Tarifas y Formas de Pago")

elif seleccion == "📋 SOLICITUD DE ADHESION":
    # Llamamos a la función que ya terminamos
    render_adhesion(LOGO_RECURSO)
