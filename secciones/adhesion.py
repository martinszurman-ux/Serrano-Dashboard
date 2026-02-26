import streamlit as st
from datetime import datetime

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# FUNCIÓN: Ficha con persistencia y botón de impresión garantizado
# =================================================================

def render_adhesion(logo_url):
    # 1. Estilos CSS para la web y para la impresora
    st.markdown("""
        <style>
        /* Estilos en pantalla */
        .instruccion-final {
            background-color: #e3f2fd;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #1E3A8A;
            margin: 20px 0;
        }
        
        /* Estilos de Impresión (PDF) */
        @media print {
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            body { color: black !important; background: white !important; }
            div[data-testid="stForm"] { border: none !important; padding: 0 !important; }
            input { border: none !important; font-weight: bold !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera
    st.image(logo_url, width=150)
    st.markdown("<h2 style='text-align: center; color: black;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)

    # 2. Formulario Principal
    with st.form("ficha_definitiva"):
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
            st.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
        with ca2:
            st.text_input("Nombres")
            st.date_input("Vencimiento D.N.I.") 
            st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

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
        st.text_area("Observaciones:")

        st.markdown("---")
        st.write("**PLAN DE PAGO ELEGIDO**")
        plan_sel = st.pills("Seleccione:", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], label_visibility="collapsed")
        
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

        # Botón para "congelar" los datos en la pantalla antes de imprimir
        st.form_submit_button("✅ 1. CONFIRMAR DATOS")

    # 3. Botón de Impresión PERMANENTE (Fuera del formulario)
    st.markdown("""
        <div class="instruccion-final">
            <strong>PASO FINAL:</strong> Una vez confirmados los datos arriba, presione el botón verde para descargar su PDF.
        </div>
    """, unsafe_allow_html=True)

    if st.button("🖨️ 2. DESCARGAR / IMPRIMIR SOLICITUD", type="primary"):
        st.write('<script>window.print();</script>', unsafe_allow_html=True)
