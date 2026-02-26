import streamlit as st
from datetime import datetime

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# FUNCIÓN: Persistencia de datos y Función de Impresión Real
# =================================================================

def render_adhesion(logo_url):
    # 1. CSS de Alta Fidelidad para impresión
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            border-radius: 10px !important;
            font-weight: bold !important;
        }
        @media print {
            header, [data-testid="stSidebar"], .no-print, .stButton, footer {
                display: none !important;
            }
            .main .block-container { padding: 1cm !important; }
            input { border: none !important; font-weight: bold !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    st.image(logo_url, width=150)
    st.markdown("<h1 style='text-align: center;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)

    # 2. Inicializar el estado para que los botones "funcionen"
    if 'formulario_listo' not in st.session_state:
        st.session_state.formulario_listo = False

    # 3. Formulario de Captura
    with st.form("ficha_adhesion"):
        col1, col2, col3, col4 = st.columns(4)
        fecha = col1.date_input("Fecha", datetime.now())
        cliente = col2.text_input("Cliente N°")
        contrato = col3.text_input("Contrato")
        lo = col4.text_input("% L.O.")

        c_ins, c_anio = st.columns(2)
        colegio = c_ins.text_input("Colegio / Instituto")
        division = c_anio.text_input("Año y División")

        st.markdown("---")
        st.write("### DATOS DEL ALUMNO")
        ca1, ca2 = st.columns(2)
        apellido = ca1.text_input("Apellido")
        nombre = ca2.text_input("Nombres")
        dni = ca1.text_input("D.N.I. Nº")
        venc_dni = ca2.date_input("Vencimiento D.N.I.")
        f_nac = ca1.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
        sexo = ca2.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        st.markdown("---")
        st.write("### DATOS DE LOS PADRES")
        ct1, ct2 = st.columns(2)
        padre1 = ct1.text_input("Madre / Padre / Tutor (1)")
        dni1 = ct1.text_input("D.N.I. (1)")
        padre2 = ct2.text_input("Madre / Padre / Tutor (2)")
        dni2 = ct2.text_input("D.N.I. (2)")
        
        email = st.text_input("E-mail de contacto")
        
        st.markdown("---")
        plan_sel = st.pills("Seleccione Plan de Pago:", ["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"])
        
        st.markdown(f"""
            <div style="font-size: 0.9rem; text-align: justify; border: 1px solid #ccc; padding: 15px; color: black;">
            Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
            a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br><br>
            Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato.<br><br>
            Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representantes del contingente de referencia.<br>
            <b>NOTA:</b> de no marcarse ningun plan de pago, su chequera se emitira como <b>PLAN 1</b>.
            </div>
        """, unsafe_allow_html=True)

        # Firmas
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        fcol1, fcol2 = st.columns(2)
        fcol1.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Firma</p>", unsafe_allow_html=True)
        fcol2.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Aclaración y DNI</p>", unsafe_allow_html=True)

        # BOTÓN DE VISTA PREVIA (Dentro del form)
        submit = st.form_submit_button("🔍 GENERAR VISTA PREVIA")
        if submit:
            st.session_state.formulario_listo = True

    # 4. BOTÓN DE IMPRESIÓN (Solo aparece si se presionó Vista Previa)
    if st.session_state.formulario_listo:
        st.success("✅ Ficha generada correctamente. Ahora puede descargarla o imprimirla.")
        if st.button("💾 DESCARGAR / IMPRIMIR PDF"):
            st.write('<script>window.print();</script>', unsafe_allow_html=True)
