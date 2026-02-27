import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: FINAL - TEXTO LEGAL ACTUALIZADO
# =================================================================

def render_adhesion(logo_url):
    # CSS para garantizar visibilidad de etiquetas y diseño limpio
    st.markdown("""
        <style>
        .main { background-color: white !important; }
        .main .block-container { 
            padding-top: 2rem !important; 
            color: black !important;
        }
        label p {
            color: black !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
        }
        input {
            color: black !important;
            background-color: #f8f9fa !important;
            border: 1px solid #ced4da !important;
        }
        @media print {
            .no-print, [data-testid="stHeader"], [data-testid="stSidebar"], .stButton { display: none !important; }
            input { border: none !important; border-bottom: 1px solid #000 !important; background: transparent !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CABECERA ---
    c_logo, c_tit = st.columns([1, 4])
    with c_logo:
        st.image(logo_url, width=80)
    with c_tit:
        st.markdown("<h1 style='color: black; margin: 0;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; color: black;'>Serrano Turismo - Ficha de Adhesión</p>", unsafe_allow_html=True)

    st.markdown("---")

    # --- DATOS DE CONTROL ---
    st.markdown("### 📋 DATOS DE CONTROL")
    c1, c2, c3, c4 = st.columns(4)
    c1.date_input("Fecha de Solicitud", datetime.now())
    c2.text_input("N° de Cliente", key="ctrl_nclie")
    c3.text_input("N° de Contrato", key="ctrl_contr")
    c4.text_input("% Localidad", key="ctrl_loc")

    inst1, inst2 = st.columns([2, 1])
    inst1.text_input("Establecimiento Educativo (Colegio / Instituto)", key="ctrl_inst")
    inst2.text_input("Año / División", key="ctrl_anio")

    st.markdown("---")
    
    # --- DATOS DEL PASAJERO ---
    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap1, nom1 = st.columns(2)
    ap1.text_input("Apellido/s", key="pas_ape")
    nom1.text_input("Nombre/s", key="pas_nom")
    
    cd1, cd2, cd3 = st.columns([1, 1, 1])
    cd1.text_input("DNI / CUIL", key="pas_dni")
    cd2.text_input("Fecha
