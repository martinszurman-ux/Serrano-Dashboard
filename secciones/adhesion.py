import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# =================================================================

def render_adhesion(logo_url):
    # CSS para forzar visibilidad y estilo profesional
    st.markdown("""
        <style>
        .main { background-color: white !important; }
        .main .block-container { 
            padding-top: 3.5rem !important; 
            color: black !important;
        }
        label p {
            color: black !important;
            font-weight: 600 !important;
        }
        input {
            color: black !important;
            background-color: #f0f2f6 !important;
            border: 1px solid #dcdcdc !important;
        }
        @media (max-width: 768px) {
            [data-testid="stHorizontalBlock"] {
                flex-direction: row !important;
                display: flex !important;
                flex-wrap: nowrap !important;
            }
            [data-testid="column"] {
                width: auto !important;
                flex: 1 1 auto !important;
            }
        }
        @media print {
            .no-print, [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
            .main .block-container { padding: 0 !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CABECERA ---
    head1, head2 = st.columns([1, 4])
    with head1:
        st.image(logo_url, width=60)
    with head2:
        st.markdown("<h2 style='color: black; margin: 0;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    
    st.markdown("<p style='font-weight: bold; color: black;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    # --- DATOS DE CONTROL ---
    c1, c2, c3, c4 = st.columns(4)
    c1.date_input("Fecha", datetime.now())
    c2.text_input("N° Clie")
    c3.text_input("Contr")
    c4.text_input("% LO")

    c_ins, c_anio = st.columns([2, 1])
    c_ins.text_input("Colegio / Instituto")
    c_anio.text_input("Año/Div")

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)
    
    # --- DATOS DEL PASAJERO ---
    st.write("**DATOS DEL PASAJERO**")
    ca1, ca2 = st.columns(2)
    ca1.text_input("Apellido")
    ca2.text_input("Nombres")
    
    cd1, cd2, cd3 = st.columns([1.5, 1.2, 1.3])
    cd1.text_input("DNI/CUIL")
    cd2.text_input("Vence") 
    cd3.date_input("Nace", min_value=datetime(1990,1,1))
    
    st.radio("Sexo", ["Masc", "Fem", "X"], horizontal=True)

    dom1, dom2 = st.columns([2, 1])
    dom1.text_input("Domicilio")
    dom2.text_input("Loc/CP")

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)
    
    # --- DATOS DE TUTORES ---
    st.write("**DATOS DE TUTORES**")
    cp1_a, cp1_c = st.columns([2, 1])
    cp1_a.text_input("Tutor 1")
    cp1_c.text_input("Tel 1")
    
    cp2_a, cp2_c = st.columns([2, 1])
    cp2_a.text_input("Tutor 2")
    cp2_c.text_input("Tel 2")
    
    st.text_input("E-mail:")

    # --- PLANES ---
    st.pills("Planes de Pago", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTRO"], default="PLAN 1")

    # --- LEGAL ---
    st.markdown("""
        <div style="font-size: 0.7rem; text-align: justify; border: 1px solid #ccc; padding: 8px; background-color: #f9f9f9; color: black; border-radius: 5px;">
        Declaro bajo juramento que los datos aqui volcados son exactos y acepto
