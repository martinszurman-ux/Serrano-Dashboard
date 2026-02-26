import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: Optimización A4 (Una sola hoja)
# =================================================================

def render_adhesion(logo_url):
    # CSS para forzar una sola hoja en el PDF
    st.markdown("""
        <style>
        @media print {
            /* Forzar tamaño A4 y eliminar márgenes del navegador */
            @page {
                size: A4;
                margin: 0.5cm;
            }
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            /* Compactar espacios */
            .main .block-container {
                padding-top: 0 !important;
                padding-bottom: 0 !important;
            }
            h2 { font-size: 1.5rem !important; margin-bottom: 0 !important; }
            p, div, label { font-size: 10pt !important; }
            .stMarkdown { line-height: 1.1 !important; }
            
            /* Ajustar inputs para que no ocupen lugar de más */
            input {
                border: none !important;
                font-weight: bold !important;
                padding: 0 !important;
                height: auto !important;
            }
            hr { margin: 0.5em 0 !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera Compacta
    st.image(logo_url, width=120)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: -10px;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 0;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    # --- CAMPOS DE ENTRADA DIRECTA ---
    col1, col2, col3, col4 = st.columns(4)
    col1.date_input("Fecha", datetime.now())
    col2.text_input("Cliente N°")
    col3.text_input("Contrato")
    col4.text_input("% L.O.")

    c_ins, c_anio = st.columns(2)
    c_ins.text_input("Colegio / Instituto")
    c_anio.text_input("Año y División")

    st.markdown("---")
    st.write("**DATOS DEL ALUMNO**")
    ca1, ca2 = st.columns(2)
    ca1.text_input("Apellido")
    ca2.text_input("Nombres")
    
    col_dni1, col_dni2, col_dni3 = st.columns(3)
    col_dni1.text_input("D.N.I. Nº")
    col_dni2.date_input("Vencimiento D.N.I.") 
    col_dni3.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
    
    ca2.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

    cd1, cd2, cd3 = st.columns([2, 1, 1])
    cd1.text_input("Domicilio")
    cd2.text_input("C.P.")
    cd3.text_input("Localidad")

    st.markdown("---")
    st.write("**DATOS DE LOS PADRES**")
    ct1, ct2 = st.columns(2)
    ct1.text_input("Madre / Padre / Tutor (1)")
    ct1.text_input("D.N.I. (1)")
    ct2.text_input("Madre / Padre / Tutor (2)")
    ct2.text_input("D.N.I. (2)")
    
    st.text_input("E-mail de contacto")
    st.text_area("Observaciones", height=60)

    st.markdown("---")
    st.write("**PLAN DE PAGO ELEGIDO**")
    plan_sel = st.pills("Seleccione:", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], label_visibility="collapsed")
    if plan_sel == "OTROS":
        st.text_input("Aclarar plan:")

    # TEXTO LEGAL COMPACTO
    st.markdown(f"""
        <div style="font-size: 0.8rem; text-align: justify; border: 1px solid #ccc; padding: 10px; color: black; background: #fff; line-height: 1.2;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
        a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br>
        Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato.<br>
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representantes del contingente de referencia. 
        <b>NOTA:</b> de no marcarse ningun plan de pago, su chequera se emitira como <b>PLAN 1</b>.
        </div>
    """, unsafe_allow_html=True)

    # ESPACIO DE FIRMAS
    st.markdown("<br>", unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:9pt;'>Firma</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:9pt;'>Aclaración y DNI</p>", unsafe_allow_html=True)

    # --- BOTÓN DE IMPRESIÓN ---
    st.markdown("<div class='no-print'><br></div>", unsafe_allow_html=True)
    components.html(
        """
        <html>
            <body>
                <button style="background-color: #2E7D32; color: white; padding: 15px; border: none; border-radius: 12px; cursor: pointer; width: 100%; font-size: 18px; font-weight: bold;" 
                onclick="window.parent.print()">🖨️ GENERAR PDF (UNA SOLA HOJA)</button>
            </body>
        </html>
        """,
        height=100,
    )
