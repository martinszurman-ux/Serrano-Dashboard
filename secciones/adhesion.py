import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: Texto legal completo + Fix Mobile Columns
# =================================================================

def render_adhesion(logo_url):
    # CSS para control de impresión y forzado de columnas en Mobile
    st.markdown("""
        <style>
        /* Ajustes de contenedor principal */
        .main .block-container { 
            padding-top: 1rem !important; 
            padding-bottom: 1rem !important; 
            max-width: 95% !important;
        }
        [data-testid="stHeader"] { display: none !important; }

        /* --- TRUCO PARA MOBILE: Forzar columnas a no apilarse --- */
        [data-testid="column"] {
            min-width: 0px !important;
            flex-basis: 0% !important;
            flex-grow: 1 !important;
        }
        
        /* Ajuste de fuentes y espaciado para legibilidad */
        label p { font-size: 0.8rem !important; margin-bottom: 2px !important; }
        .stInput input { height: 32px !important; font-size: 0.9rem !important; }
        
        /* Estilos específicos para IMPRESIÓN */
        @media print {
            @page {
                size: A4;
                margin: 0.4cm; 
            }
            html, body {
                zoom: 88%; 
                height: 100%;
                overflow: hidden !important;
                background-color: white !important;
            }
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, iframe, [data-testid="stHeader"] {
                display: none !important;
                visibility: hidden !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            
            h2 { font-size: 1.2rem !important; margin-top: -20px !important; margin-bottom: 2px !important; }
            p, div, label { font-size: 8pt !important; line-height: 1.0 !important; color: black !important; }
            
            input { 
                border: none !important; 
                border-bottom: 1px solid #ccc !important;
                background: transparent !important; 
                font-weight: bold !important;
            }
            hr { margin: 4px 0 !important; border: 0.5px solid #eee !important; }
            [data-testid="stVerticalBlock"] > div { margin-top: -12px !important; }
            
            .bloque-firmas {
                margin-top: 30px !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CABECERA ---
    st.image(logo_url, width=70)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: -35px;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold; margin-top: -10px;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    # --- DATOS DE CONTROL ---
    c1, c2, c3, c4 = st.columns(4)
    c1.date_input("Fecha", datetime.now())
    c2.text_input("N° Cliente")
    c3.text_input("Contrato")
    c4.text_input("% L.O.")

    c_ins, c_anio = st.columns([2, 1])
    c_ins.text_input("Colegio / Instituto")
    c_anio.text_input("Año y División")

    st.markdown("---")
    
    # --- DATOS DEL ALUMNO ---
    st.write("**DATOS DEL ALUMNO / PASAJERO**")
    ca1, ca2 = st.columns(2)
    ca1.text_input("Apellido")
    ca2.text_input("Nombres")
    
    cd1, cd2, cd3 = st.columns([1.5, 1.2, 1.3])
    cd1.text_input("DNI / CUIL")
    cd2.text_input("Vence DNI") 
    cd3.date_input("Nacimiento", min_value=datetime(1990,1,1))
    
    st.radio("Sexo", ["Masc", "Fem", "X"], horizontal=True)

    dom1, dom2 = st.columns([2, 1])
    dom1.text_input("Domicilio")
    dom2.text_input("Localidad / CP")

    st.markdown("---")
    
    # --- DATOS DE LOS PADRES ---
    st.write("**DATOS DE LOS PADRES / TUTORES**")
    
    cp1_a, cp1_c = st.columns([2, 1])
    cp1_a.text_input("Madre / Padre / Tutor (1)")
    cp1_c.text_input("Teléfono (1)")
    
    cp2_a, cp2_c = st.columns([2, 1])
    cp2_a.text_input("Madre / Padre / Tutor (2)")
    cp2_c.text_input("Teléfono (2)")
    
    st.text_input("E-mail de contacto:")
    st.text_input("Observaciones:")

    st.markdown("---")
    
    # --- PLANES ---
    st.write("**Seleccione su Plan de Pago:**")
    st.pills("Planes", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], default="PLAN 1", label_visibility="collapsed")

    # --- TEXTO LEGAL COMPLETO ---
    st.markdown(f"""
        <div style="font-size: 0.78rem; text-align: justify; border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9; color: black; line-height: 1.2; border-radius: 5px;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br><br>
        Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato. 
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto.<br><br>
        <b>NOTA: de no marcarse plan, se emitira como PLAN 1.</b>
        </div>
    """, unsafe_allow_html=True)

    # --- FIRMAS ---
    st.markdown('<div class="bloque-firmas" style="margin-top: 25px;">', unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt;'>Firma del Responsable</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt;'>Aclaración y C.U.I.L.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BOTÓN DE IMPRESIÓN ---
    st.markdown("<div class='no-print'><br></div>", unsafe_allow_html=True)
    components.html(
        """
        <html>
            <body>
                <button style="background-color: #2E7D32; color: white; padding: 12px; border: none; border-radius: 10px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold;" 
                onclick="window.parent.print()">🖨️ GENERAR PDF (CARILLA ÚNICA)</button>
            </body>
        </html>
        """,
        height=80,
    )
