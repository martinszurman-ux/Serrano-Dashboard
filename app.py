import streamlit as st

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# 2. IMPORTACIÓN DE MÓDULOS EXISTENTES
try:
    from secciones.transporte import render_transporte
    from secciones.hoteleria import render_hoteleria
    from secciones.excursiones import render_excursiones
    from secciones.actividades_nocturnas import render_nocturnas
    from secciones.seguro import render_seguro
    from secciones.tarifas import render_tarifas
    from secciones.adhesion import render_adhesion
except ImportError as e:
    st.error(f"Error crítico de importación: {e}")
    st.stop()

# 3. ESTILO DEL BOTÓN DE ADHESIÓN (Gris Mate Profesional)
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background: linear-gradient(145deg, #495057, #343a40) !important;
        color: white !important;
        border: 1px solid #212529 !important;
        border-radius: 10px !important;
        padding: 12px 20px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        width: 100% !important;
        margin-top: 10px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(145deg, #343a40, #212529) !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# 4. SIDEBAR Y NAVEGACIÓN
with st.sidebar:
    st.image("https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png", use_container_width=True)
    st.divider()
    
    destino = st.selectbox("📍 Destino Seleccionado", ["Villa Carlos Paz", "San Pedro"])
    
    # Orden solicitado por el usuario
    opciones_menu = [
        "1. Transporte",
        "2. Hotelería",
        "3. Excursiones",
        "4. Actividades",
        "5. Seguro Médico",
        "6. Tarifas"
    ]
    
    # Radio para las secciones numeradas
    # Usamos un índice en session_state para poder resetearlo desde el botón
    if "nav_index" not in st.session_state:
        st.session_state.nav_index = 0

    seleccion = st.radio("Menú de Navegación", opciones_menu, key="menu_radio")
    
    st.divider()
    
    # Botón de Adhesión al final
    if st.button("📝 Solicitud de Adhesión"):
        st.session_state.go_to_adhesion = True
    else:
        if "go_to_adhesion" not in st.session_state:
            st.session_state.go_to_adhesion = False

# 5. LÓGICA DE RENDERIZADO (Enrutador)
if st.session_state.go_to_adhesion:
    render_adhesion(destino)
    # Botón pequeño para volver al menú si se desea
    if st.button("⬅️ Volver al Menú Principal"):
        st.session_state.go_to_adhesion = False
        st.rerun()

elif seleccion == "1. Transporte":
    render_transporte(destino)

elif seleccion == "2. Hotelería":
    render_hoteleria(destino)

elif seleccion == "3. Excursiones":
    render_excursiones(destino)

elif seleccion == "4. Actividades":
    # Aquí mapeamos al archivo actividades_nocturnas.py
    render_nocturnas(destino)

elif seleccion == "5. Seguro Médico":
    render_seguro(destino)

elif seleccion == "6. Tarifas":
    render_tarifas(destino)
