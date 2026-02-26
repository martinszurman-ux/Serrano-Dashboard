import streamlit as st
import pandas as pd
import os

# 1. Configuración de página y Estilos CSS Profesionales
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

st.markdown("""
    <style>
    .header-container {
        position: relative;
        height: 200px;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        border-radius: 15px;
        margin-bottom: 30px;
    }
    .header-image-blur {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: url('https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png');
        background-size: cover;
        background-position: center;
        filter: blur(10px) brightness(0.4); 
        z-index: -1;
    }
    .header-text {
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.9);
        letter-spacing: 1px;
    }
    [data-testid="stMetricValue"] { 
        font-size: 2rem !important; 
        color: #1E3A8A; 
        font-weight: bold;
    }
    .promo-box {
        background-color: #e8f5e9; 
        padding: 18px; 
        border-radius: 12px; 
        border-left: 6px solid #2e7d32; 
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .footer-text { font-size: 0.8rem; color: #6c757d; line-height: 1.4; }
    </style>
    """, unsafe_allow_html=True)

# Logo y Sidebar
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    
    # Selección de Destino (Villa Carlos Paz o San Pedro)
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    opcion = st.radio("📂 Navegación", [
        "Tarifas y Formas de Pago", 
        "Formulario de Preventa",
        "Transporte", 
        "Hotelería", 
        "Excursiones",
        "Seguro Médico", 
        "Regalos y Promociones"
    ])

    st.sidebar.divider()
    st.markdown(f"""
    <div class="footer-text">
    <b>Nuestras Oficinas</b><br>
    Av. Rivadavia 4532 - Galería Alefa (local 10)<br>
    Del Cimarrón 1846 - Parque Leloir<br><br>
    <b>WhatsApp</b><br>
    (011) 5609-6283
    </div>
    """, unsafe_allow_html=True)

# Función para limpiar nombres de archivos CSV
def limpiar_nombre_archivo(texto):
    reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", " ": "_"}
    texto = texto.lower()
    for original, reemplazo in reemplazos.items():
        texto = texto.replace(original, reemplazo)
    return texto + ".csv"

# --- SECCIÓN TARIFAS ---
if opcion == "Tarifas y Formas de Pago":
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
                <div class="header-image-blur"></div>
                <div class="header-text">TARIFARIO {destino.upper()} 2026/27</div>
            </div>
        """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    if os.path.exists(path_tarifas):
        df_tarifas = pd.read_csv(path_tarifas)
        programa_sel = st.selectbox("🎯 Seleccioná tu Plan de Viaje:", df_tarifas['Programa'])
        v = df_tarifas[df_tarifas['Programa'] == programa_sel].iloc[0]

        st.divider()
        col1, col2, col3 = st.columns([1.1, 0.9, 1.4])

        with col1:
            columnas_cuotas = [c.replace('_', ' ') for c in df_tarifas.columns if c not in ['Programa', 'Contado']]
            cuota_label = st.pills("Opciones de pago:", options=columnas_cuotas, default=columnas_cuotas[0])
        
        col_name = cuota_label.replace(' ', '_')
        
        # Extracción de valores numéricos de los planes 
        monto_cuota = float(str(v[col_name]).replace('$', '').replace('.', '').replace(',', ''))
        monto_contado = float(str(v['Contado']).replace('$', '').replace('.', '').replace(',', ''))

        with col2:
            st.metric(label=f"Monto {cuota_label}", value=f"${monto_cuota:,.0f}")

        with col3:
            st.markdown(f"""
            <div class="promo-box">
                <p style="margin:0; color: #2e7d32; font-weight: bold; font-size: 0.85rem;">💎 BENEFICIO PAGO EFECTIVO</p>
                <h3 style="margin:5px 0; color: #1b5e20;">Final: ${monto_contado * 0.9:,.0f}</h3>
                <p style="margin:0; font-size: 0.8rem; color: #388e3c;">Incluye 10% de bonificación especial.</p>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Comparativa de todos los planes"):
            st.dataframe(df_tarifas.set_index('Programa'))
        
        # Notas finales del documento original [cite: 6]
        st.info("Nota: Se pueden realizar otras opciones de pago de acuerdo a la necesidad de cada familia.")

# --- SECCIÓN FORMULARIO PREVENTA ---
elif opcion == "Formulario de Preventa":
    st.header("📝 Ficha de Inscripción")
    with st.form("preventa_form"):
        c1, c2 = st.columns(2)
        nombre = c1.text_input("Nombre Alumno")
        apellido = c2.text_input("Apellido Alumno")
        dni = c1.text_input("DNI")
        colegio = c2.text_input("Colegio")
        obs = st.text_area("Observaciones Médicas / Dietas")
        enviar = st.form_submit_button("Generar Comprobante")
    
    if enviar:
        st.success("Ficha lista para imprimir (Ctrl+P)")
        st.markdown(f"""
            <div style="border:2px solid #333; padding:20px; background:white; color:black">
                <h2 style="text-align:center">SERRANO TURISMO - PREVENTA</h2>
                <p><b>Pasajero:</b> {nombre} {apellido} | <b>DNI:</b> {dni}</p>
                <p><b>Colegio:</b> {colegio}</p>
                <p><b>Observaciones:</b> {obs}</p>
                <hr>
                <p style="font-size:0.8rem">Este documento es una reserva preliminar sujeta a firma de contrato.</p>
            </div>
        """, unsafe_allow_html=True)

# --- VISTA ESTÁNDAR (OTROS CONTENIDOS) ---
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
        st.error(f"El archivo {limpiar_nombre_archivo(opcion)} no se encuentra en la carpeta {folder}.")

# Pie de página Sidebar
st.sidebar.markdown(f"### [📲 Consultar por WhatsApp](https://api.whatsapp.com/send?phone=5491167877990&text=Hola%20Martin,%20consulto%20por%20{destino})")
