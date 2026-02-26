import streamlit as st
from datetime import datetime

def render_adhesion(logo_url):
    # 1. CSS para que el navegador fuerce la descarga/impresión correctamente
    st.markdown("""
        <style>
        .boton-imprimir {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background-color: #2E7D32;
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1rem;
            border: none;
            width: 100%;
            cursor: pointer;
        }
        @media print {
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            body { color: black !important; background: white !important; }
            input { border: none !important; font-weight: bold !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera
    st.image(logo_url, width=150)
    st.markdown("<h2 style='text-align: center;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)

    # --- ENTRADA DE DATOS DIRECTA ---
    # Usamos columnas pero sin FORM para que el valor sea persistente
    col1, col2, col3, col4 = st.columns(4)
    f_hoy = col1.date_input("Fecha", datetime.now())
    c_num = col2.text_input("Cliente N°")
    cont = col3.text_input("Contrato")
    lo = col4.text_input("% L.O.")

    c_ins, c_anio = st.columns(2)
    inst = c_ins.text_input("Colegio / Instituto")
    div = c_anio.text_input("Año y División")

    st.markdown("---")
    st.write("**DATOS DEL ALUMNO**")
    ca1, ca2 = st.columns(2)
    ape = ca1.text_input("Apellido")
    nom = ca2.text_input("Nombres")
    dni = ca1.text_input("D.N.I. Nº")
    v_dni = ca2.date_input("Vencimiento D.N.I.")
    f_nac = ca1.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
    sexo = ca2.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

    st.markdown("---")
    st.write("**DATOS DE LOS PADRES**")
    ct1, ct2 = st.columns(2)
    p1 = ct1.text_input("Madre / Padre / Tutor (1)")
    d1 = ct1.text_input("D.N.I. (1)")
    p2 = ct2.text_input("Madre / Padre / Tutor (2)")
    d2 = ct2.text_input("D.N.I. (2)")
    
    email = st.text_input("E-mail de contacto")
    obs = st.text_area("Observaciones")

    st.markdown("---")
    plan = st.selectbox("Plan de Pago:", ["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"])

    # BLOQUE LEGAL EXACTO
    st.markdown(f"""
        <div style="font-size: 0.9rem; text-align: justify; border: 1px solid #ccc; padding: 15px; color: black; background: #fff;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
        a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br><br>
        Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato.<br><br>
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representantes del contingente de referencia.<br>
        <b>NOTA:</b> de no marcarse ningun plan de pago, su chequera se emitira como <b>PLAN 1</b>.
        </div>
    """, unsafe_allow_html=True)

    # ESPACIO DE FIRMAS
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Firma</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Aclaración y DNI</p>", unsafe_allow_html=True)

    # --- EL BOTÓN DEFINITIVO ---
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Este botón ejecuta el comando de impresión del sistema
    if st.button("💾 GENERAR PDF / DESCARGAR FORMULARIO"):
        st.write('<script>window.print();</script>', unsafe_allow_html=True)
