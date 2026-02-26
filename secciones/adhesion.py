import streamlit as st
from datetime import datetime

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# Versión: Botón de Impresión Corregido (Fuera del Form)
# =================================================================

def render_adhesion(logo_url):
    # CSS para que la ficha salga perfecta en papel
    st.markdown("""
        <style>
        @media print {
            header, [data-testid="stSidebar"], .stButton, .no-print, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container {
                padding: 0 !important;
                margin: 0 !important;
            }
            body { color: black !important; background: white !important; }
            div[data-testid="stForm"] { border: none !important; padding: 0 !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera
    st.image(logo_url, width=150)
    st.markdown("<h2 style='text-align: center; color: black; margin-bottom: 0;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    # El formulario para que el cliente complete
    with st.form("ficha_adhesion_final"):
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.date_input("Fecha", datetime.now())
        with col2: st.text_input("Cliente N°")
        with col3: st.text_input("Contrato")
        with col4: st.text_input("% L.O.")

        c_ins, c_anio = st.columns(2)
        with c_ins: st.text_input("Colegio / Instituto")
        with c_anio: st.text_input("Año y División")

        st.markdown("---")
        st.write("**DATOS DEL ALUMNO / PASAJERO**")
        
        ca1, ca2 = st.columns(2)
        with ca1:
            st.text_input("Apellido")
            st.text_input("D.N.I. Nº")
            st.date_input("Fecha de Nacimiento", min_value=datetime(2000,1,1))
        with ca2:
            st.text_input("Nombres")
            st.date_input("Vencimiento D.N.I.") 
            st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        cd1, cd2, cd3 = st.columns([2, 1, 1])
        with cd1: st.text_input("Domicilio")
        with cd2: st.text_input("C.P.")
        with cd3: st.text_input("Localidad")

        st.markdown("---")
        st.write("**DATOS DE LOS PADRES / TUTORES**")
        ct1, ct2 = st.columns(2)
        with ct1: 
            st.text_input("Madre / Padre / Tutor (1)")
            st.text_input("D.N.I. (1)")
        with ct2: 
            st.text_input("Madre / Padre / Tutor (2)")
            st.text_input("D.N.I. (2)")
        
        st.text_input("E-mail de contacto:")
        st.text_area("Observaciones:", label_visibility="collapsed")

        st.markdown("---")
        plan_sel = st.pills("Plan de Pago:", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"])
        
        st.markdown(f"""
            <div style="font-size: 0.9rem; text-align: justify; border: 1px solid #ccc; padding: 15px; background-color: #fcfcfc; color: black;">
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
        with fcol1:
            st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
            st.caption("Firma del Padre/Madre/Tutor")
        with fcol2:
            st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
            st.caption("Aclaración y D.N.I.")

        # Este botón "valida" el formulario para que los datos queden fijos
        enviar = st.form_submit_button("✅ CONFIRMAR DATOS")

    # --- EL BOTÓN DE IMPRESIÓN AHORA ESTÁ AQUÍ (FUERA DEL FORM) ---
    st.divider()
    if st.button("🖨️ IMPRIMIR SOLICITUD COMPLETADA", type="primary", use_container_width=True):
        st.write('<script>window.print();</script>', unsafe_allow_html=True)
        st.balloons()
