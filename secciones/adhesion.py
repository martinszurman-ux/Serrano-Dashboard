import streamlit as st
from datetime import datetime

def render_adhesion(logo_url):
    # CSS específico para que la impresión sea una ficha limpia
    st.markdown("""
        <style>
        @media print {
            /* Ocultar elementos de la web */
            header, [data-testid="stSidebar"], .stButton, .no-print {
                display: none !important;
            }
            /* Ajustar el contenedor para que ocupe toda la hoja */
            .main .block-container {
                padding: 0 !important;
                margin: 0 !important;
            }
            /* Asegurar que el texto sea negro y legible */
            body {
                color: black !important;
                background: white !important;
            }
            /* Forzar que los expanders o bordes se vean prolijos */
            div[data-testid="stForm"] {
                border: none !important;
                padding: 0 !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Contenido de la Solicitud
    st.image(logo_url, width=150)
    st.markdown("<h2 style='text-align: center; color: black;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    with st.form("form_impresion_adhesion"):
        # Seccion de Datos de Control
        col1, col2, col3, col4 = st.columns(4)
        with col1: fecha = st.date_input("Fecha", datetime.now())
        with col2: cliente_n = st.text_input("Cliente N°")
        with col3: contrato = st.text_input("Contrato")
        with col4: lo = st.text_input("% L.O.")

        c_ins, c_anio = st.columns(2)
        with c_ins: colegio = st.text_input("Colegio / Instituto")
        with c_anio: anio_div = st.text_input("Año y División")

        st.markdown("---")
        st.write("**DATOS DEL ALUMNO**")
        
        ca1, ca2 = st.columns(2)
        with ca1:
            ape = st.text_input("Apellido")
            dni = st.text_input("D.N.I. Nº")
            fnac = st.date_input("Fecha de Nacimiento", min_value=datetime(2000,1,1))
        with ca2:
            nom = st.text_input("Nombres")
            nac = st.text_input("Nacionalidad", value="Argentina")
            sex = st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        cd1, cd2, cd3 = st.columns([2, 1, 1])
        with cd1: dom = st.text_input("Domicilio")
        with cd2: cp = st.text_input("C.P.")
        with cd3: loc = st.text_input("Localidad")

        st.markdown("---")
        st.write("**DATOS DE LOS PADRES / TUTORES**")
        ct1, ct2 = st.columns(2)
        with ct1: 
            p1 = st.text_input("Madre / Padre / Tutor (1)")
            d1 = st.text_input("D.N.I. (1)")
        with ct2: 
            p2 = st.text_input("Madre / Padre / Tutor (2)")
            d2 = st.text_input("D.N.I. (2)")
        
        email = st.text_input("E-mail de contacto:")
        
        st.markdown("#### OBSERVACIONES")
        obs = st.text_area("Aclaraciones:", label_visibility="collapsed")

        st.markdown("---")
        # Selector de Plan
        plan_pago = st.pills("Seleccione Plan:", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"])
        
        # Bloque de Texto Legal
        st.markdown(f"""
            <div style="font-size: 0.9rem; text-align: justify; border: 1px solid #ccc; padding: 10px;">
            Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
            a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br><br>
            Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato.<br><br>
            Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representantes del contingente de referencia.<br>
            <b>NOTA:</b> de no marcarse ningun plan de pago, su chequera se emitira como <b>PLAN 1</b>.
            </div>
        """, unsafe_allow_html=True)

        # Espacio para Firmas
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        fcol1, fcol2 = st.columns(2)
        with fcol1:
            st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
            st.caption("Firma del Padre/Madre/Tutor")
        with fcol2:
            st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
            st.caption("Aclaración y D.N.I.")

        # Botón para procesar los datos dentro del formulario (no imprime)
        st.form_submit_button("Confirmar Datos para Impresión")

    # BOTÓN DE IMPRESIÓN REAL
    st.button("🖨️ IMPRIMIR SOLICITUD COMPLETADA", on_click=lambda: st.write('<script>window.print();</script>', unsafe_allow_html=True))
