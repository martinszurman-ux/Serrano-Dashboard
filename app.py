import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Serrano Turismo", 
    layout="wide", 
    initial_sidebar_state="collapsed" # Ocultamos el sidebar nativo
)

# URLs DE RECURSOS (Reemplaza con tus links de GitHub cuando los tengas)
LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# 2. IMPORTACIÓN DE SECCIONES
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
except ImportError as e:
    st.error(f"Error de importación: {e}")
    st.stop()

# 3. CSS PARA EL NAVBAR SUPERIOR (Wireframe style)
st.markdown("""
    <style>
    /* Ocultar elementos nativos */
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
    .main .block-container { padding-top: 0rem !important; }

    /* Estilo del Navbar */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 5rem;
        background-color: white;
        border-bottom: 1px solid #e0e0e0;
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 9999;
    }

    .nav-links { display: flex; gap: 40px; }

    /* Dropdown Logic */
    .dropdown { position: relative; display: inline-block; }
    .dropbtn {
        font-size: 16px; border: none; outline: none;
        color: #333; padding: 14px 16px; background: inherit;
        font-family: inherit; margin: 0; cursor: pointer;
        font-weight: 500;
    }
    .dropdown-content {
        display: none; position: absolute; background-color: #f9f9f9;
        min-width: 200px; box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1; border-radius: 4px;
    }
    .dropdown-content a {
        color: black; padding: 12px 16px; text-decoration: none;
        display: block; text-align: left; font-size: 14px;
    }
    .dropdown-content a:hover { background-color: #f1f1f1; }
    .dropdown:hover .dropdown-content { display: block; }
    .dropdown:hover .dropbtn { color: #007bff; }

    /* Ajuste de contenido para que no quede debajo del navbar */
    .content-wrapper { margin-top: 100px; }
    </style>
""", unsafe_allow_html=True)

# 4. LÓGICA DE NAVEGACIÓN (Session State)
if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Home"

# 5. RENDERIZADO DEL NAVBAR (HTML + Botones invisibles para Streamlit)
# Nota: Streamlit no detecta clics en enlaces <a> fácilmente para cambiar el estado interno,
# por lo que usaremos una combinación de botones o links con parámetros.

with st.container():
    st.markdown(f"""
        <div class="navbar">
            <img src="{LOGO_URL}" width="100">
            <div class="nav-links">
                <div class="dropdown">
                    <button class="dropbtn" onclick="window.location.href='/?nav=Home'">Home</button>
                </div>
                <div class="dropdown">
                    <button class="dropbtn">Conoce tu gira ▼</button>
                    <div class="dropdown-content">
                        <a href="/?nav=Transporte">🚌 Transporte</a>
                        <a href="/?nav=Hoteleria">🏨 Hotelería</a>
                        <a href="/?nav=Comidas">🍽️ Comidas</a>
                        <a href="/?nav=Excursiones">🏞️ Excursiones</a>
                        <a href="/?nav=Actividades">🌙 Actividades</a>
                        <a href="/?nav=Seguro">🏥 Seguro/Coordinación</a>
                    </div>
                </div>
                <div class="dropdown">
                    <button class="dropbtn">Arma tu gira ▼</button>
                    <div class="dropdown-content">
                        <a href="/?nav=Tarifas">💰 Tarifas</a>
                        <a href="/?nav=Adhesion">📝 Ficha de Adhesión</a>
                    </div>
                </div>
            </div>
            <div></div> </div>
    """, unsafe_allow_html=True)

# Capturar navegación desde URL (truco para que los links del Navbar funcionen)
query_nav = st.query_params.get("nav", "Home")
st.session_state.seccion_activa = query_nav

# 6. RENDERIZADO DE CONTENIDO
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Selector de destino (Global para las secciones que lo necesiten)
# Podríamos ponerlo en el navbar o dentro de las secciones.
destino = "Villa Carlos Paz" # Por defecto

if st.session_state.seccion_activa == "Home":
    render_landing()
elif st.session_state.seccion_activa == "Transporte":
    render_transporte(destino)
elif st.session_state.seccion_activa == "Hoteleria":
    render_hoteleria(destino)
elif st.session_state.seccion_activa == "Comidas":
    render_comidas(destino)
elif st.session_state.seccion_activa == "Excursiones":
    render_excursiones(destino)
elif st.session_state.seccion_activa == "Actividades":
    render_nocturnas(destino)
elif st.session_state.seccion_activa == "Seguro":
    render_seguro(destino)
elif st.session_state.seccion_activa == "Tarifas":
    render_tarifas(destino)
elif st.session_state.seccion_activa == "Adhesion":
    render_adhesion(LOGO_URL)

st.markdown('</div>', unsafe_allow_html=True)
