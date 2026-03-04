import streamlit as st

# 1. CONFIGURACIÓN (Debe ser lo primero)
st.set_page_config(page_title="Serrano Turismo", layout="wide", initial_sidebar_state="collapsed")

# 2. ESTADO DE LA APP (Memoria de navegación)
if "nav" not in st.session_state:
    st.session_state.nav = "Home"
if "destino" not in st.session_state:
    st.session_state.destino = None

# 3. IMPORTACIONES
try:
    from secciones.landing import render_landing
    from secciones.transporte import render_transporte
    from secciones.hoteleria import render_hoteleria
    from secciones.comidas import render_comidas
    from secciones.excursiones import render_excursiones
    from secciones.actividades_nocturnas import render_nocturnas
    from secciones.seguro import render_seguro
    from secciones.tarifas import render_tarifas
    from secciones.adhesion import render_adhesion
    from secciones.admin import render_admin
except ImportError as e:
    st.error(f"Error cargando secciones: {e}")
    st.stop()

# 4. CSS PARA LIMPIAR LA INTERFAZ Y ESTILIZAR EL MENÚ
st.markdown("""
    <style>
    /* Ocultar basura de Streamlit */
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
    .main .block-container { padding-top: 1rem !important; }
    
    /* Estilo de los botones del menú superior */
    div[data-testid="column"] button {
        background-color: transparent !important;
        border: none !important;
        font-weight: 600 !important;
        color: #333 !important;
        font-size: 16px !important;
    }
    div[data-testid="column"] button:hover {
        color: #007bff !important;
        text-decoration: underline !important;
    }
    
    /* Sigla del destino elegido */
    .badge {
        background-color: #000; color: #fff;
        padding: 5px 12px; border-radius: 5px;
        font-weight: bold; font-size: 14px;
        display: inline-block; margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# 5. NAVBAR SUPERIOR (Usando columnas de Streamlit para que no falle el clic)
# Creamos una fila fija arriba
logo_url = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# Definimos cuántas columnas necesitamos según si hay destino o no
if st.session_state.destino:
    # Si hay destino, mostramos Home + Conoce + Arma + Sigla
    c1, c2, c3, c4, c5, c6 = st.columns([1, 1, 2, 2, 0.5, 1])
    with c1:
        st.image(logo_url, width=100)
    with c2:
        if st.button("Home"):
            st.session_state.nav = "Home"
            st.session_state.destino = None
            st.rerun()
    with c3:
        # Simplificamos a un Selectbox para "Conoce tu viaje" para evitar dropdowns rotos
        opcion_conoce = st.selectbox("", ["Conoce tu viaje...", "🚌 Transporte", "🏨 Hotelería", "🍽️ Comidas", "🏞️ Excursiones", "🌙 Actividades", "🏥 Seguro"], label_visibility="collapsed")
        if opcion_conoce != "Conoce tu viaje...":
            mapa = {"🚌 Transporte": "Transporte", "🏨 Hotelería": "Hoteleria", "🍽️ Comidas": "Comidas", "🏞️ Excursiones": "Excursiones", "🌙 Actividades": "Actividades", "🏥 Seguro": "Seguro"}
            st.session_state.nav = mapa[opcion_conoce]
            st.rerun()
    with c4:
        opcion_arma = st.selectbox("", ["Arma tu viaje...", "💰 Tarifas", "📝 Adhesión"], label_visibility="collapsed")
        if opcion_arma != "Arma tu viaje...":
            mapa_arma = {"💰 Tarifas": "Tarifas", "📝 Adhesión": "Adhesion"}
            st.session_state.nav = mapa_arma[opcion_arma]
            st.rerun()
    with c5:
        sigla = "CP" if st.session_state.destino == "Villa Carlos Paz" else "SP"
        st.markdown(f'<div class="badge">{sigla}</div>', unsafe_allow_html=True)
else:
    # Si NO hay destino, solo Logo y Home
    c1, c2, c3 = st.columns([1, 1, 8])
    with c1:
        st.image(logo_url, width=100)
    with c2:
        if st.button("Home"):
            st.session_state.nav = "Home"
            st.session_state.destino = None
            st.rerun()

st.divider()

# 6. LÓGICA DE RENDERIZADO DE CONTENIDO
dest = st.session_state.destino
pantalla = st.session_state.nav

if pantalla == "Home" or dest is None:
    render_landing() # Aquí es donde el usuario elige CP o SP
elif pantalla == "Transporte":
    render_transporte(dest)
elif pantalla == "Hoteleria":
    render_hoteleria(dest)
elif pantalla == "Comidas":
    render_comidas(dest)
elif pantalla == "Excursiones":
    render_excursiones(dest)
elif pantalla == "Actividades":
    render_nocturnas(dest)
elif pantalla == "Seguro":
    render_seguro(dest)
elif pantalla == "Tarifas":
    render_tarifas(dest)
elif pantalla == "Adhesion":
    render_adhesion(logo_url)
elif pantalla == "Admin":
    render_admin()
