import streamlit as st
import pandas as pd
import os
from datetime import datetime

# =================================================================
# 🛠️ ÁREA DE TRABAJO: [TU NOMBRE] - VERSIÓN RESTAURADA
# CAMBIOS: Recuperación de Formulario Original + Tarifas Niveladas
# =================================================================

# 1. Configuración de página
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Estilo Gris Profesional para Contenedores */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #f8f9fa !important;
        border: 1px solid #dee2e6 !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }
    
    /* Header de Secciones */
    .header-container {
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        background-color: #495057;
        margin-bottom: 30px;
    }
    
    .header-text-overlay {
        color: white;
        font-size: 2.2rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Widgets de Tarifas */
    .widget-title { color: #6c757d; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; }
    .widget-value { color: #212529; font-size: 2.2rem; font-weight: 800; margin: 0; }
    .promo-subtitle { font-size: 0.75rem; color: #adb5bd; }

    /* Estilo de Impresión */
    @media print {
        header, [data-testid="stSidebar"], .stButton, .no-print {
            display: none !important;
        }
        .main .block-container {
            padding: 0 !important;
        }
    }

    .text-legal {
        font-size: 0.8rem;
        line-height: 1.4;
        color: #333;
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# --- SIDEBAR ---
with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    st.warning("⚠️ MODO EDICIÓN ACTIVADO") # Aviso para tu compañero
    
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    opcion = st.radio("📂 Navegación", [
        "Tarifas y Formas de Pago", 
        "Transporte", "Hotelería", "Excursiones", 
        "Solicitud de Adhesión", "Seguro Médico"
    ])

# Función de limpieza de archivos
def limpiar_nombre_archivo(texto):
    reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", " ": "_"}
    texto = texto.lower()
    for original, reemplazo in reemplazos.items(): 
        texto = texto.replace(original, reemplazo)
    return texto + ".csv"

# =================================================================
# 📋 SECCIÓN: SOLICITUD DE ADHESIÓN (FORMULARIO ORIGINAL)
# =================================================================
if opcion == "Solicitud de Adhesión":
    st.image(LOGO_URL, width=180)
    st.markdown("<h2 style='text-align: center;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    with st.form("form_adhesion_original"):
        # Encabezado del documento
        col1, col2, col3, col4 = st.columns(4)
        with col1: f_doc = st.date_input("Fecha", datetime.now())
        with col2: c_num = st.text_input("Cliente N°")
        with col3: cont = st.text_input("Contrato")
        with col4: perc_lo = st.text_input("% L.O.")

        c_inst, c_anio = st.columns(2)
        with c_inst: colegio = st.text_input("Colegio / Instituto")
        with c_anio: anio_div = st.text_input("Año y Div.")

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

        c_dom1, c_dom2, c_dom3 = st.columns([2, 1, 1])
        with c_dom1: dom_al = st.text_input("Domicilio")
        with c_dom2: cp_al = st.text_input("Código Postal")
        with c_dom3: loc_al = st.text_input("Localidad")
        
        c_dom4, c_dom5 = st.columns(2)
        with c_dom4: prov_al = st.text_input("Provincia", value="Buenos Aires")
        with c_dom5: tel_al = st.text_input("Teléfono (Cod. Área + Número)")

        st.markdown("---")
        st.write("**DATOS DE LOS PADRES / TUTORES**")
        c_tut1, c_tut2 = st.columns(2)
        with c_tut1:
            t1_nom = st.text_input("Madre / Padre / Tutor (1)")
            t1_dni = st.text_input("D.N.I. (1)")
        with c_tut2:
            t2_nom = st.text_input("Madre / Padre / Tutor (2)")
            t2_dni = st.text_input("D.N.I. (2)")
        
        email_p = st.text_input("E-mail:")
        st.caption("Información enviada al e-mail del representante del grupo.")

        st.markdown("#### OBSERVACIONES")
        obs_val = st.text_area("", label_visibility="collapsed")

        st.markdown("---")
        st.markdown("""<div class="text-legal">Declaro bajo juramento que los datos aquí volcados son exactos y acepto el plan de pagos denominado:</div>""", unsafe_allow_html=True)
        
        plan_elegido = st.radio("Seleccione Plan:", ["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "OTROS"], horizontal=True)

        st.markdown("""
        <div class="text-legal">
        <br><b>PLAN 1:</b> Cuotas mensuales según contrato. <b>PLAN 2:</b> Pago contado dentro de los 30 días.<br><br>
        <b>NOTA:</b> Las cuotas vencen del 1 al 10 de cada mes. Pasada esa fecha, sufrirá el recargo correspondiente.
        La empresa no se responsabiliza por falta de entrega de chequera si los datos son erróneos.<br><br>
        <b>IMPORTANTE:</b> Los servicios cuentan con Seguro de Caución (Ley 25.599) de la compañía <b>ALBA CAUCION</b>.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        f_c1, f_c2 = st.columns(2)
        with f_c1:
            st.divider()
            st.caption("Firma del Tutor")
        with f_c2:
            st.divider()
            st.caption("Aclaración y DNI")

        st.form_submit_button("Guardar Formulario")

    st.button("🖨️ Imprimir Formulario", on_click=lambda: st.write('<script>window.print();</script>', unsafe_allow_html=True))

# =================================================================
# 💰 SECCIÓN: TARIFAS (WIDGETS NIVELADOS)
# =================================================================
elif opcion == "Tarifas y Formas de Pago":
    st.markdown(f'<div class="header-container"><div class="header-text-overlay">TARIFAS {destino.upper()}</div></div>', unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        prog_sel = st.selectbox("🎯 Plan de Viaje:", df['Programa'])
        v = df[df['Programa'] == prog_sel].iloc[0]

        st.divider()
        col1, col2, col3 = st.columns(3)

        def to_n(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col1:
            with st.container(border=True):
                st.markdown("<p class='widget-title'>OPCIONES DE PAGO</p>", unsafe_allow_html=True)
                cols_c = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
                cuota_sel = st.pills("Seleccione:", options=cols_c, default=cols_c[0], label_visibility="collapsed")
        
        c_db = cuota_sel.replace(' ', '_')
        val_c = to_n(v[c_db])
        val_cont = to_n(v['Contado'])

        with col2:
            with st.container(border=True):
                st.markdown(f"<div style='text-align: center;'><p class='widget-title'>MONTO {cuota_sel.upper()}</p><p class='widget-value'>${val_c:,.0f}</p></div>", unsafe_allow_html=True)

        with col3:
            with st.container(border=True):
                st.markdown(f"<div style='text-align: center;'><p class='widget-title'>💎 EFECTIVO (10% OFF)</p><p class='widget-value' style='color: #495057;'>${val_cont * 0.9:,.0f}</p></div>", unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver tabla comparativa completa"):
            st.table(df.set_index('Programa'))
    else:
        st.error("Base de datos no encontrada.")


# =================================================================
# SECCIÓN: SEGURO MÉDICO (CÓDIGO PARA PEGAR EN APP.PY)
# =================================================================
elif opcion == "Seguro Médico":
    # CSS específico para asegurar tamaños uniformes y alineación
    st.markdown("""
        <style>
        .med-container {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            border: 1px solid #e0e0e0;
            box-shadow: 8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff;
            margin-bottom: 15px;
            /* Forzar altura uniforme */
            min-height: 380px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .med-icon { font-size: 4rem; margin-bottom: 20px; }
        .med-title { 
            color: #495057; 
            font-size: 1.2rem; 
            font-weight: 800; 
            text-transform: uppercase; 
            margin-bottom: 15px;
            min-height: 50px;
            display: flex;
            align-items: center;
        }
        .med-text { color: #6c757d; font-size: 0.95rem; line-height: 1.5; }
        </style>
    """, unsafe_allow_html=True)

    # 1. Cabecera con Logo de Assistravel
    st.markdown(f"""
        <div style="text-align: center; padding: 20px; background: #f8f9fa; border-radius: 20px; border: 1px solid #eee; margin-bottom: 30px;">
            <img src="https://assistravel.com/web/image/website/1/logo/Assistravel?unique=966a426" width="280">
            <h2 style="color: #495057; font-weight: 800; margin-top: 15px;">COBERTURA MÉDICA NACIONAL</h2>
        </div>
    """, unsafe_allow_html=True)

    st.write("Serrano Turismo brinda tranquilidad total mediante la cobertura de *Assistravel*, diseñada específicamente para el turismo estudiantil.")

    # 2. Widgets de tamaño uniforme en paralelo
    col_m1, col_m2, col_m3 = st.columns(3)

    with col_m1:
        st.markdown("""
            <div class="med-container">
                <div class="med-icon">🏥</div>
                <div class="med-title">Asistencia en Destino</div>
                <p class="med-text">Atención primaria y de especialistas las 24 hs en Villa Carlos Paz y San Pedro, incluyendo traslados sanitarios.</p>
            </div>
        """, unsafe_allow_html=True)

    with col_m2:
        st.markdown("""
            <div class="med-container">
                <div class="med-icon">💊</div>
                <div class="med-title">Servicio de Farmacia</div>
                <p class="med-text">Cobertura completa en medicamentos recetados por enfermedad o accidente durante todo el itinerario.</p>
            </div>
        """, unsafe_allow_html=True)

    with col_m3:
        st.markdown("""
            <div class="med-container">
                <div class="med-icon">🛡️</div>
                <div class="med-title">Seguro de Accidentes</div>
                <p class="med-text">Incluye seguro de Accidentes Personales y Responsabilidad Civil por plaza, cumpliendo la Ley Nacional de Turismo.</p>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

    # 3. Información Complementaria (App Viaxlab)
    st.markdown("### 📲 Control y Seguimiento en Tiempo Real")
    st.write("Cada pasajero cuenta con una pulsera inteligente con tecnología NFC integrada a la *App Viaxlab*, permitiendo que los padres sigan el estado de salud y las actividades de sus hijos en tiempo real.")

# =================================================================
# FIN DE LA SECCIÓN SEGURO MÉDICO
# =================================================================





# --- SECCIONES ESTÁNDAR ---
else:
    st.title(opcion)
    p_info = f"data/{folder}/{limpiar_nombre_archivo(opcion)}"
    if os.path.exists(p_info):
        df_i = pd.read_csv(p_info)
        for _, row in df_i.iterrows():
            with st.expander(f"🔹 {row['Titulo']}", expanded=True):
                st.write(row['Contenido'])
                if 'Destacado' in row: st.info(row['Destacado'])

st.sidebar.divider()
st.sidebar.caption("Serrano Turismo - 29 años")
