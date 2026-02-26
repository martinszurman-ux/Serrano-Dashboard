import streamlit as st
import pandas as pd
import os

# 1. Configuración de página y Estilos CSS Avanzados
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

st.markdown("""
    <style>
    /* Contenedor de imagen esfumada */
    .header-container {
        position: relative;
        height: 220px;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        border-radius: 15px;
        margin-bottom: 30px;
    }
    .header-image {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: url('https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png');
        background-size: cover;
        background-position: center;
        filter: blur(5px) brightness(0.5); /* Efecto esfumado y oscuro */
        z-index: -1;
    }
    .header-text {
        text-align: center;
        font-size: 2.2rem;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
        letter-spacing: 2px;
    }
    /* Estilo para las métricas */
    [data-testid="stMetricValue"] { font-size: 1.8rem !important; color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

# Logo y Sidebar
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    opcion = st.radio("📂 Información del Viaje", [
        "Transporte", "Hotelería", "Régimen de Comidas", 
        "Excursiones de Día", "Actividades Nocturnas", 
        "Seguro Médico", "Coordinación", 
        "Tarifas y Formas de Pago", "Regalos y Promociones"
    ])

# Función para limpiar nombres de archivos
def limpiar_nombre_archivo(texto):
    reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", " ": "_"}
    texto = texto.lower()
    for original, reemplazo in reemplazos.items():
        texto = texto.replace(original, reemplazo)
    return texto + ".csv"

file_name = limpiar_nombre_archivo(opcion)
path = f"data/{folder}/{file_name}"

# --- LÓGICA PRINCIPAL ---

if opcion == "Tarifas y Formas de Pago":
    # Cabecera con Imagen Esfumada
    st.markdown(f"""
        <div class="header-container">
            <div class="header-image"></div>
            <div class="header-text">TARIFARIO {destino.upper()} 2027</div>
        </div>
    """, unsafe_allow_html=True)

    if os.path.exists(path):
        df_tarifas = pd.read_csv(path)
        
        # Selector de Programa
        programa_elegido = st.selectbox("🎯 Seleccioná tu Plan de Viaje:", df_tarifas['Programa'])
        datos_plan = df_tarifas[df_tarifas['Programa'] == programa_elegido].iloc[0]
        
        st.divider()

        # SECCIÓN NIVELADA: Selector, Valor y Beneficio
        col_selec, col_valor, col_promo = st.columns([1.2, 1, 1.3])
        
        with col_selec:
            st.write("**💳 Elegí tus cuotas:**")
            # Selector de cuotas estilo "pills" (moderno)
            cuota_sel = st.pills(
                "Opciones:",
                options=["Contado", "3 Cuotas", "6 Cuotas", "12 Cuotas", "18 Cuotas"],
                default="Contado",
                label_visibility="collapsed"
            )

        # Limpieza y cálculos
        def clean_val(val):
            if isinstance(val, str):
                return float(val.replace('$', '').replace('.', '').replace(',', '').strip())
            return float(val)

        col_map = {"Contado": "Contado", "3 Cuotas": "3_Cuotas", "6 Cuotas": "6_Cuotas", "12 Cuotas": "12_Cuotas", "18 Cuotas": "18_Cuotas"}
        valor_cuota = clean_val(datos_plan[col_map[cuota_sel]])
        valor_contado = clean_val(datos_plan['Contado'])
        valor_con_descuento = valor_contado * 0.90

        with col_valor:
            st.metric(label=f"Monto {cuota_sel}", value=f"${valor_cuota:,.0f}")

        with col_promo:
            st.markdown(f"""
            <div style="background-color: #e8f5e9; padding: 12px; border-radius: 10px; border-left: 5px solid #2e7d32; height: 95px;">
                <p style="margin:0; color: #2e7d32; font-weight: bold; font-size: 0.8rem;">💎 PAGO EFECTIVO (OFICINA)</p>
                <h3 style="margin:0; color: #1b5e20; font-size: 1.4rem;">Final: ${valor_con_descuento:,.0f}</h3>
                <p style="margin:0; font-size: 0.7rem; color: #555;">Incluye 10% de ahorro por pago total.</p>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver tabla comparativa de todos los planes"):
            st.table(df_tarifas.set_index('Programa'))

        # Notas del PDF en negrita y profesionales
        st.markdown("""
        <div style="background-color: #f1f3f5; padding: 15px; border-radius: 8px; border: 1px solid #dee2e6;">
            <p style="margin-bottom: 5px;"><strong>• LIBERADOS PARA NIÑOS Y ACOMPAÑANTES SEGÚN CONTRATO.</strong></p>
            <p style="margin-bottom: 5px;"><strong>• DESCUENTOS ESPECIALES SEGÚN FORMAS DE PAGO SELECCIONADAS.</strong></p>
            <p style="margin-bottom: 0px;"><strong>• VALORES EXPRESADOS EN PESOS ARGENTINOS, TEMPORADA 2027.</strong></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("No se encontró el archivo de tarifas en GitHub.")

else:
    # Resto de las secciones (Transporte, Hotelería, etc.)
    st.title(opcion)
    if os.path.exists(path):
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            with st.expander(f"🔹 {row['Titulo']}", expanded=True):
                st.write(row['Contenido'])
                if 'Destacado' in row:
                    st.info(row['Destacado'])
    else:
        st.error(f"Archivo no encontrado: {file_name}")

st.sidebar.divider()
st.sidebar.caption("Serrano Turismo - 29 años de trayectoria")
