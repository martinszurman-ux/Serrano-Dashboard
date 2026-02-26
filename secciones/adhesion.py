import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

def render_adhesion(logo_url):
    # CSS de Máxima Compresión y Eliminación de Espacios
    st.markdown("""
        <style>
        /* Vista Web: Eliminar márgenes superiores */
        .main .block-container { 
            padding-top: 0rem !important; 
            padding-bottom: 0rem !important; 
        }
        [data-testid="stHeader"] { display: none !important; }
        
        @media print {
            @page {
                size: A4;
                margin: 0.3cm; /* Margen mínimo absoluto */
            }
            /* ESCALADO FUERTE AL 85% */
            html, body {
                zoom: 85%; 
                height: 99%;
                overflow: hidden;
            }
            header, [data-testid="stSidebar"], .no-print, .stButton, footer {
                display: none !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            
            /* Compactar Títulos y Textos */
            h2 { font-size: 1.2rem !important; margin-top: -15px !important; margin-bottom: 0px !important; }
            p, div, label { font-size: 8.5pt !important; line-height: 0.9 !important; }
            
            /* Eliminar espacios entre widgets de Streamlit */
            [data-testid="stVerticalBlock"] > div { margin-top: -8px !important; }
            
            /* Inputs ultra planos */
            input { border: none !important; font-weight: bold !important; height: auto !important; padding: 0 !important; }
            hr { margin: 3px 0 !important; }
            .stTextArea textarea { height: 35px !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera Mínima
    st.image(logo_url, width=80)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: -25px;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold; margin-top: -5px;'>Ficha del Pasajero</p>", unsafe_allow_html=True)

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
    st.write("**DATOS DE RESPONSABLES**")
    ct1, ct2 = st.columns(2)
    ct1.text_input("Responsable 1 (Nombre y DNI)")
    ct2.text_input("Responsable 2 (Nombre y DNI)")
    
    email_col, obs_col = st.columns([1, 1])
    email_col.text_input("E-mail")
    obs_col.text_input("Observaciones")

    st.markdown("---")
    
    # --- PLANES ---
    st.write("**Plan de Pago:**")
    st.pills("Planes", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], default="PLAN 1", label_visibility="collapsed")

    # TEXTO LEGAL (Micro-fuente)
    st.markdown(f"""
        <div style="font-size: 0.7rem; text-align: justify; border: 1px solid #ccc; padding: 5px; color: black; background: #f9f9f9; line-height: 1.0;">
        Declaro bajo juramento que los datos volcados son exactos y acepto, para Serrano Turismo, el plan de pagos de la reserva. 
        Los planes contado vencen a los 30 días. Conozco las condiciones del contrato. 
        <b>NOTA:</b> De no marcarse plan, se emitirá como <b>PLAN 1</b>.
        </div>
    """, unsafe_allow_html=True)

    # FIRMAS (Muy pegadas al texto legal)
    st.markdown("<br>", unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt;'>Firma del Responsable</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:0.5px solid black; margin-bottom:0;'><p style='text-align:center; font-size:7pt;'>Aclaración y D.N.I.</p>", unsafe_allow_html=True)

    # BOTÓN DE IMPRESIÓN
    st.markdown("<div class='no-print'><br></div>", unsafe_allow_html=True)
    components.html(
        """
        <html>
            <body>
                <button style="background-color: #2E7D32; color: white; padding: 10px; border: none; border-radius: 10px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold;" 
                onclick="window.parent.print()">🖨️ GENERAR PDF (CARILLA ÚNICA)</button>
            </body>
        </html>
        """,
        height=70,
    )
