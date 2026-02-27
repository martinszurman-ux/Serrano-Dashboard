import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

def render_adhesion(logo_url):
    # CSS Optimizado para impresión en una sola carilla A4
    st.markdown("""
        <style>
        .main { background-color: white !important; }
        .main .block-container { 
            padding-top: 1.5rem !important; 
            padding-bottom: 0rem !important;
            color: black !important;
        }
        label p {
            color: black !important;
            font-weight: 700 !important;
            font-size: 0.85rem !important;
            margin-bottom: 2px !important;
        }
        input {
            color: black !important;
            background-color: #f8f9fa !important;
            border: 1px solid #ced4da !important;
            height: 30px !important; /* Achicamos altura de inputs */
        }
        
        /* AJUSTES ESPECÍFICOS PARA IMPRESIÓN */
        @media print {
            @page { 
                size: A4; 
                margin: 0.5cm; /* Márgenes mínimos para ganar espacio */
            }
            html, body { 
                zoom: 82%; /* Reducimos escala global para asegurar 1 carilla */
            }
            .no-print, [data-testid="stHeader"], [data-testid="stSidebar"], .stButton { 
                display: none !important; 
            }
            .main .block-container { 
                padding: 0 !important; 
                margin: 0 !important; 
            }
            /* Convertimos inputs en líneas para ahorrar tinta y espacio */
            input { 
                border: none !important; 
                border-bottom: 1px solid #000 !important; 
                background: transparent !important; 
            }
            hr { margin: 5px 0 !important; }
            h1 { font-size: 1.5rem !important; }
            h3 { font-size: 1.1rem !important; margin-top: 5px !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera - Reducida en margen
    c_logo, c_tit = st.columns([1, 5])
    with c_logo:
        st.image(logo_url, width=65)
    with c_tit:
        st.markdown("<h1 style='color: black; margin: 0; padding: 0;'>SOLICITUD DE INGRESO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-weight: bold; color: black; margin-top: -5px;'>Serrano Turismo - Ficha de Adhesión</p>", unsafe_allow_html=True)

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)

    # Datos de Control
    st.markdown("### 📋 DATOS DE CONTROL")
    c1, c2, c3, c4 = st.columns(4)
    c1.date_input("Fecha de Solicitud", datetime.now())
    c2.text_input("N° de Cliente", key="ctrl_nclie_f")
    c3.text_input("N° de Contrato", key="ctrl_contr_f")
    c4.text_input("% Localidad", key="ctrl_loc_f")

    inst1, inst2 = st.columns([2, 1])
    inst1.text_input("Establecimiento Educativo", key="ctrl_inst_f")
    inst2.text_input("Año / División", key="ctrl_anio_f")

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)
    
    # Datos del Pasajero
    st.markdown("### 🧒 DATOS DEL PASAJERO")
    ap1, nom1 = st.columns(2)
    ap1.text_input("Apellido/s", key="pas_ape_f")
    nom1.text_input("Nombre/s", key="pas_nom_f")
    
    cd1, cd2, cd3 = st.columns([1, 1, 1])
    cd1.text_input("DNI / CUIL", key="pas_dni_f")
    cd2.text_input("Fecha de Vencimiento DNI", key="pas_vence_f") 
    cd3.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1), key="pas_nace_f")
    
    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True, key="pas_sexo_f")

    dom1, dom2 = st.columns([2, 1])
    dom1.text_input("Domicilio Particular", key="pas_dom_f")
    dom2.text_input("Localidad / CP", key="pas_cp_f")

    st.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)
    
    # Datos de Tutores
    st.markdown("### 👥 DATOS DE LOS PADRES / TUTORES")
    
    st.markdown("**DATOS TUTOR 1**")
    t1_1, t1_2, t1_3 = st.columns([2, 1, 1])
    t1_1.text_input("Nombre y Apellido", key="t1_nom_f")
    t1_2.text_input("CUIL", key="t1_cuil_f")
    t1_3.text_input("Teléfono de Contacto", key="t1_tel_f")
    
    st.markdown("**DATOS TUTOR 2**")
    t2_1, t2_2, t2_3 = st.columns([2, 1, 1])
    t2_1.text_input("Nombre y Apellido ", key="t2_nom_f")
    t2_2.text_input("CUIL ", key="t2_cuil_f")
    t2_3.text_input("Teléfono de Contacto ", key="t2_tel_f")
    
    st.text_input("Correo Electrónico (E-mail):", key="tut_email_f")

    # Selección de Plan
    st.pills("Seleccione su Plan de Pago:", 
             options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTRO"], 
             default="PLAN 4", key="plan_sel_f")

    # Texto Legal
    st.markdown(f"""
        <div style="font-size: 0.68rem; text-align: justify; border: 1px solid #ccc; padding: 8px; background-color: #f9f9f9; color: black; border-radius: 5px; line-height: 1.1;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente denominado.<br>
        Los planes al contado deberan abonarse dentro de los 30 dias de firmado el contrato.
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representante del contingente de referencia.<br>
        <b>NOTA: De
