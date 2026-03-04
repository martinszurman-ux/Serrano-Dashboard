import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Serrano Turismo", layout="wide", initial_sidebar_state="collapsed")

# 2. LÓGICA DE ESTADO (Priorizamos limpiar si es HOME)
params = st.query_params
nav_param = params.get("nav", "Home")
dest_param = params.get("destino", None)

# Reset total si el usuario pide ir al Home
if nav_param == "Home":
    st.session_state.nav = "Home"
    st.session_state.destino = None
else:
    st.session_state.nav = nav_param
    st.session_state.destino = dest_param

# 3. IMPORTACIONES
try:
    from secciones.landing import render_landing
    from secciones.landing_sanpedro import render_landing_sp  
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

# 4. CSS MAESTRO (Sin errores de sintaxis)
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
    .main .block-container { padding-top: 0rem !important; }
    .stApp { background-color: white !important; }

    .navbar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 60px; height: 80px; background-color: white;
        border-bottom: 1px solid #f0f0f0; position: fixed;
        top: 0; left: 0; right: 0; z-index: 9999;
    }

    .logo-box img { max-height: 60px; width: auto; }
    .nav-links { display: flex; align-items: center; gap: 35px; }

    .nav-item {
        color: black !important; text-decoration: none !important; 
        font-size: 14px; font-weight: 700; text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* DROPDOWN */
    .dropdown { position: relative; display: inline-block; }
    .dropbtn {
        color: black !important; font-size: 14px; font-weight: 700;
        text-decoration: none !important; border: none; background: none;
        cursor: pointer; text-transform: uppercase; padding: 30px 0;
    }
    .dropdown-content {
        display: none; position: absolute; background-color: white;
        min-width: 240px; box-shadow: 0px 8px 16px rgba(0,0,0,0.1);
        z-index: 1000; border-radius: 8px; border: 1px solid #f0f0f0; top: 70px;
    }
    .dropdown:hover .dropdown-content { display: block; }
    .dropdown-content a {
        color: #444; padding: 12px 20px; text-decoration: none;
        display: block; font-size: 13px;
    }
    .dropdown-content a:hover { background-color: #f8f9fa; color: #000 !important; }

    .sigla-badge {
        background: #000; color: #fff; padding: 4px 10px;
        border-radius: 4px; font-weight: bold; font-size: 12px;
    }
    .content-wrapper { margin-top: 100px; padding: 0 5%; }
    </style>
""", unsafe_allow_html=True)

# 5. CONSTRUCCIÓN DEL NAVBAR (Lógica separada del f-string para evitar errores)
logo_url = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"
dest = st.session_state.destino
sigla = "SP" if dest == "San Pedro" else "CP" if dest == "Villa Carlos Paz" else ""

if not dest:
    links_html = f"""
        <a href="/?nav=Home&destino=San+Pedro" class="nav-item" target="_self">SAN PEDRO</a>
        <a href="/?nav=Home&destino=Villa+Carlos+Paz" class="nav-item" target="_self">CARLOS PAZ</a>
    """
else:
    links_html = f"""
        <a href="/?nav=Home" class="nav-item" target="_self">HOME</a>
        <div class="dropdown">
            <button class="dropbtn">CONOCÉ TU VIAJE ▼</button>
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
            <button class="dropbtn">ARMÁ TU VIAJE ▼</button>
            <div class="dropdown-content">
                <a href="/?nav=Tarifas&destino={dest}" target="_self">Tarifas</a>
                <a href="/?nav=Adhesion&destino={dest}" target="_self">Ficha de Adhesión</a>
            </div>
        </div>
        <div class="sigla-badge">{sigla}</div>
    """

st.markdown(f"""
    <div class="navbar">
        <div class="logo-box"><a href="/?nav=Home" target="_self"><img src="{logo_url}"></a></div>
        <div class="nav-links">{links_html}</div>
        <div style="width:110px;"></div>
    </div>
""", unsafe_allow_html=True)

# 6. RENDERIZADO
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
n = st.session_state.nav

if n == "Home":
    if dest == "San Pedro":
        render_landing_sp()
    else:
        render_landing()
elif n == "Transporte": render_transporte(dest)
elif n == "Hoteleria": render_hoteleria(dest)
elif n == "Comidas": render_comidas(dest)
elif n == "Excursiones": render_excursiones(dest)
elif n == "Actividades": render_nocturnas(dest)
elif n == "Seguro": render_seguro(dest)
elif n == "Tarifas": render_tarifas(dest)
elif n == "Adhesion": render_adhesion(logo_url)
st.markdown('</div>', unsafe_allow_html=True)
