import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

def render_adhesion(logo_url):
    # CSS de Máxima Compresión para Carilla Única
    st.markdown("""
        <style>
        /* Ajustes para la vista Web y eliminación de márgenes superiores */
        .main .block-container { 
            padding-top: 0rem !important; 
            padding-bottom: 0rem !important; 
        }
        [data-testid="stHeader"] { display: none !important; }
        
        @media print {
            @page {
                size: A4;
                margin: 0.5cm; /* Margen mínimo de seguridad */
            }
            /* ESCALADO DINÁMICO */
            html, body {
                zoom: 90%; 
            }
            header, [data-testid="stSidebar"], .no-print, .stButton, footer {
                display: none !important;
            }
            /* Eliminar espacios vacíos de Streamlit en PDF */
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            
            h2 { font-size: 1.3rem !important; margin-top: -10px !important; margin-bottom: 2px !important; }
            p, div, label { font-size: 9pt !important; line-height: 1.0 !important; }
            
            /* Inputs ultra compactos para el PDF */
            input { border: none !important; font-weight: bold !important; height: auto !important; padding: 0 !important; }
            hr { margin: 5px 0 !important; }
            .stTextArea textarea { height: 40px !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera Ultra Compacta
    st.image(logo_url, width=90)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: -20px;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold; margin-top: -5px;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    # --- DATOS DE CONTROL ---
    col1, col2, col3, col4 = st.columns(4)
    col1.date_input("Fecha", datetime.now())
    col2.text_input("Cliente N°")
    col3.text_input("Contrato")
    col4.text_input("% L.O.")

    c_ins, c_anio = st.columns([2, 1])
    c_ins.text_input("Colegio / Instituto")
    c_anio.text_input("Año y División")

    st.markdown("---")
    
    # --- DATOS ALUMNO ---
    st.write("**DATOS DEL ALUMNO / PASAJERO**")
    ca1, ca2 = st.columns(2)
    ca1.text_input("Apellido")
    ca2.text_input("Nombres")
    
    cdni1, cdni2, cdni3 = st.columns(3)
    cdni1.text_input("D.N.I. Nº")
    cdni2.date_input("Vto. D.N.I.") 
    cdni3.date_input("Nacimiento", min_value=datetime(1990,1,1))
    
    st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

    cd1, cd2, cd3 = st.columns([2, 1, 1])
    cd1.text_input("Domicilio")
    cd2.text_input("C.P.")
    cd3.text_input("Localidad")

    st.markdown("---")
    
    # --- DATOS PADRES ---
    st.write("**DATOS DE LOS PADRES / TUTORES**")
    ct1, ct2 = st.columns(2)
    ct1.text_input("Responsable 1 (Nombre y DNI)")
    ct2.text_input("Responsable 2 (Nombre y DNI)")
    
    email_col, obs_col = st.columns([1, 1])
    email_col.text_input("E-mail de contacto")
    obs_col.text_input("Observaciones")

    st.markdown("---")
    
    # --- PLANES ---
    st.write("**Plan de Pago:**")
    plan_sel = st.pills("Planes", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], default="PLAN 1", label_visibility="collapsed")

    # TEXTO LEGAL (Fuente pequeña para ganar espacio)
    st.markdown(f"""
        <div style="font-size: 0.75rem; text-align: justify; border: 1px solid #ccc; padding: 8px; color: black; background: #f9f9f9; line-height: 1.0;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
        a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br>
        Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato. 
        Ademas declaro conocer las condiciones del contrato suscripto por mi y/u otros representantes. 
        <b>NOTA:</b> de no marcarse plan, se emitira como <b>PLAN 1</b>.
        </div>
    """, unsafe_allow_html=True)

    # FIRMAS
    st.markdown("<br>", unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:8pt;'>Firma del Responsable</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:8pt;'>Aclaración y D.N.I.</p>", unsafe_allow_html=True)

    # BOTÓN DE IMPRESIÓN
    st.markdown("<div class='no-print'><br></div>", unsafe_allow_html=True)
    components.html(
        """
        <html>
            <body>
                <button style="background-color: #2E7D32; color: white; padding: 12px; border: none; border-radius: 10px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold;" 
                onclick="window.parent.print()">🖨️ GENERAR PDF (UNA SOLA CARILLA)</button>
            </body>
        </html>
        """,
        height=80,
    )
