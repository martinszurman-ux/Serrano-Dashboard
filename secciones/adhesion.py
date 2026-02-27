import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: Ultra-Fix Mobile (Nombres de Planes Corregidos)
# =================================================================

def render_adhesion(logo_url):
    # CSS Total para corregir visibilidad en Mobile y modo oscuro
    st.markdown("""
        <style>
        /* 1. Reset de visibilidad y colores (Anti Modo Oscuro) */
        .main {
            background-color: white !important;
        }
        .main .block-container { 
            padding-top: 3.5rem !important; /* Espacio para el menú superior */
            padding-bottom: 1rem !important; 
            color: black !important;
        }

        /* Forzar etiquetas visibles */
        label p {
            color: black !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
        }

        /* Forzar inputs legibles */
        input {
            color: black !important;
            background-color: #f0f2f6 !important;
            border: 1px solid #dcdcdc !important;
        }

        /* 2. FIX MENÚ: Mostrar cabecera nativa */
        [data-testid="stHeader"] { 
            display: flex !important; 
            visibility: visible !important;
            background-color: rgba(255,255,255,0.9) !important;
        }

        /* 3. TRUCO COLUMNAS MOBILE: Forzar 2 o más por fila */
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
            /* Achicar un poco los textos en móvil para que entren */
            h2 { font-size: 1.1rem !important; }
            .stMarkdown p { font-size: 0.8rem !important; }
        }

        /* 4. MODO IMPRESIÓN */
        @media print {
            @page { size: A4; margin: 0.4cm; }
            html, body { zoom: 85%; }
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
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
    
    cd1, cd2, cd3 = st.columns([1.5, 1.2, 1.3])
    cd1.text_input("DNI/CUIL")
    cd2.text_input("Vence") 
    cd3.date_input("Nace", min_value=datetime(1990,1,1))
    
    st.radio("Sexo", ["Masc", "Fem", "X"], horizontal=True)

    dom1, dom2 = st.columns([2, 1])
    dom1.text_input("Domicilio")
    dom2.text_input("Loc/CP")

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)
    
    # --- DATOS DE LOS PADRES ---
    st.write("**DATOS DE TUTORES**")
    cp1_a, cp1_c = st.columns([2, 1])
    cp1_a.text_input("Tutor 1")
    cp1_c.text_input("Tel 1")
    
    cp2_a, cp2_c = st.columns([2, 1])
    cp2_a.text_input("Tutor 2")
    cp2_c.text_input("Tel 2")
    
    st.text_input("E-mail:")

    # --- PLANES (ACTUALIZADO: Nombres completos) ---
    st.pills("Planes", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTRO"], default="PLAN 1")

    # --- TEXTO LEGAL ---
    st.markdown(f"""
        <div style="font-size: 0.7rem; text-align: justify; border: 1px solid #ccc; padding: 8px; background-color: #f9f9f9; color: black; line-height: 1.1; border-radius: 5px;">
        Declaro bajo juramento que los datos aqui volcados son exactos y acepto el plan de pagos de <b>SERRANO TURISMO</b>. 
        Los planes contado vencen a los 30 dias de la firma. Declaro conocer las condiciones del contrato suscripto.<br>
        <b>NOTA: de no marcarse plan, se emitirá como PLAN 1.</b>
        </div>
    """, unsafe_allow_html=True)

    # --- FIRMAS ---
    st.markdown('<div style="margin-top: 20px;">', unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt; color:black;'>Firma Responsable</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt; color:black;'>Aclaración y C.U.I.L.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BOTÓN DE IMPRESIÓN ---
    st.markdown("<div class='no-print'><br></div>", unsafe_allow_html=True)
    components.html(
        """
        <html>
            <body>
                <button style="background-color: #2E7D32; color: white; padding: 12px; border: none; border-radius: 10px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold;" 
                onclick="window.parent.print()">🖨️ GENERAR PDF</button>
            </body>
        </html>
        """,
        height=80,
    )
