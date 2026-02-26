import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Serrano Turismo", layout="wide")

# 2. IMPORTACIONES
# Intentamos importar cada sección. Si falla, mostramos un aviso claro.
try:
    from secciones.tarifas import render_tarifas
    from secciones.adhesion import render_adhesion
    from secciones.transporte import render_transporte
except ImportError as e:
    st.error(f"Error de importación: {e}. Verificá que los archivos existan en la carpeta 'secciones'.")
    st.stop()

# URL del logo institucional
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# 3. SIDEBAR (Navegación)
with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    
    # Menú con el orden solicitado
    opcion = st.radio("📂 Navegación", [
        "🚌 TRANSPORTE",
        "🏨 HOTELERIA",
        "☀️ EXCURSIONES DE DIA",
        "🌙 ACTIVIDADES NOCTURNAS",
        "🏥 SEGURO MEDICO",
        "💰 TARIFAS Y FORMAS DE PAGO",
        "📋 SOLICITUD DE ADHESION"
    ])

# 4. LÓGICA DE VISUALIZACIÓN
if opcion == "🚌 TRANSPORTE":
    render_transporte(destino)

elif opcion == "💰 TARIFAS Y FORMAS DE PAGO":
    render_tarifas(destino)

elif opcion == "📋 SOLICITUD DE ADHESION":
    render_adhesion(LOGO_URL)

elif opcion == "🏨 HOTELERIA":
    st.title("🏨 Hotelería")
    st.info(f"Próximamente: Detalles de alojamiento en {destino}.")

elif opcion == "🏥 SEGURO MEDICO":
    st.title("🏥 Seguro Médico")
    st.info("Información sobre cobertura médica y asistencia al viajero.")

else:
    st.title(opcion)
    st.info("Esta sección se encuentra en desarrollo.")
