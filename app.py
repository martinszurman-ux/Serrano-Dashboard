import streamlit as st
import os

# 1. Importación de las secciones modulares
# Asegúrate de que los archivos existan en la carpeta /secciones
from secciones.tarifas import render_tarifas
from secciones.adhesion import render_adhesion
from secciones.seguro import render_seguro
from secciones.transporte import render_transporte
from secciones.hoteleria import render_hoteleria
from secciones.excursiones import render_excursiones
from secciones.actividades_nocturnas import render_nocturnas
from secciones.standard import render_standard

# 2. Configuración general de la página
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# 3. Estilos Globales (CSS que comparten todas las secciones)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Estilo para los Headers de cada sección */
    .header-container {
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        background-color: #495057;
        margin-bottom: 30px;
    }
    .header-text-overlay {
        color: white;
        font-size: 2.2rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Estilos para los Widgets 3D (Se usan en Tarifas y Seguro) */
    .widget-3d-grad, .widget-3d-inner {
        background: linear-gradient(145deg, #f0f0f0, #ffffff);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        border: 1px solid #e0e0e0;
        box-shadow: 8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff;
        margin-bottom: 15px;
    }

    .widget-title { color: #6c757d; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; }
    .widget-value { color: #212529; font-size: 2.2rem; font-weight: 800; margin: 0; }
    
    /* Ocultar botones de navegación visualmente para usar las tarjetas como botones */
    .stButton button {
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Sidebar y Navegación
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    
    # Selección de Destino (Villa Carlos Paz o San Pedro)
    # Basado en la configuración de carpetas
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    
    st.divider()
    
    # Menú de navegación principal
    opcion = st.radio("📂 Navegación", [
        "Tarifas y Formas de Pago", 
        "Transporte", 
        "Hotelería", 
        "Excursiones", 
        "Actividades Nocturnas",
        "Solicitud de Adhesión", 
        "Seguro Médico"
    ])
    
    st.sidebar.divider()
    st.sidebar.caption("Serrano Turismo - 29 años de trayectoria")

# 5. Lógica de Enrutamiento (Ejecución de módulos)
# Cada función render_X recibe los parámetros necesarios para funcionar
if opcion == "Tarifas y Formas de Pago":
    render_tarifas(destino)

elif opcion == "Transporte":
    render_transporte(destino)

elif opcion == "Hotelería":
    render_hoteleria(destino)

elif opcion == "Excursiones":
    render_excursiones(destino)

elif opcion == "Actividades Nocturnas":
    render_nocturnas(destino)

elif opcion == "Solicitud de Adhesión":
    # Le pasamos el logo para que lo use en la cabecera del formulario
    render_adhesion(LOGO_URL)

elif opcion == "Seguro Médico":
    render_seguro()

else:
    # Para cualquier otra opción que use la lógica estándar de CSV
    render_standard(destino, opcion)
