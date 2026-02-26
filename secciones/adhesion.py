import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: Botón de Impresión por Componente HTML (Infalible)
# =================================================================

def render_adhesion(logo_url):
    # 1. CSS para que la ficha salga perfecta en el PDF
    st.markdown("""
        <style>
        @media print {
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            body { color: black !important; background: white !important; }
            input, textarea { border: none !important; font-weight: bold !important; background: transparent !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabecera
    st.image(logo_url, width=150)
    st.markdown("<h2 style='text-align: center; color: black;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)

    # --- CAMPOS DE ENTRADA ---
    col1, col2, col3, col4 = st.columns(4)
    col1.date_input("Fecha", datetime.now())
    col2.text_input("Cliente N°")
    col3.text_input("Contrato")
    col4.text_input("% L.O.")

    c_ins, c_anio = st.columns(2)
    c_ins.text_input("Colegio / Instituto")
    c_anio.text_input("Año y División")

    st.markdown("---")
    st.write("**DATOS DEL ALUMNO**")
    ca1, ca2 = st.columns(2)
    ca1.text_input("Apellido")
    ca2.text_input("Nombres")
    ca1.text_input("D.N.I. Nº")
    ca2.date_input("Vencimiento D.N.I.") 
    ca1.date_input("Fecha de Nacimiento", min_value=datetime(1990,1,1))
    ca2.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

    st.markdown("---")
    st.write("**DATOS DE LOS PADRES**")
    ct1, ct2 = st.columns(2)
    ct1.text_input("Madre / Padre / Tutor (1)")
    ct1.text_input("D.N.I. (1)")
    ct2.text_input("Madre / Padre / Tutor (2)")
    ct2.text_input("D.N.I. (2)")
    
    st.text_input("E-mail de contacto")
    st.text_area("Observaciones")

    st.markdown("---")
    st.write("**PLAN DE PAGO ELEGIDO**")
    plan_sel = st.pills("Seleccione:", options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], label_visibility="collapsed")
    if plan_sel == "OTROS":
        st.text_input("Aclarar plan:")

    # TEXTO LEGAL
    st.markdown(f"""
        <div style="font-size: 0.9rem; text-align: justify; border: 1px solid #ccc; padding: 15px; color: black; background: #fff;">
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
    fcol1.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Firma</p>", unsafe_allow_html=True)
    fcol2.markdown("<hr style='border:1px solid black;'><p style='text-align:center;'>Aclaración y DNI</p>", unsafe_allow_html=True)

    # --- EL BOTÓN INFALIBLE (HTML COMPONENT) ---
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Creamos un botón real de HTML que no depende del motor de Streamlit para ejecutarse
    components.html(
        """
        <html>
            <head>
            <style>
                .print-button {
                    background-color: #2E7D32;
                    border: none;
                    color: white;
                    padding: 15px 32px;
                    text-align: center;
                    text-decoration: none;
                    display: block;
                    font-size: 18px;
                    font-weight: bold;
                    margin: 4px 2px;
                    cursor: pointer;
                    width: 100%;
                    border-radius: 12px;
                }
                .print-button:hover {
                    background-color: #1B5E20;
                }
            </style>
            </head>
            <body>
                <button class="print-button" onclick="window.parent.print()">🖨️ GENERAR PDF / IMPRIMIR</button>
            </body>
        </html>
        """,
        height=100,
    )
