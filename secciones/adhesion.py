import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

def render_adhesion(logo_url):
    # CSS Final: Protege el diseño en la web y ajusta escala solo al imprimir
    st.markdown("""
        <style>
        /* Vista Web Normal */
        .main .block-container { padding-top: 2rem; }
        
        @media print {
            /* Forzar carilla única sin deformar */
            @page {
                size: A4;
                margin: 0.8cm;
            }
            html, body {
                zoom: 94%; /* Ajuste leve para asegurar que entren las firmas */
            }
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            
            /* Inputs limpios para el PDF */
            input, textarea { 
                border: none !important; 
                background: transparent !important; 
                font-weight: bold !important;
                color: black !important;
            }
            [data-testid="stVerticalBlock"] > div { margin-top: -5px !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera Institucional (Logo original)
    st.image(logo_url, width=150)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: -10px;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    # --- DATOS DE CONTROL (RESTAURADOS) ---
    col1, col2, col3, col4 = st.columns(4)
    col1.date_input("Fecha", datetime.now())
    col2.text_input("Cliente N°")
    col3.text_input("Contrato")
    col4.text_input("% L.O.")

    c_ins, c_anio = st.columns(2)
    c_ins.text_input("Colegio / Instituto")
    c_anio.text_input("Año y División")

    st.markdown("---")
    
    # --- DATOS DEL ALUMNO (RESTAURADOS) ---
    st.write("**DATOS DEL ALUMNO / PASAJERO**")
    ca1, ca2 = st.columns(2)
    ca1.text_input("Apellido")
    ca2.text_input("Nombres")
    
    col_d1, col_d2 = st.columns(2)
    col_d1.text_input("D.N.I. Nº")
    col_d2.date_input("Vencimiento D.N.I.") # Restaurado
    
    col_f1, col_f2 = st.columns(2)
    col_f1.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
    col_f2.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

    cd1, cd2, cd3 = st.columns([2, 1, 1])
    cd1.text_input("Domicilio")
    cd2.text_input("C.P.")
    cd3.text_input("Localidad")

    st.markdown("---")
    
    # --- DATOS DE LOS PADRES (RESTAURADOS) ---
    st.write("**DATOS DE LOS PADRES / TUTORES**")
    ct1, ct2 = st.columns(2)
    ct1.text_input("Madre / Padre / Tutor (1)")
    ct1.text_input("D.N.I. (1)")
    ct2.text_input("Madre / Padre / Tutor (2)")
    ct2.text_input("D.N.I. (2)")
    
    st.text_input("E-mail de contacto:")
    st.text_area("Observaciones:") # Restaurado amplio

    st.markdown("---")
    
    # --- PLANES COMO BOTONES (RESTAURADOS) ---
    st.write("**Seleccione su Plan de Pago:**")
    plan_sel = st.pills(
        "Planes", 
        options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], 
        default="PLAN 1", 
        label_visibility="collapsed"
    )
    if plan_sel == "OTROS":
        st.text_input("Especifique plan:")

    # --- TEXTO LEGAL EXACTO (RESTAURADO) ---
    st.markdown(f"""
        <div style="font-size: 0.9rem; text-align: justify; border: 1px solid #ccc; padding: 15px; background-color: #f9f9f9; color: black; margin-top: 10px;">
        Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
        a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br><br>
        Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato.<br><br>
        Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representantes del contingente de referencia.<br>
        <b>NOTA:</b> de no marcarse ningun plan de pago, su chequera se emitira como <b>PLAN 1</b>.
        </div>
    """, unsafe_allow_html=True)

    # --- FIRMAS (RESTAURADAS) ---
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Firma del Padre/Madre/Tutor</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Aclaración y D.N.I.</p>", unsafe_allow_html=True)

    # --- BOTÓN DE IMPRESIÓN (RESTAURADO E INFALIBLE) ---
    st.divider()
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
