import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(
    page_title="Serrano Turismo", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# 2. IMPORTACIONES
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
    st.error(f"Error de importación: {e}")
    st.stop()

# 3. LÓGICA DE ESTADO (Navegación Interna)
if "nav" not in st.session_state:
    st.session_state.nav = "Home"
if "destino" not in st.session_state:
    st.session_state.destino = None

# Sincronizar con Query Params por si el usuario usa links externos
params = st.query_params
if "nav" in params: st.session_state.nav = params["nav"]
if "destino" in params: st.session_state.destino = params["destino"]

# 4. CSS MAESTRO (Navbar y Estilización de Botones)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
    .main .block-container { padding-top: 0rem !important; }
    .stApp { background-color: white !important; }

    /* Contenedor del Navbar */
    .nav-container {
        position: fixed; top: 0; left: 0; right: 0;
        height: 80px; background: white;
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 50px; border-bottom: 1px solid #eee;
        z-index: 999999; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    /* Forzar que los botones de la barra parezcan links */
    div[data-testid="stHorizontalBlock"] button {
        background: none !important;
        border: none !important;
        color: #333 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 10px !important;
    }
    div[data-testid="stHorizontalBlock"] button:hover {
        color: #007bff !important;
        background: #f8f9fa !important;
    }

    .dest-badge {
        background-color: #333; color: white;
        padding: 4px 12px; border-radius: 6px;
        font-weight: 800; font-size: 14px;
    }

    .content-wrapper { margin-top: 100px; padding: 0 5%; }
    </style>
""", unsafe_allow_html=True)

# 5. NAVBAR CON BOTONES NATIVOS (Para que funcionen siempre)
# Usamos un contenedor de Streamlit para el Navbar
with st.container():
    # Simulamos el Navbar con columnas
    cols = st.columns([1, 4, 1])
    
    with cols[0]:
        # Logo (Si se toca, resetea a Home)
        if st.button("Serrano", key="logo_btn", use_container_width=False):
            st.session_state.nav = "Home"
            st.session_state.destino = None
            st.query_params.clear()
            st.rerun()

    with cols[1]:
        # Botones de navegación central
        inner_cols = st.columns([1, 2, 2, 0.5])
        
        with inner_cols[0]:
            if st.button("Home", key="home_nav"):
                st.session_state.nav = "Home"
                st.session_state.destino = None
                st.query_params.clear()
                st.rerun()
        
        if st.session_state.destino:
            with inner_cols[1]:
                # Como los dropdowns son difíciles en botones nativos, 
                # usaremos un selectbox estilizado o botones directos.
                # Por ahora, para asegurar que ANDE, usemos botones de acceso rápido:
                if st.button("Conocé tu Viaje", key="btn_conoce"):
                    st.session_state.nav = "Transporte"
                    st.rerun()
            with inner_cols[2]:
                if st.button("Armá tu Viaje", key="btn_arma"):
                    st.session_state.nav = "Tarifas"
                    st.rerun()
            with inner_cols[3]:
                sigla = "CP" if st.session_state.destino == "Villa Carlos Paz" else "SP"
                st.markdown(f'<div class="dest-badge">{sigla}</div>', unsafe_allow_html=True)

    with cols[2]:
        # Admin invisible
        if params.get("admin") == "true":
            if st.button(".", key="admin_dot"):
                st.session_state.nav = "Admin"
                st.rerun()

st.divider() # Línea visual bajo el navbar

# 6. RENDERIZADO DE CONTENIDO
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

current_nav = st.session_state.nav
current_dest = st.session_state.destino

if current_nav == "Home" or not current_dest:
    render_landing()
elif current_nav == "Transporte":
    render_transporte(current_dest)
elif current_nav == "Hoteleria":
    render_hoteleria(current_dest)
elif current_nav == "Comidas":
    render_comidas(current_dest)
elif current_nav == "Excursiones":
    render_excursiones(current_dest)
elif current_nav == "Actividades":
    render_nocturnas(current_dest)
elif current_nav == "Seguro":
    render_seguro(current_dest)
elif current_nav == "Tarifas":
    render_tarifas(current_dest)
elif current_nav == "Adhesion":
    render_adhesion(LOGO_URL)
elif current_nav == "Admin":
    render_admin()

st.markdown('</div>', unsafe_allow_html=True)
