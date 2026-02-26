import streamlit as st
from datetime import datetime

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# FUNCIÓN: Generar Formulario y Descargar/Imprimir PDF
# =================================================================

def render_adhesion(logo_url):
    # 1. CSS de alta fidelidad para que el PDF salga perfecto
    st.markdown("""
        <style>
        /* Estilos para el botón en la web */
        .stButton>button {
            width: 100%;
            background-color: #1E3A8A !important;
            color: white !important;
            border-radius: 10px !important;
            height: 3.5em !important;
            font-size: 1.2rem !important;
            font-weight: bold !important;
            border: none !important;
        }

        /* CONFIGURACIÓN DE PDF / IMPRESIÓN */
        @media print {
            /* Ocultar todo lo que no es el formulario */
            header, [data-testid="stSidebar"], .stButton, .no-print, [data-testid="stHeader"], footer {
                display: none !important;
            }
            /* Reset de márgenes para hoja A4 */
            .main .block-container {
                padding: 1cm !important;
                margin: 0 !important;
            }
            body {
                color: black !important;
                background: white !important;
            }
            /* Hacer que los inputs parezcan texto plano en el PDF */
            input, textarea {
                border: none !important;
                background: transparent !important;
                color: black !important;
                font-weight: bold !important;
            }
            div[data-testid="stForm"] {
                border: 2px solid #000 !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Encabezado del PDF
    st.image(logo_url, width=150)
    st.markdown("<h1 style='text-align: center; color: black;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'><b>Ficha del Cliente / Pasajero</b></p>", unsafe_allow_html=True)

    # Formulario donde el cliente carga los datos
    with st.form("ficha_para_pdf"):
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.date_input("Fecha", datetime.now())
        with col2: st.text_input("Cliente N°")
        with col3: st.text_input("Contrato")
        with col4: st.text_input("% L.O.")

        c_ins, c_anio = st.columns(2)
        with c_ins: st.text_input("Colegio / Instituto")
        with c_anio: st.text_input("Año y División")

        st.markdown("---")
        st.write("### DATOS DEL ALUMNO")
        
        ca1, ca2 = st.columns(2)
        with ca1:
            st.text_input("Apellido")
            st.text_input("D.N.I. Nº")
            st.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
        with ca2:
            st.text_input("Nombres")
            st.date_input("Vencimiento D.N.I.") 
            st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        cd1, cd2, cd3 = st.columns([2, 1, 1])
        with cd1: st.text_input("Domicilio")
        with cd2: st.text_input("C.P.")
        with cd3: st.text_input("Localidad")

        st.markdown("---")
        st.write("### DATOS DE LOS PADRES")
        ct1, ct2 = st.columns(2)
        with ct1: 
            st.text_input("Madre / Padre / Tutor (1)")
            st.text_input("D.N.I. (1)")
        with ct2: 
            st.text_input("Madre / Padre / Tutor (2)")
            st.text_input("D.N.I. (2)")
        
        st.text_input("E-mail de contacto:")
        st.text_area("Observaciones:")

        st.markdown("---")
        st.write("**PLAN DE PAGO ELEGIDO:**")
        plan_sel = st.pills("Selección:", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], label_visibility="collapsed")
        
        st.markdown(f"""
            <div style="font-size: 0.95rem; text-align: justify; border: 2px solid black; padding: 15px; background-color: #f9f9f9; color: black; margin-top: 10px;">
            Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
            a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br><br>
            Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato.<br><br>
            Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representantes del contingente de referencia.<br>
            <b>NOTA:</b> de no marcarse ningun plan de pago, su chequera se emitira como <b>PLAN 1</b>.
            </div>
        """, unsafe_allow_html=True)

        # Espacio para Firmas manuales
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        fcol1, fcol2 = st.columns(2)
        with fcol1:
            st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center;'>Firma del Responsable</p>", unsafe_allow_html=True)
        with fcol2:
            st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center;'>Aclaración y D.N.I.</p>", unsafe_allow_html=True)

        # Botón para fijar los datos en el navegador
        st.form_submit_button("✅ 1. GENERAR VISTA PREVIA")

    # --- BOTÓN DE DESCARGA / IMPRESIÓN ---
    st.markdown("### ⬇️ PASO FINAL")
    if st.button("💾 DESCARGAR FORMULARIO COMPLETADO (PDF)"):
        st.write('<script>window.print();</script>', unsafe_allow_html=True)
