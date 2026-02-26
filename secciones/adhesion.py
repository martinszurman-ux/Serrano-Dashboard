import streamlit as st
from datetime import datetime

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: Triple Seguridad (Estado + JS Directo + Persistencia)
# =================================================================

def render_adhesion(logo_url):
    # 1. CSS de Alta Fidelidad y Control de Impresión
    st.markdown("""
        <style>
        /* Estilo del botón de impresión en la web */
        .btn-imprimir {
            display: block;
            width: 100%;
            padding: 15px;
            background-color: #2E7D32 !important;
            color: white !important;
            text-align: center;
            font-weight: bold;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 20px;
            text-decoration: none;
            font-size: 1.2rem;
            border: none;
        }
        
        @media print {
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            body { color: black !important; background: white !important; }
            div[data-testid="stForm"] { border: none !important; padding: 0 !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. Inicialización del Estado (Para que los botones no desaparezcan)
    if 'form_confirmado' not in st.session_state:
        st.session_state.form_confirmado = False

    # Cabecera
    st.image(logo_url, width=150)
    st.markdown("<h2 style='text-align: center;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)

    # 3. Formulario de Carga
    with st.form("form_serrano_final"):
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.date_input("Fecha", datetime.now())
        with col2: st.text_input("Cliente N°")
        with col3: st.text_input("Contrato")
        with col4: st.text_input("% L.O.")

        c_ins, c_anio = st.columns(2)
        with c_ins: st.text_input("Colegio / Instituto")
        with c_anio: st.text_input("Año y División")

        st.markdown("---")
        st.write("**DATOS DEL ALUMNO**")
        ca1, ca2 = st.columns(2)
        with ca1:
            st.text_input("Apellido")
            st.text_input("D.N.I. Nº")
            st.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
        with ca2:
            st.text_input("Nombres")
            st.date_input("Vencimiento D.N.I.") 
            st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        st.markdown("---")
        st.write("**DATOS DE LOS PADRES**")
        ct1, ct2 = st.columns(2)
        with ct1: 
            st.text_input("Madre / Padre / Tutor (1)")
            st.text_input("D.N.I. (1)")
        with ct2: 
            st.text_input("Madre / Padre / Tutor (2)")
            st.text_input("D.N.I. (2)")
        
        st.text_input("E-mail de contacto")
        st.text_area("Observaciones")

        st.markdown("---")
        st.pills("Plan de Pago:", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"])
        
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

        # Botón de Confirmación
        if st.form_submit_button("✅ 1. CONFIRMAR DATOS"):
            st.session_state.form_confirmado = True

    # 4. Botón de Impresión (Solo se ve si confirmaron los datos)
    if st.session_state.form_confirmado:
        st.success("✅ Datos anclados. Presione el botón de abajo para imprimir o guardar como PDF.")
        
        # Botón con JavaScript inyectado directamente en el evento onClick
        if st.button("🖨️ 2. CLIC AQUÍ PARA IMPRIMIR / DESCARGAR PDF"):
            st.markdown("""
                <script>
                    window.print();
                </script>
            """, unsafe_allow_html=True)
