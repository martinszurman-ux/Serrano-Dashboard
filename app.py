import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. Configuración de página y Estética Profesional
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# Estilos CSS
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Contenedores con bordes y fondo gris profesional */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #f8f9fa !important;
        border: 1px solid #dee2e6 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02) !important;
    }
    
    /* Estilo del Header */
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

    .widget-title {
        color: #6c757d;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .widget-value {
        color: #212529;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }

    .promo-subtitle {
        font-size: 0.75rem;
        color: #adb5bd;
        margin-top: 5px;
    }

    /* Estilo específico para impresión */
    @media print {
        header, [data-testid="stSidebar"], .stButton, .no-print {
            display: none !important;
        }
        .main .block-container {
            padding: 0 !important;
        }
        .print-only {
            display: block !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# --- SIDEBAR ---
with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
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

# Función para limpiar nombres de archivos
def limpiar_nombre_archivo(texto):
    reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", " ": "_"}
    texto = texto.lower()
    for original, reemplazo in reemplazos.items():
        texto = texto.replace(original, reemplazo)
    return texto + ".csv"

# --- SECCIÓN: SOLICITUD DE ADHESIÓN ---
if opcion == "Solicitud de Adhesión":
    st.image(LOGO_URL, width=200)
    st.title("📄 Solicitud de Ingreso / Adhesión")
    st.subheader("Ficha del Cliente / Pasajero")

    with st.form("formulario_adhesion"):
        col1, col2, col3 = st.columns(3)
        with col1:
            fecha_doc = st.date_input("Fecha", datetime.now())
            contrato = st.text_input("Contrato N°")
        with col2:
            colegio = st.text_input("Colegio / Instituto")
            año_div = st.text_input("Año y División")
        with col3:
            liberado = st.text_input("% L.O. (Porcentaje Liberado)")

        st.markdown("#### Datos del Alumno")
        c_al1, c_al2 = st.columns(2)
        with c_al1:
            ap_alumno = st.text_input("Apellido Alumno")
            dni_alumno = st.text_input("DNI Alumno")
            f_nac_alumno = st.date_input("Fecha de Nacimiento", min_value=datetime(2000,1,1))
        with c_al2:
            nom_alumno = st.text_input("Nombres Alumno")
            dni_venc = st.date_input("Vencimiento de DNI")
            nacionalidad = st.text_input("Nacionalidad", value="Argentina")
        
        sexo = st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        st.markdown("#### Domicilio y Contacto")
        c_dom1, c_dom2, c_dom3 = st.columns([2, 1, 1])
        with c_dom1:
            domicilio = st.text_input("Domicilio")
        with c_dom2:
            cp = st.text_input("Código Postal")
        with c_dom3:
            localidad = st.text_input("Localidad")
        
        c_dom4, c_dom5 = st.columns(2)
        with c_dom4:
            provincia = st.text_input("Provincia", value="Buenos Aires")
        with c_dom5:
            telefono = st.text_input("Teléfono (Cod. Área + Número)")

        st.markdown("#### Datos de los Padres / Tutores")
        c_p1, c_p2 = st.columns(2)
        with c_p1:
            padre_nom = st.text_input("Nombre y Apellido Padre / Tutor (1)")
            padre_dni = st.text_input("DNI Padre")
        with c_p2:
            madre_nom = st.text_input("Nombre y Apellido Madre / Tutor (2)")
            madre_dni = st.text_input("DNI Madre")
        
        email_padres = st.text_input("E-mail de contacto (Madre o Padre)")

        st.markdown("#### Plan de Pago Elegido")
        plan_pago = st.radio("Seleccione el plan de pago acordado:", 
                             ["PLAN 1: Cuotas mensuales según contrato", 
                              "PLAN 2: Pago contado (dentro de los 30 días)", 
                              "PLAN 3: Plan personalizado", 
                              "PLAN 4: Plan especial grupo", 
                              "OTROS: Ver observaciones"], horizontal=False)

        observaciones = st.text_area("Observaciones")

        st.markdown("---")
        st.write("**Declaración Jurada:** Declaro bajo juramento que los datos aquí volcados son absolutamente exactos y acepto, para la cancelación de los servicios a prestar por SERRANO TURISMO, el plan de pagos mencionado anteriormente. Declaro conocer todas y cada una de las condiciones del contrato suscripto.")
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.divider()
            st.caption("Firma del Padre/Madre/Tutor")
        with col_f2:
            st.divider()
            st.caption("Aclaración y DNI")

        submitted = st.form_submit_button("Finalizar y Preparar para Imprimir")
        
        if submitted:
            st.success("Formulario completado. Use el botón de abajo para imprimir.")
            st.info("💡 Consejo: Al abrirse la ventana de impresión, guarde como 'PDF' o seleccione su impresora.")

    # Botón de impresión (fuera del form para ejecutar JS)
    st.button("🖨️ Enviar a Imprimir Formulario", on_click=lambda: st.write('<script>window.print();</script>', unsafe_allow_html=True))

# --- SECCIÓN TARIFAS ---
elif opcion == "Tarifas y Formas de Pago":
    header_img_path = None
    for ext in [".jpg", ".png", ".jpeg"]:
        temp_path = f"data/{folder}/tarifas_y_formas_header{ext}"
        if os.path.exists(temp_path):
            header_img_path = temp_path
            break

    if header_img_path:
        st.image(header_img_path, use_container_width=True)
    else:
        st.markdown(f"""
            <div class="header-container">
                <div class="header-text-overlay">TARIFAS {destino.upper()}</div>
            </div>
        """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        prog = st.selectbox("🎯 Plan de Viaje:", df['Programa'])
        v = df[df['Programa'] == prog].iloc[0]

        st.divider()
        col1, col2, col3 = st.columns(3)

        def clean_val(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col1:
            with st.container(border=True):
                st.markdown("<p class='widget-title'>OPCIONES DE PAGO</p>", unsafe_allow_html=True)
                cols_cuotas = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
                cuota_sel = st.pills("Seleccione:", options=cols_cuotas, default=cols_cuotas[0], label_visibility="collapsed")
        
        col_db = cuota_sel.replace(' ', '_')
        val_cuota = clean_val(v[col_db])
        val_contado = clean_val(v['Contado'])

        with col2:
            with st.container(border=True):
                st.markdown(f"""
                    <div style='text-align: center;'>
                        <p class='widget-title'>MONTO {cuota_sel.upper()}</p>
                        <p class='widget-value'>${val_cuota:,.0f}</p>
                    </div>
                """, unsafe_allow_html=True)

        with col3:
            with st.container(border=True):
                st.markdown(f"""
                    <div style='text-align: center;'>
                        <p class='widget-title'>💎 PAGO EFECTIVO (OFICINA)</p>
                        <p class='widget-value' style='color: #495057;'>${val_contado * 0.9:,.0f}</p>
                        <p class='promo-subtitle'>Incluye bonificación especial del 10%</p>
                    </div>
                """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver tabla comparativa completa"):
            st.table(df.set_index('Programa'))
        st.info("Nota: Las opciones de pago se complementan con el plan de cuotas ajustado por IPC según contrato.")

# --- VISTA ESTÁNDAR ---
else:
    st.title(opcion)
    path_info = f"data/{folder}/{limpiar_nombre_archivo(opcion)}"
    if os.path.exists(path_info):
        df_info = pd.read_csv(path_info)
        for _, row in df_info.iterrows():
            with st.expander(f"🔹 {row['Titulo']}", expanded=True):
                st.write(row['Contenido'])
                if 'Destacado' in row: st.info(row['Destacado'])
    else:
        st.error(f"Contenido no disponible para {destino}.")

st.sidebar.divider()
st.sidebar.caption("Serrano Turismo - 29 años de trayectoria")
