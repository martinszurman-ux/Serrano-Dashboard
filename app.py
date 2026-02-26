import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Serrano Turismo - Dashboard de Experiencia", layout="wide")

# Estilo personalizado
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Experiencia Serrano Turismo")
st.subheader("Todo lo que necesitás saber sobre tu próximo gran viaje")

# Cargar datos
df = pd.read_csv('data.csv')

# Selector de Destino
destino_select = st.selectbox("Seleccioná tu destino:", df['Destino'].unique())
datos = df[df['Destino'] == destino_select].iloc[0]

# Diseño en columnas
col1, col2 = st.columns([1, 1])

with col1:
    st.image(datos['Imagen_URL'], use_container_width=True)
    st.info(f"✨ **Promoción Actual:** {datos['Promo_Vigente']}")

with col2:
    st.header(f"🏨 Hotelería en {destino_select}")
    st.write(f"**{datos['Hotel_Nombre']}**")
    st.write(datos['Hotel_Highlight'])
    
    st.header("👨‍🏫 Nuestro Staff")
    st.success(datos['Staff_Valor'])
    
    st.header("🍕 Sistema All Inclusive")
    st.write("Pensión completa, gaseosa libre de primera marca y agua mineral 24hs.")

# Pie de página con contacto
st.divider()
st.write("¿Tenés dudas? Contactanos por WhatsApp o seguinos en la App Viaxlab.")