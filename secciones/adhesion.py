import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: DEFINITIVA - ESTRUCTURA COMPLETA
# =================================================================

def render_adhesion(logo_url):
    # CSS para mantener la estética y visibilidad total
    st.markdown("""
        <style>
        .main { background-color: white !important; }
        .main .block-container { 
            padding-top: 3.5rem !important; 
            padding-bottom: 1rem !important; 
            color: black !important;
        }
        label p {
            color: black !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
        }
        input {
            color: black !important;
            background-color: #f0f2f6 !important;
            border: 1px solid #dcdcdc !important;
        }
        /* Fix para que en móvil no se amontonen los campos */
        @media (max-width: 768px) {
            [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
            }
        }
        @media print {
            @page { size: A4; margin: 0.4cm; }
            .no-print, [data-testid="stHeader"], [data-testid="stSidebar"], .stButton { display: none !important; }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            input { border: none !important; border-bottom: 1px solid #000 !important; background: transparent !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CABECERA ---
    col_logo, col_tit = st.columns([1, 4])
    with col_logo:
        st.image(logo_url, width=80)
    with col_tit:
        st.markdown("<h1 style='color: black; margin: 0;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; color: black;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    # --- DATOS DE CONTROL ---
    st.markdown("### 📋 DATOS DE CONTROL")
    c1, c2, c3, c4 = st.columns(4)
    c1.date_input("Fecha de Solicitud", datetime.now())
    c2.text_input("N° de Cliente")
    c3.text_input("N° de Contrato")
    c4.text_input("% Localidad")

    c_ins, c_anio = st.columns([2, 1])
    c_ins.text_input("Establecimiento Educativo (Colegio / Instituto)")
    c_anio.text_input("Año / División")

    st.markdown("---")
    
    # --- DATOS DEL PASAJERO (Nombres extendidos) ---
    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ca1, ca2 = st.columns(2)
    ca1.text_input("Apellido/s")
    ca2.text_input("Nombre/s")
    
    cd1, cd2, cd3 = st.columns([1, 1, 1])
    cd1.text_input("DNI / CUIL")
    cd2.text_input("Fecha de Vencimiento DNI") 
    cd3.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
    
    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

    dom1, dom2 = st.columns([2, 1])
    dom1.text_input("Domicilio Particular")
    dom2.text_input("Localidad / CP")

    st.markdown("---")
    
    # --- DATOS DE LOS PADRES / TUTORES (3 CAMPOS SOLICITADOS) ---
    st.markdown("### 👥 DATOS DE LOS PADRES / TUTORES")
    
    st.write("**Tutor 1**")
