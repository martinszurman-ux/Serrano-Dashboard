import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Serrano Turismo", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# URL DEL LOGO
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
    from secciones.admin import render_admin
except ImportError as e:
    st.error(f"Error de importación: {e}")
    st.stop()

# 3. CSS MAESTRO (Navbar Superior y Estética General)
st.markdown("""
    <style>
    /* Ocultar elementos nativos de Streamlit */
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
    .main .block-container { padding-top: 0rem !important; }

    /* Estilo del Navbar */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5rem 5rem;
        background-color: white;
        border-bottom: 1px solid #eeeeee;
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 999999;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .nav-links { display: flex; gap: 20px; }

    /* Dropdown CSS (Al pasar el mouse) */
    .dropdown { position: relative; display: inline-block; }
    
    .dropbtn {
        background-color: transparent;
        color: #333;
        padding: 16px;
        font-size: 15px;
        font-weight: 600;
        border: none;
        cursor: pointer;
        font-family: 'Source Sans Pro', sans-serif;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: white;
        min-width: 240px;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.1);
        z-index: 1;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #f0f0f0;
    }

    .dropdown-content a {
        color: #444;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
        font-size: 14px;
        transition: 0.2s;
    }

    .dropdown-content a:hover {
        background-color: #f8f9fa;
        color: #007bff;
        padding-left: 20px;
    }

    .dropdown:hover .dropdown-content { display: block; }
    .dropdown:hover .dropbtn { color: #007bff; }

    /* Ajuste para que el contenido no quede tapado por el navbar */
    .content-wrapper { margin-top: 100px; padding: 0 5%; }
    
    /* Forzado de Colores Light */
    .stApp { background-color: white !important; }
    </style>
""", unsafe_allow_html=True)

# 4. CAPTURAR NAVEGACIÓN Y DESTINO
# Usamos query_params para saber en qué sección estamos
params = st.query_params
seccion_activa = params.get("nav", "Home")
destino_seleccionado = params.get("destino", "Villa Carlos Paz")

# 5. RENDERIZADO DEL NAVBAR (HTML Puro)
st.markdown(f"""
    <div class="navbar">
        <a href="/?nav=Home" target="_self">
            <img src="{LOGO_URL}" width="100">
        </a>
        <div class="nav-links">
            <div class="dropdown">
                <a href="/?nav=Home" target="_self"><button class="dropbtn">Home</button></a>
            </div>
            <div class="dropdown">
                <button class="dropbtn">Conoce tu viaje de egresados ▼</button>
                <div class="dropdown-content">
                    <a href="/?nav=Transporte" target="_self">🚌 Transporte</a>
                    <a href="/?nav=Hoteleria" target="_self">🏨 Hotelería</a>
                    <a href="/?nav=Comidas" target="_self">🍽️ Comidas</a>
                    <a href="/?nav=Excursiones" target="_self">🏞️ Excursiones</a>
                    <a href="/?nav=Actividades" target="_self">🌙 Actividades</a>
                    <a href="/?nav=Seguro" target="_self">🏥 Seguro/Coordinación</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">Arma tu viaje de egresados ▼</button>
                <div class="dropdown-content">
                    <a href="/?nav=Tarifas" target="_self">💰 Tarifas</a>
                    <a href="/?nav=Adhesion" target="_self">📝 Ficha de Adhesión</a>
                </div>
            </div>
        </div>
        <div style="width:100px;">
            {"<a href='/?nav=Admin' style='text-decoration:none; color:white; font-size:10px;'>.</a>" if params.get("admin") == "true" else ""}
        </div>
    </div>
""", unsafe_allow_html=True)

# 6. RENDERIZADO DE CONTENIDO
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

if seccion_activa == "Home":
    render_landing()
elif seccion_activa == "Transporte":
    render_transporte(destino_seleccionado)
elif seccion_activa == "Hoteleria":
    render_hoteleria(destino_seleccionado)
elif seccion_activa == "Comidas":
    render_comidas(destino_seleccionado)
elif seccion_activa == "Excursiones":
    render_excursiones(destino_seleccionado)
elif seccion_activa == "Actividades":
    render_nocturnas(destino_seleccionado)
elif seccion_activa == "Seguro":
    render_seguro(destino_seleccionado)
elif seccion_activa == "Tarifas":
    render_tarifas(destino_seleccionado)
elif seccion_activa == "Adhesion":
    render_adhesion(LOGO_URL)
elif seccion_activa == "Admin":
    render_admin()

st.markdown('</div>', unsafe_allow_html=True)
