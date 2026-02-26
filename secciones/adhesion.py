import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: Cambio DNI a CUIL + Bloqueo de Segunda Hoja
# =================================================================

def render_adhesion(logo_url):
    # CSS para forzar carilla única y eliminar la hoja fantasma
    st.markdown("""
        <style>
        .main .block-container { 
            padding-top: 0rem !important; 
            padding-bottom: 0rem !important; 
        }
        [data-testid="stHeader"] { display: none !important; }
        
        @media print {
            @page {
                size: A4;
                margin: 0.4cm; 
            }
            /* ESCALADO PARA UNA CARILLA */
            html, body {
                zoom: 92%; 
                height: 100%;
                max-height: 100%;
                overflow: hidden !important;
            }
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, iframe, [data-testid="stHeader"] {
                display: none !important;
                visibility: hidden !important;
                height: 0 !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            
            h2 { font-size: 1.3rem !important; margin-top: -15px !important; margin-bottom: 2px !important; }
            p, div, label { font-size: 9pt !important; line-height: 1.0 !important; }
            
            /* Inputs compactos */
            input, textarea { 
                border: none !important; 
                background: transparent !important; 
                font-weight: bold !important;
                color: black !important;
            }
            hr { margin: 4px 0 !important; }
            [data-testid="stVerticalBlock"] > div { margin-top: -9px !important; }
            
            .bloque-firmas {
                margin-top: 40px !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera
    st.image(logo_url, width=80)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: -25px;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold; margin-top: -5px;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    # --- DATOS DE CONTROL ---
    col1, col2, col3, col4 = st.columns(4)
    col1.date_input("Fecha", datetime.now())
    col2.text_input("Cliente N°")
    col3.text_input("Contrato")
    col4.text_input("% L.O.")

    c_ins, c_anio = st.columns([2, 1])
    c_ins.text_input("Colegio / Instituto")
    c_anio.text_input("Año y División")

    st.markdown("---")
    
    # --- DATOS DEL ALUMNO ---
    st.write("**DATOS DEL ALUMNO / PASAJERO**")
    ca1, ca2 = st.columns(2)
    ca1.text_input("Apellido")
    ca2.text_input("Nombres")
    
    cd1, cd2, cd3 = st.columns([2, 1, 1])
    cd1.text_input("C.U.I.L. Nº") # CAMBIO A CUIL
    cd2.date_input("Vencimiento C.U.I.L.") # CAMBIO A CUIL
    cd3.date_input("Nacimiento", min_value=datetime(1990,1,1))
    
    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

    dom1, dom2, dom3 = st.columns([2, 1, 1])
    dom1.text_input("Domicilio")
    dom2.text_input("C.P.")
    dom3.text_input("Localidad")

    st.markdown("---")
    
    # --- DATOS DE LOS PADRES ---
    st.write("**DATOS DE LOS PADRES / TUTORES**")
    
    cp1_a, cp1_b, cp1_c = st.columns([2, 1, 1])
    cp1_a.text_input("Madre / Padre / Tutor (1)")
    cp1_b.text_input("C.U.I.L. (1)") # CAMBIO A CUIL
    cp1_c.text_input("Teléfono (1)")
    
    cp2_a, cp2_b, cp2_c = st.columns([2, 1, 1])
    cp2_a.text_input("Madre / Padre / Tutor (2)")
    cp2_b.text_input("C.U.I.L. (2)") # CAMBIO A CUIL
    cp2_c.text_input("Teléfono (2)")
    
    st.text_input("E-mail de contacto:")
    st.text_area("Observaciones:", height=50)

    st.markdown("---")
    
    # --- PLANES ---
    st.write("**Seleccione su Plan de Pago:**")
    st.pills("Planes", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], default="PLAN 1", label_visibility="collapsed")

    # TEXTO LEGAL
    st.markdown(f"""
        <div style="font-size: 0.8rem; text-align: justify; border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9; color: black; line-height: 1.1;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
        a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br>
        Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato. 
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto. 
        <b>NOTA:</b> de no marcarse plan, se emitira como <b>PLAN 1</b>.
        </div>
    """, unsafe_allow_html=True)

    # --- FIRMAS ---
    st.markdown('<div class="bloque-firmas">', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:8pt;'>Firma del Responsable</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:8pt;'>Aclaración y C.U.I.L.</p>", unsafe_allow_html=True) # CAMBIO A CUIL
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
