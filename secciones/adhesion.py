import streamlit as st
from datetime import datetime

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN FINAL - NO MODIFICAR ESTRUCTURA
# =================================================================

def render_adhesion(logo_url):
    # CSS para ocultar la web al imprimir y que el PDF salga limpio
    st.markdown("""
        <style>
        /* Estilos en pantalla para el botón verde */
        .boton-pdf {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background-color: #2E7D32 !important;
            color: white !important;
            padding: 15px 25px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.2rem;
            width: 100%;
            border: none;
            cursor: pointer;
        }
        
        @media print {
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container { padding: 1cm !important; margin: 0 !important; }
            body { color: black !important; background: white !important; }
            /* Que los inputs se vean como texto negrita en el PDF */
            input, textarea { 
                border: none !important; 
                font-weight: bold !important; 
                background: transparent !important;
                color: black !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera
    st.image(logo_url, width=150)
    st.markdown("<h2 style='text-align: center; color: black; margin-bottom: 0;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    # --- CAMPOS DE ENTRADA (Sin Formulario para evitar bloqueos de script) ---
    col1, col2, col3, col4 = st.columns(4)
    col1.date_input("Fecha", datetime.now())
    col2.text_input("Cliente N°")
    col3.text_input("Contrato")
    col4.text_input("% L.O.")

    c_ins, c_anio = st.columns(2)
    c_ins.text_input("Colegio / Instituto")
    c_anio.text_input("Año y División")

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
    st.text_area("Observaciones:")

    st.markdown("---")
    
    # Planes con botones (Pills)
    st.write("**Seleccione su Plan de Pago:**")
    plan_sel = st.pills(
        "Planes", 
        options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], 
        default="PLAN 1", 
        label_visibility="collapsed"
    )
    if plan_sel == "OTROS":
        st.text_input("Especifique plan:")

    # TEXTO LEGAL
    st.markdown(f"""
        <div style="font-size: 0.9rem; text-align: justify; border: 1px solid #ccc; padding: 15px; background-color: #f9f9f9; color: black; margin-top: 10px;">
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
    fcol1.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Firma del Padre/Madre/Tutor</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Aclaración y D.N.I.</p>", unsafe_allow_html=True)

    # --- BOTÓN DE IMPRESIÓN / GENERAR PDF ---
    st.divider()
    
    # Usamos un botón de Streamlit con una inyección directa de JS
    if st.button("💾 GENERAR PDF / IMPRIMIR SOLICITUD", type="primary"):
        st.markdown("""
            <script>
                window.print();
            </script>
        """, unsafe_allow_html=True)
