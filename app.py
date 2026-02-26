import streamlit as st
from secciones.tarifas import render_tarifas
from secciones.adhesion import render_adhesion
from secciones.seguro import render_seguro
from secciones.transporte import render_transporte
from secciones.hoteleria import render_hoteleria
from secciones.excursiones import render_excursiones
from secciones.actividades_nocturnas import render_nocturnas

st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# Estilos Globales
st.markdown("""
    <style>
    .widget-3d-grad {
        background: linear-gradient(145deg, #f0f0f0, #ffffff);
        border-radius: 20px; padding: 25px; text-align: center;
        border: 1px solid #e0e0e0; box-shadow: 8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff;
        margin-bottom: 15px;
    }
    .header-container { height: 150px; display: flex; align-items: center; justify-content: center; border-radius: 15px; background-color: #495057; margin-bottom: 30px; }
    .header-text-overlay { color: white; font-size: 2.2rem; font-weight: 800; text-transform: uppercase; }
    .widget-title { color: #6c757d; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; }
    .widget-value { color: #212529; font-size: 2.2rem; font-weight: 800; margin: 0; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.image("https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png", use_container_width=True)
    destino = st.selectbox("📍 Destino", ["Villa Carlos Paz", "San Pedro"])
    opcion = st.radio("📂 Navegación", ["Tarifas", "Transporte", "Hotelería", "Excursiones", "Actividades Nocturnas", "Solicitud de Adhesión", "Seguro Médico"])

if opcion == "Tarifas": render_tarifas(destino)
elif opcion == "Transporte": render_transporte(destino)
elif opcion == "Hotelería": render_hoteleria(destino)
elif opcion == "Excursiones": render_excursiones(destino)
elif opcion == "Actividades Nocturnas": render_nocturnas(destino)
elif opcion == "Solicitud de Adhesión": render_adhesion("https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png")
elif opcion == "Seguro Médico": render_seguro()
