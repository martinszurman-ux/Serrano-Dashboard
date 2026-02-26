import streamlit as st
import pandas as pd
import os

# 1. Configuración de página y Estética Profesional (Gris)
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

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
    
    /* Estilo del Header con la imagen de tarifas */
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

    /* Ajustes de texto en los widgets de monto */
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
    </style>
    """, unsafe_allow_html=True)

# Logo y Sidebar - URL corregida
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    opcion = st.radio("📂 Navegación", [
        "Tarifas y Formas de Pago", 
        "Transporte", "Hotelería", "Excursiones", 
        "Formulario de Preventa", "Seguro Médico"
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

# --- SECCIÓN TARIFAS ---
if opcion == "Tarifas y Formas de Pago":
    # Header dinámico
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

        # TRIPLE WIDGET EN PARALELO (GRIS PROFESIONAL)
        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container(border=True):
                st.markdown("<p class='widget-title'>OPCIONES DE PAGO</p>", unsafe_allow_html=True)
                cols_cuotas = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
                cuota_sel = st.pills("Seleccione:", options=cols_cuotas, default=cols_cuotas[0], label_visibility="collapsed")
        
        # Limpieza de valores numéricos de los planes 
        col_db = cuota_sel.replace(' ', '_')
        val_cuota = float(str(v[col_db]).replace('$', '').replace('.', '').replace(',', '').strip())
        val_contado = float(str(v['Contado']).replace('$', '').replace('.', '').replace(',', '').strip())

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
