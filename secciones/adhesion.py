import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

def render_adhesion(logo_url):
    # CSS para una carilla única sin deformar el contenido
    st.markdown("""
        <style>
        /* Optimización de la vista Web */
        .main .block-container { 
            padding-top: 1rem !important; 
            padding-bottom: 0rem !important; 
        }
        
        @media print {
            @page {
                size: A4;
                margin: 1cm; /* Margen estándar para que no se corte nada */
            }
            /* ESCALADO NATURAL */
            html, body {
                zoom: 95%; /* Un toque leve para asegurar el cierre de la hoja */
            }
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            
            /* Ajuste de tipografía para legibilidad */
            h2 { font-size: 1.6rem !important; margin-top: 0 !important; margin-bottom: 10px !important; }
            p, div, label { font-size: 10pt !important; color: black !important; }
            
            /* Quitar el sombreado gris de los inputs en el PDF */
            input { 
                border: none !important; 
                background: transparent !important; 
                font-weight: bold !important;
                color: black !important;
            }
            /* Reducir espacio entre líneas de Streamlit */
            [data-testid="stVerticalBlock"] > div { margin-top: -10px !important; }
            hr { margin: 10px 0 !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera Institucional
    st.image(logo_url, width=120)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: -10px;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Pasajero</p>", unsafe_allow_html=True)

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
    st.write("**DATOS DEL PASAJERO**")
    ca1, ca2 = st.columns(2)
    ca1.text_input("Apellido")
    ca2.text_input("Nombres")
    
    # Agrupamos DNI y Nacimiento para ganar espacio vertical
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
    st.write("**DATOS DE RESPONSABLES / TUTORES**")
    ct1, ct2 = st.columns(2)
    ct1.text_input("Responsable 1 (Nombre y DNI)")
    ct2.text_input("Responsable 2 (Nombre y DNI)")
    
    c_mail, c_obs = st.columns([1, 1])
    c_mail.text_input("E-mail")
    c_obs.text_input("Observaciones")

    st.markdown("---")
    
    # --- PLANES ---
    st.write("**Plan de Pago Elegido:**")
    st.pills("Planes", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], default="PLAN 1", label_visibility="collapsed")

    # TEXTO LEGAL (Legible pero compacto)
    st.markdown(f"""
        <div style="font-size: 0.85rem; text-align: justify; border: 1px solid #ccc; padding: 12px; color: black; background: #fdfdfd; line-height: 1.2; margin-top: 10px;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
        a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br><br>
        Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato. 
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto. 
        <b>NOTA:</b> de no marcarse ningun plan de pago, su chequera se emitira como <b>PLAN 1</b>.
        </div>
    """, unsafe_allow_html=True)

    # FIRMAS
    st.markdown("<br><br>", unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("<hr style='border:1px solid black; margin-bottom:0;'><p style='text-align:center;'>Firma del Responsable</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:1px solid black; margin-bottom:0;'><p style='text-align:center;'>Aclaración y D.N.I.</p>", unsafe_allow_html=True)

    # BOTÓN DE IMPRESIÓN
    st.markdown("<div class='no-print'><br></div>", unsafe_allow_html=True)
    components.html(
        """
        <html>
            <body>
                <button style="background-color: #2E7D32; color: white; padding: 15px; border: none; border-radius: 10px; cursor: pointer; width: 100%; font-size: 18px; font-weight: bold;" 
                onclick="window.parent.print()">🖨️ GENERAR PDF / IMPRIMIR</button>
            </body>
        </html>
        """,
        height=100,
    )
