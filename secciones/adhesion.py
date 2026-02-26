import streamlit as st
from datetime import datetime

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: Entrada Directa (Sin Form) para garantizar Impresión
# =================================================================

def render_adhesion(logo_url):
    # 1. CSS de Alta Fidelidad para impresión
    st.markdown("""
        <style>
        /* Estilo del botón de impresión */
        .stButton>button {
            width: 100%;
            padding: 15px;
            background-color: #2E7D32 !important;
            color: white !important;
            font-weight: bold !important;
            font-size: 1.2rem !important;
            border-radius: 10px;
            margin-top: 20px;
        }
        
        @media print {
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            body { color: black !important; background: white !important; }
            /* Estilizar los inputs para que se vean como texto en el PDF */
            div[data-testid="stTextInput"]>div>div>input, 
            div[data-testid="stTextArea"]>div>div>textarea {
                border: none !important;
                color: black !important;
                font-weight: bold !important;
                background: transparent !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera
    st.image(logo_url, width=150)
    st.markdown("<h2 style='text-align: center;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.info("💡 Complete los campos y luego presione el botón verde al final para generar el PDF.")

    # --- CAMPOS DE ENTRADA DIRECTA (Sin st.form para evitar bloqueos) ---
    
    col1, col2, col3, col4 = st.columns(4)
    fecha = col1.date_input("Fecha", datetime.now())
    cliente = col2.text_input("Cliente N°")
    contrato = col3.text_input("Contrato")
    lo = col4.text_input("% L.O.")

    c_ins, c_anio = st.columns(2)
    colegio = c_ins.text_input("Colegio / Instituto")
    division = c_anio.text_input("Año y División")

    st.markdown("---")
    st.write("**DATOS DEL ALUMNO**")
    ca1, ca2 = st.columns(2)
    apellido = ca1.text_input("Apellido")
    nombres = ca2.text_input("Nombres")
    dni = ca1.text_input("D.N.I. Nº")
    venc_dni = ca2.date_input("Vencimiento D.N.I.") 
    f_nac = ca1.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
    sexo = ca2.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

    st.markdown("---")
    st.write("**DATOS DE LOS PADRES**")
    ct1, ct2 = st.columns(2)
    padre1 = ct1.text_input("Madre / Padre / Tutor (1)")
    dni1 = ct1.text_input("D.N.I. (1)")
    padre2 = ct2.text_input("Madre / Padre / Tutor (2)")
    dni2 = ct2.text_input("D.N.I. (2)")
    
    email = st.text_input("E-mail de contacto")
    obs = st.text_area("Observaciones")

    st.markdown("---")
    # Usamos selectbox para asegurar compatibilidad en la impresión
    plan_pago = st.selectbox("Seleccione Plan de Pago:", ["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"])
    
    st.markdown(f"""
        <div style="font-size: 0.9rem; text-align: justify; border: 1px solid #ccc; padding: 15px; color: black; background: #fff;">
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

    # --- BOTÓN DE IMPRESIÓN DIRECTO ---
    # Al no estar en un formulario, este botón siempre está presente y funcional
    st.divider()
    if st.button("🖨️ GENERAR Y DESCARGAR PDF"):
        st.write('<script>window.print();</script>', unsafe_allow_html=True)
