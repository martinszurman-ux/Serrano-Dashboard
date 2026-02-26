import streamlit as st
import pandas as pd
import os
from datetime import datetime

# =================================================================
# 🚀 ÁREA DE TRABAJO DE: [TU NOMBRE / VERSIÓN ACTUALIZADA]
# MODIFICACIÓN: Solicitud de Adhesión con Textos Legales y Estilo Gris
# =================================================================

# 1. Configuración de página
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Contenedores Grises Profesionales */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #f8f9fa !important;
        border: 1px solid #dee2e6 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02) !important;
    }
    
    /* Header de Tarifas */
    .header-container {
        position: relative;
        height: 180px;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        margin-bottom: 30px;
        background-color: #495057;
        overflow: hidden;
    }
    
    .header-text-overlay {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }

    .widget-title { color: #6c757d; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-bottom: 5px; }
    .widget-value { color: #212529; font-size: 2.2rem; font-weight: 800; margin: 0; }
    .promo-subtitle { font-size: 0.75rem; color: #adb5bd; margin-top: 5px; }

    /* Textos Legales de Solicitud */
    .text-legal {
        font-size: 0.85rem;
        line-height: 1.5;
        color: #333;
        text-align: justify;
        background: #f1f3f5;
        padding: 15px;
        border-radius: 8px;
    }

    /* Configuración para Impresión */
    @media print {
        header, [data-testid="stSidebar"], .stButton, .no-print {
            display: none !important;
        }
        .main .block-container {
            padding: 0 !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# --- SIDEBAR ---
with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    st.info("🛠️ EDITANDO: Sección Solicitud") # Marca visual para tu compañero
    
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    opcion = st.radio("📂 Navegación", [
        "Tarifas y Formas de Pago", 
        "Transporte", "Hotelería", "Excursiones", 
        "Solicitud de Adhesión", "Seguro Médico"
    ])

    st.sidebar.divider()
    st.markdown("""
    <div style="font-size: 0.8rem; color: #6c757d;">
    <b>CABA:</b> Av. Rivadavia 4532<br>
    <b>Leloir:</b> Del Cimarrón 1846<br>
    <b>WA:</b> (011) 5609-6283
    </div>
    """, unsafe_allow_html=True)

# Función de limpieza
def limpiar_nombre_archivo(texto):
    reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", " ": "_"}
    texto = texto.lower()
    for original, reemplazo in reemplazos.items(): 
        texto = texto.replace(original, reemplazo)
    return texto + ".csv"

# =================================================================
# 📋 SECCIÓN: SOLICITUD DE ADHESIÓN (REVISIÓN ACTUAL)
# =================================================================
if opcion == "Solicitud de Adhesión":
    st.image(LOGO_URL, width=180)
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    with st.form("form_adhesion_v2"):
        col1, col2, col3, col4 = st.columns(4)
        with col1: f_doc = st.date_input("Fecha", datetime.now())
        with col2: c_num = st.text_input("Cliente N°")
        with col3: cont = st.text_input("Contrato")
        with col4: perc_lo = st.text_input("% L.O.")

        c_a, c_b = st.columns(2)
        with c_a: col_ins = st.text_input("Colegio / Instituto")
        with c_b: anio_div = st.text_input("Año y Div.")

        st.markdown("---")
        st.write("**DATOS DEL ALUMNO**")
        c_al1, c_al2 = st.columns(2)
        with c_al1:
            ape_al = st.text_input("Apellido")
            dni_al = st.text_input("D.N.I. Nº")
            fnac_al = st.date_input("Fecha de Nacimiento", min_value=datetime(2000,1,1))
        with c_al2:
            nom_al = st.text_input("Nombres")
            nac_al = st.text_input("Nacionalidad", value="Argentina")
            sex_al = st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        c_d1, c_d2, c_d3 = st.columns([2, 1, 1])
        with c_d1: dom_al = st.text_input("Domicilio")
        with c_d2: cp_al = st.text_input("C.P.")
        with c_d3: loc_al = st.text_input("Localidad")
        
        c_d4, c_d5 = st.columns(2)
        with c_d4: prov_al = st.text_input("Provincia", value="Buenos Aires")
        with c_d5: tel_al = st.text_input("Teléfono (Cod. Área + Número)")

        st.markdown("---")
        st.write("**DATOS DE LOS PADRES / TUTORES**")
        c_t1, c_t2 = st.columns(2)
        with c_t1:
            t1_nom = st.text_input("Madre / Padre / Tutor (1)")
            t1_dni = st.text_input("D.N.I. (1)")
        with c_t2:
            t2_nom = st.text_input("Madre / Padre / Tutor (2)")
            t2_dni = st.text_input("D.N.I. (2)")
        
        email_cto = st.text_input("E-mail de contacto:")
        st.caption("La información será enviada al e-mail del representante del grupo.")

        st.markdown("#### OBSERVACIONES")
        obs_texto = st.text_area("", label_visibility="collapsed")

        st.markdown("---")
        st.markdown("""
        <div class="text-legal">
        Declaro bajo juramento que los datos aquí volcados son absolutamente exactos y acepto, para la cancelación de los servicios 
        a prestar por <b>TRANSPORTE SERRANO TURISMO RECREATIVO</b>, el plan de pagos denominado:
        </div>
        """, unsafe_allow_html=True)
        
        plan_sel = st.radio("Seleccione Plan:", ["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "OTROS"], horizontal=True)

        st.markdown("""
        <div class="text-legal">
        <br>
        <b>PLAN 1:</b> Cuotas mensuales según contrato.<br>
        <b>PLAN 2:</b> Pago contado dentro de los 30 días de la firma.<br><br>
        <b>NOTA:</b> De no marcarse plan, se emitirá como PLAN 1 (Cuotas). Las cuotas vencen del 1 al 10 de cada mes. 
        La empresa no se responsabiliza por falta de entrega de chequera si los datos son erróneos.<br><br>
        <b>IMPORTANTE:</b> Servicios con Seguro de Caución (Ley 25.599) de la compañía <b>ALBA CAUCION</b>. 
        Serrano Turismo Recreativo Leg. 12.441 disp. 1018/05.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            st.divider()
            st.caption("Firma del Responsable")
        with f_col2:
            st.divider()
            st.caption("Aclaración y DNI")

        st.form_submit_button("Guardar Datos")

    st.button("🖨️ Imprimir Formulario Completo", on_click=lambda: st.write('<script>window.print();</script>', unsafe_allow_html=True))

# =================================================================
# 💰 SECCIÓN: TARIFAS
# =================================================================
elif opcion == "Tarifas y Formas de Pago":
    st.markdown(f'<div class="header-container"><div class="header-text-overlay">TARIFAS {destino.upper()}</div></div>', unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        prog = st.selectbox("🎯 Plan de Viaje:", df['Programa'])
        v = df[df['Programa'] == prog].iloc[0]

        st.divider()
        col1, col2, col3 = st.columns(3)

        def to_num(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col1:
            with st.container(border=True):
                st.markdown("<p class='widget-title'>OPCIONES DE PAGO</p>", unsafe_allow_html=True)
                cols_cuotas = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
                cuota_sel = st.pills("Seleccione:", options=cols_cuotas, default=cols_cuotas[0], label_visibility="collapsed")
        
        col_db = cuota_sel.replace(' ', '_')
        val_cuota = to_num(v[col_db])
        val_contado = to_num(v['Contado'])

        with col2:
            with st.container(border=True):
                st.markdown(f"<div style='text-align: center;'><p class='widget-title'>MONTO {cuota_sel.upper()}</p><p class='widget-value'>${val_cuota:,.0f}</p></div>", unsafe_allow_html=True)

        with col3:
            with st.container(border=True):
                st.markdown(f"<div style='text-align: center;'><p class='widget-title'>💎 EFECTIVO (10% OFF)</p><p class='widget-value' style='color: #495057;'>${val_contado * 0.9:,.0f}</p></div>", unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver tabla comparativa"):
            st.table(df.set_index('Programa'))

# =================================================================
# 🔹 RESTO DE SECCIONES
# =================================================================
else:
    st.title(opcion)
    path_info = f"data/{folder}/{limpiar_nombre_archivo(opcion)}"
    if os.path.exists(path_info):
        df_info = pd.read_csv(path_info)
        for _, row in df_info.iterrows():
            with st.expander(f"🔹 {row['Titulo']}", expanded=True):
                st.write(row['Contenido'])
                if 'Destacado' in row: st.info(row['Destacado'])

st.sidebar.divider()
st.sidebar.caption("Serrano Turismo - 29 años")
