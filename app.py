import streamlit as st

# 1. CONFIGURACIÓN (Debe ser lo primero)
st.set_page_config(page_title="Serrano Turismo", layout="wide")

# 2. IMPORTACIÓN SEGURA
try:
    from secciones.tarifas import render_tarifas
except ImportError as e:
    st.error(f"Error al cargar módulos: {e}")
    st.stop()

# 3. SIDEBAR Y NAVEGACIÓN
with st.sidebar:
    st.image("https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png", use_container_width=True)
    st.divider()
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    opcion = st.radio("📂 Navegación", ["Tarifas", "Solicitud de Adhesión", "Seguro Médico"])

# 4. LÓGICA DE RENDERIZADO
if opcion == "Tarifas":
    render_tarifas(destino)
else:
    st.info(f"La sección '{opcion}' estará disponible próximamente.")
