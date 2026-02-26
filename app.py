import streamlit as st
import pandas as pd
import os

# Configuración de página y Estilo Serrano
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

st.markdown("""
    <style>
    .stRadio > label { font-weight: bold; color: #1E3A8A; }
    .stSelectbox > label { font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Logo
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# --- SIDEBAR ---
with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    st.subheader("📂 Menú del Viaje")
    opcion = st.radio("Información disponible:", [
        "Transporte", "Hotelería", "Régimen de Comidas", 
        "Excursiones de Día", "Actividades Nocturnas", 
        "Seguro Médico", "Coordinación", "Regalos y Promociones",
        "Tarifas y Formas de Pago"
    ])
    
    st.divider()
    st.caption("Serrano Turismo - 29 años de trayectoria")

# --- CONTENIDO PRINCIPAL ---
# Convertimos la opción del radio al nombre del archivo csv
file_name = opcion.lower().replace(" ", "_").replace("í", "i").replace("ó", "o") + ".csv"
path = f"data/{folder}/{file_name}"

st.title(f"{opcion}")
st.subheader(f"Destino: {destino}")

if os.path.exists(path):
    df = pd.read_csv(path)
    
    # Mostramos cada fila del CSV como una tarjeta informativa
    for index, row in df.iterrows():
        with st.expander(f"🔹 {row['Titulo']}", expanded=True):
            st.write(row['Contenido'])
            if pd.notna(row['Destocado']) if 'Destocado' in row else False: # Manejo de errores de tipeo
                st.info(row['Destocado'])
            elif 'Destacado' in row:
                st.info(row['Destacado'])
else:
    st.warning(f"🚧 El archivo `{file_name}` aún no ha sido creado en la carpeta `data/{folder}/` de GitHub.")
    st.info("Subí el archivo a tu repositorio para que la información aparezca aquí automáticamente.")import streamlit as st
import pandas as pd
import json

# Configuración de página
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# Función para cargar la configuración del menú desde GitHub/Local
def load_menu_config():
    with open('menu_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

menu_config = load_menu_config()
df = pd.read_csv('data.csv')

# --- SECCIÓN: MENÚ LATERAL ---
with st.sidebar:
    st.image(menu_config['logo_url'], use_container_width=True)
    st.divider()
    
    st.subheader("📍 Seleccioná tu Destino")
    nombres_destinos = [d['nombre'] for d in menu_config['destinos']]
    destino_seleccionado = st.selectbox("Destino", nombres_destinos)
    
    st.subheader("📂 Menú de Opciones")
    # Obtener secciones dinámicamente del JSON para el destino elegido
    config_destino = next(d for d in menu_config['destinos'] if d['nombre'] == destino_seleccionado)
    seccion_seleccionada = st.radio("Navegar a:", config_destino['secciones'])
    
    st.divider()
    st.caption("Serrano Turismo - 29 años de trayectoria")

# --- SECCIÓN: CONTENIDO PRINCIPAL ---
info = df[df['Destino'] == destino_seleccionado].iloc[0]

if seccion_seleccionada == "Inicio":
    st.title(f"¡Bienvenidos a la Experiencia {destino_seleccionado}!")
    st.image(info['Imagen_URL'], use_container_width=True)
    st.markdown(f"### Una aventura pensada para vos.")
    st.write("Seleccioná las pestañas del menú lateral para conocer más sobre nuestro servicio exclusivo.")

elif seccion_seleccionada == "Hotelería":
    st.header(f"🏨 Hotelería Exclusiva")
    st.subheader(info['Hotel_Nombre'])
    st.write(info['Hotel_Info'])
    st.info("💡 Recordá: Nuestros hoteles son exclusivos para pasajeros de Serrano.")

elif seccion_seleccionada == "Staff y Valores":
    st.header("👨‍🏫 Nuestro Equipo Profesional")
    st.success(f"**Coordinación:** {info['Staff_Valor']}")
    st.header("🍕 Sistema Alimentación")
    st.info(f"**All Inclusive:** {info['All_Inclusive']}")

elif seccion_seleccionada == "Tarifas y Promos":
    st.header("💰 Tarifas y Beneficios Especiales")
    st.warning(f"🔥 **PROMOCIÓN ACTUAL:** {info['Promo']}")
    st.write("Consultá con nuestros asesores por planes de pago personalizados y liberados.")

