import streamlit as st
import pandas as pd
import json

# Configuración inicial
st.set_page_config(page_title="Serrano Turismo - Clientes", layout="wide")

# Cargar configuración del menú
with open('menu_data.json', 'r') as f:
    menu_config = json.load(f)

# --- SECCIÓN 1: MENÚ LATERAL (SIDEBAR) ---
with st.sidebar:
    st.image(menu_config['logo_url'], use_container_width=True)
    st.divider()
    
    st.subheader("📍 Seleccioná tu Viaje")
    destino_nombres = [d['nombre'] for d in menu_config['destinos']]
    destino_elegido = st.selectbox("Destino", destino_nombres)
    
    st.subheader("📂 Información")
    # Buscamos las secciones del destino elegido en el JSON
    secciones = next(d['secciones'] for d in menu_config['destinos'] if d['nombre'] == destino_elegido)
    seccion_elegida = st.radio("Ver detalles de:", secciones)

# --- SECCIÓN 2 Y 3: CONTENIDO PRINCIPAL ---
df = pd.read_csv('data.csv')
info = df[df['Destino'] == destino_elegido].iloc[0]

st.title(f"Experiencia {destino_elegido}")

if seccion_elegida == "General":
    st.header("¡Bienvenidos a la aventura!")
    st.image(info['Imagen_URL'], use_container_width=True)
    st.write("Explorá las opciones en el menú de la izquierda para conocer cada detalle.")

elif seccion_elegida == "Hotelería":
    st.header("🏨 Nuestra Hotelería")
    st.subheader(info['Hotel_Nombre'])
    st.write(info['Hotel_Info'])
    # Aquí podrías agregar más fotos si sumamos columnas al CSV

elif seccion_elegida == "Staff y Valores":
    st.header("👨‍🏫 Profesionales a cargo")
    st.success(info['Staff_Valor'])
    st.info("🍴 **All Inclusive:** " + info['All_Inclusive'])

elif seccion_elegida == "Tarifas y Promos":
    st.header("💰 Tarifas y Beneficios")
    st.warning(f"🔥 **PROMO:** {info['Promo']}")
    st.write("Consultá por nuestros planes de pago con cuponera y beneficios por cantidad de pasajeros.")

st.sidebar.divider()
st.sidebar.caption("Serrano Turismo - 29 años de trayectoria")
