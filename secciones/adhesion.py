import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

def render_adhesion(logo_url):
    # Estilos CSS
    st.markdown("""
        <style>
        .main { background-color: white !important; }
        .main .block-container { 
            padding-top: 2rem !important; 
            color: black !important;
        }
        label p {
            color: black !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
        }
        input {
            color: black !important;
            background-color: #f8f9fa !important;
            border: 1px solid #ced4da !important;
        }
        @media print {
            .no-print, [data-testid="stHeader"], [data-testid="stSidebar"], .stButton { display: none !important; }
            input { border: none !important; border-bottom: 1px solid #000 !important; background: transparent !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera
    c_logo, c_tit = st.columns([1, 4])
    with c_logo:
        st.image(logo_url, width=80)
    with c_tit:
        st.markdown("<h1 style='color: black; margin: 0;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; color: black;'>Serrano Turismo - Ficha de Adhesión</p>", unsafe_allow_html=True)

    st.markdown("---")

    # Datos de Control
    st.markdown("### 📋 DATOS DE CONTROL")
    c1, c2, c3, c4 = st.columns(4)
    c1.date_input("Fecha de Solicitud", datetime.now())
    c2.text_input("N° de Cliente", key="ctrl_nclie")
    c3.text_input("N° de Contrato", key="ctrl_contr")
    c4.text_input("% Localidad", key="ctrl_loc")

    inst1, inst2 = st.columns([2, 1])
    inst1.text_input("Establecimiento Educativo", key="ctrl_inst")
    inst2.text_input("Año / División", key="ctrl_anio")

    st.markdown("---")
    
    # Datos del Pasajero
    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap1, nom1 = st.columns(2)
    ap1.text_input("Apellido/s", key="pas_ape")
    nom1.text_input("Nombre/s", key="pas_nom")
    
    cd1, cd2, cd3 = st.columns([1, 1, 1])
    cd1.text_input("DNI / CUIL", key="pas_dni")
    cd2.text_input("Fecha de Vencimiento DNI", key="pas_vence") 
    cd3.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1), key="pas_nace")
    
    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True, key="pas_sexo")

    dom1, dom2 = st.columns([2, 1])
    dom1.text_input("Domicilio Particular", key="pas_dom")
    dom2.text_input("Localidad / CP", key="pas_cp")

    st.markdown("---")
    
    # Datos de Tutores
    st.markdown("### 👥 DATOS DE LOS PADRES / TUTORES")
    
    st.markdown("**DATOS TUTOR 1**")
    t1_1, t1_2, t1_3 = st.columns([2, 1, 1])
    t1_1.text_input("Nombre y Apellido", key="t1_nom_def")
    t1_2.text_input("CUIL", key="t1_cuil_def")
    t1_3.text_input("Teléfono de Contacto", key="t1_tel_def")
    
    st.markdown("**DATOS TUTOR 2**")
    t2_1, t2_2, t2_3 = st.columns([2, 1, 1])
    t2_1.text_input("Nombre y Apellido ", key="t2_nom_def")
    t2_2.text_input("CUIL ", key="t2_cuil_def")
    t2_3.text_input("Teléfono de Contacto ", key="t2_tel_def")
    
    st.text_input("Correo Electrónico (E-mail):", key="tut_email_def")

    st.markdown("---")

    # Selección de Plan
    st.markdown("### 💰 SELECCIÓN DE PLAN")
    st.pills("Seleccione su Plan de Pago:", 
             options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTRO"], 
             default="PLAN 4", key="plan_sel_def")

    # Texto Legal exacto solicitado
    st.markdown("""
        <div style="font-size: 0.75rem; text-align: justify; border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9; color: black; border-radius: 5px; line-height: 1.3;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente denominado.<br><br>
        Los planes al contado deberan abonarse dentro de los 30 dias de firmado el contrato.<br><br>
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representante del contingente de referencia.<br><br>
        <b>NOTA: De no marcar ningun plan de pago, su chequera se emitira como PLAN CUOTAS (PLAN 4).</b>
        </div>
    """, unsafe_allow_html=True)

    # Firmas
    st.markdown('<div style="margin-top: 30px;">', unsafe_allow_html=True)
    f1, f2 = st.columns(2)
    f1.markdown("<hr style='border:0.5px solid black;'><p style='text-align:center; font-size:9pt; color:black;'>Firma Responsable</p>", unsafe_allow_html=True)
    f2.markdown("<hr style='border:0.5px solid black;'><p style='text-align:center; font-size:9pt; color:black;'>Aclaración y N° de C.U.I.L.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Botón de impresión
    components.html(
        """
        <html><body>
            <button style="background-color: #2E7D32; color: white; padding: 15px; border: none; border-radius: 10px; cursor: pointer; width: 100%; font-size: 18px; font-weight: bold;" 
            onclick="window.parent.print()">🖨️ GENERAR COMPROBANTE PDF</button>
        </body></html>
        """,
        height=100,
    )
