import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: Final Estructurada
# =================================================================

def render_adhesion(logo_url):
    # CSS para forzar visibilidad y estilo profesional
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
            font-size: 0.85rem !important;
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
                gap: 5px !important;
            }
            [data-testid="column"] {
                width: auto !important;
                min-width: 0px !important;
                flex: 1 1 auto !important;
            }
            h2 { font-size: 1.1rem !important; }
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
    head1, head2 = st.columns([1, 4])
    with head1:
        st.image(logo_url, width=60)
    with head2:
        st.markdown("<h2 style='color: black; margin-top: 5px;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    
    st.markdown("<p style='font-weight: bold; color: black; margin-top: -15px;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

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
    
    cd1, cd2, cd3 = st.columns([1.2, 1.4, 1.4])
    cd1.text_input("DNI/CUIL")
    cd2.text_input("Fecha de Vencimiento DNI") 
    cd3.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
    
    st.radio("Sexo", ["Masc", "Fem", "X"], horizontal=True)

    dom1, dom2 = st.columns([2, 1])
    dom1.
