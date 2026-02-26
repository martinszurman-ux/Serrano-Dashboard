import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# Estilo para la imagen de fondo en la parte superior y diseño general
st.markdown("""
    <style>
    .header-image {
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
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

# --- LÓGICA DE VISUALIZACIÓN ---

if opcion == "Tarifas y Formas de Pago":
    # Imagen de fondo arriba (Tarifario)
    st.markdown('<img src="https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png" class="header-image">', unsafe_allow_html=True)
    st.title("💰 Tarifario Exclusivo 2027")

    if os.path.exists(path):
        df_tarifas = pd.read_csv(path)
        
        # Selector de Programa
        programa_elegido = st.selectbox("Seleccioná tu opción de viaje:", df_tarifas['Programa'])
        datos_plan = df_tarifas[df_tarifas['Programa'] == programa_elegido].iloc[0]
        
        col_selec, col_widget = st.columns([1, 1])
        
        with col_selec:
            st.subheader("Configurá tu plan")
            cuota_sel = st.select_slider(
                "Cantidad de cuotas fijas:",
                options=["Contado", "3 Cuotas", "6 Cuotas", "12 Cuotas", "18 Cuotas"]
            )
            
            # Limpieza de valores (por si vienen con $)
            def clean_val(val):
                if isinstance(val, str):
                    return float(val.replace('$', '').replace('.', '').replace(',', '').strip())
                return val

            col_map = {"Contado": "Contado", "3 Cuotas": "3_Cuotas", "6 Cuotas": "6_Cuotas", "12 Cuotas": "12_Cuotas", "18 Cuotas": "18_Cuotas"}
            valor_cuota = clean_val(datos_plan[col_map[cuota_sel]])
            valor_contado = clean_val(datos_plan['Contado'])

        with col_widget:
            st.metric(label=f"Valor de {cuota_sel}", value=f"${valor_cuota:,.0f}")
            
            # Cálculo del 10% de descuento sobre el valor total de contado
            valor_con_descuento = valor_contado * 0.90
            
            st.markdown(f"""
            <div style="background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32;">
                <p style="margin:0; color: #2e7d32; font-weight: bold;">💎 BENEFICIO PAGO EFECTIVO</p>
                <p style="margin:5px 0; font-size: 0.9em;">Si abonás la totalidad de las cuotas en efectivo en nuestra oficina, obtenés un 10% de descuento adicional sobre el valor de contado.</p>
                <h3 style="margin:0; color: #1b5e20;">Valor Final: ${valor_con_descuento:,.0f}</h3>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.subheader("📊 Comparativo de Opciones")
        st.dataframe(df_tarifas, use_container_width=True)

        # Notas del PDF en negrita y profesionales
        st.markdown("""
        ### 📋 Notas Importantes del Servicio
        * **Liberados:** Disponibles para niños y acompañantes según contrato.
        * **Bonificaciones:** Descuentos aplicables según las formas de pago elegidas.
        * **Vigencia:** Los valores expresados corresponden a la temporada 2027.
        """)
    else:
        st.error("No se encontró el archivo de tarifas.")

else:
    # Visualización estándar para el resto de las secciones
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
