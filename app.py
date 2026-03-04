import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Serrano Turismo", layout="wide", initial_sidebar_state="collapsed")

# 2. ESTADO
if "nav" not in st.session_state:
    st.session_state.nav = "Home"
if "destino" not in st.session_state:
    st.session_state.destino = None

# Sincronizar parámetros de URL
params = st.query_params
if "nav" in params: st.session_state.nav = params["nav"]
if "destino" in params: st.session_state.destino = params["destino"]

# 3. IMPORTACIONES (Asegúrate de tener estos archivos en /secciones)
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
    st.error(f"Error: {e}")
    st.stop()

# 4. CSS MAESTRO (Ajuste de Logo y Menú Negro)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
    .main .block-container { padding-top: 0rem !important; }
    .stApp { background-color: white !important; }

    /* Barra de Navegación */
    .navbar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 60px; height: 80px; background-color: white;
        border-bottom: 1px solid #f0f0f0; position: fixed;
        top: 0; left: 0; right: 0; z-index: 9999;
    }

    /* Contenedor de Logo para que no sobresalga */
    .logo-box {
        display: flex; align-items: center; height: 100%;
    }
    .logo-box img {
        max-height: 65px; /* Controla que no sobresalga */
        width: auto;
    }

    .nav-links { display: flex; align-items: center; gap: 35px; }

    /* Estilo de los Destinos: Negro, sin subrayado, sin íconos */
    .nav-item {
        color: black !important; 
        text-decoration: none !important; 
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.3s;
    }
    .nav-item:hover { color: #555 !important; }

    /* Dropdown Estilo Wireframe */
    .dropdown { position: relative; display: inline-block; }
    .dropbtn {
        color: black !important; font-size: 14px; font-weight: 700;
        text-decoration: none !important; border: none; background: none;
        cursor: pointer; text-transform: uppercase;
    }
    .dropdown-content {
        display: none; position: absolute; background-color: white;
        min-width: 240px; box-shadow: 0px 8px 16px rgba(0,0,0,0.1);
        z-index: 1; border-radius: 8px; border: 1px solid #f0f0f0; top: 50px;
    }
    .dropdown-content a {
        color: #444; padding: 12px 20px; text-decoration: none;
        display: block; font-size: 13px; text-transform: none;
    }
    .dropdown-content a:hover { background-color: #f8f9fa; color: #000; }
    .dropdown:hover .dropdown-content { display: block; }

    .sigla-badge {
        background: #000; color: #fff; padding: 4px 10px;
        border-radius: 4px; font-weight: bold; font-size: 12px;
    }

    .content-wrapper { margin-top: 100px; padding: 0 5%; }
    </style>
""", unsafe_allow_html=True)

# 5. RENDERIZADO DEL NAVBAR
logo_url = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"
dest = st.session_state.destino
sigla = "CP" if dest == "Villa Carlos Paz" else "SP" if dest == "San Pedro" else ""

if not dest:
    # MENÚ INICIAL: Logo y Destinos en Negro
    nav_html = f"""
    <div class="navbar">
        <div class="logo-box">
            <a href="/?nav=Home" target="_self"><img src="{logo_url}"></a>
        </div>
        <div class="nav-links">
            <a href="/?nav=Home&destino=San+Pedro" class="nav-item" target="_self">SAN PEDRO</a>
            <a href="/?nav=Home&destino=Villa+Carlos+Paz" class="nav-item" target="_self">CARLOS PAZ</a>
        </div>
        <div style="width:110px;"></div>
    </div>
    """
else:
    # MENÚ POST-SELECCIÓN
    nav_html = f"""
    <div class="navbar">
        <div class="logo-box">
            <a href="/?nav=Home" target="_self"><img src="{logo_url}"></a>
        </div>
        <div class="nav-links">
            <a href="/?nav=Home" class="nav-item" target="_self">HOME</a>
            <div class="dropdown">
                <button class="dropbtn">CONOCÉ TU VIAJE DE EGRESADOS ▼</button>
                <div class="dropdown-content">
                    <a href="/?nav=Transporte&destino={dest}" target="_self">Transporte</a>
                    <a href="/?nav=Hoteleria&destino={dest}" target="_self">Hotelería</a>
                    <a href="/?nav=Comidas&destino={dest}" target="_self">Comidas</a>
                    <a href="/?nav=Excursiones&destino={dest}" target="_self">Excursiones</a>
                    <a href="/?nav=Actividades&destino={dest}" target="_self">Actividades</a>
                    <a href="/?nav=Seguro&destino={dest}" target="_self">Seguro/Coordinación</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">ARMÁ TU VIAJE DE EGRESADOS ▼</button>
                <div class="dropdown-content">
                    <a href="/?nav=Tarifas&destino={dest}" target="_self">Tarifas</a>
                    <a href="/?nav=Adhesion&destino={dest}" target="_self">Ficha de Adhesión</a>
                </div>
            </div>
            <div class="sigla-badge">{sigla}</div>
        </div>
        <div style="width:100px;"></div>
    </div>
    """

st.markdown(nav_html, unsafe_allow_html=True)

# 6. CONTENIDO
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
n = st.session_state.nav
if n == "Home": render_landing()
elif n == "Transporte": render_transporte(dest)
elif n == "Hoteleria": render_hoteleria(dest)
elif n == "Comidas": render_comidas(dest)
elif n == "Excursiones": render_excursiones(dest)
elif n == "Actividades": render_nocturnas(dest)
elif n == "Seguro": render_seguro(dest)
elif n == "Tarifas": render_tarifas(dest)
elif n == "Adhesion": render_adhesion(logo_url)
st.markdown('</div>', unsafe_allow_html=True)
