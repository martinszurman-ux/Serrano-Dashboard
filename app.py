import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Serrano Turismo", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. LÓGICA DE NAVEGACIÓN
query_params = st.query_params
nav_actual = query_params.get("nav", "Home")
dest_actual = query_params.get("destino", None)

st.session_state.nav = nav_actual
st.session_state.destino = dest_actual

# 3. IMPORTACIÓN DE SECCIONES
try:
    from secciones.landing import render_landing
    from secciones.landing_sanpedro import render_landing_sp
    from secciones.landing_carlospaz import render_landing_cp
    from secciones.transporte import render_transporte
    from secciones.hoteleria import render_hoteleria
    from secciones.comidas import render_comidas
    from secciones.excursiones import render_excursiones
    from secciones.actividades_nocturnas import render_nocturnas
    from secciones.seguro import render_seguro
    from secciones.tarifas import render_tarifas
    from secciones.adhesion import render_adhesion
except ImportError as e:
    st.error(f"⚠️ Error de importación: {e}")
    st.stop()

# 4. CSS MAESTRO
try:
    with open("utilidades/desktop.css", "r", encoding="utf-8") as f:
        desktop_style = f.read().strip()
    with open("utilidades/mobile.css", "r", encoding="utf-8") as f:
        mobile_style = f.read().strip()

    css_html = "<style>"
    css_html += '[data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; } '
    css_html += '.stApp { background-color: white !important; } '
    
    # Inyectamos Desktop (> 768px)
    css_html += "@media screen and (min-width: 769px) { " + desktop_style + " } "
    
    # Inyectamos Mobile (<= 768px)
    css_html += "@media screen and (max-width: 768px) { " + mobile_style + " }"
    css_html += "</style>"

    st.markdown(css_html.replace('\n', ' '), unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error crítico en CSS: {e}")

# 5. CONSTRUCCIÓN DEL NAVBAR DINÁMICO
logo_url = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"
sigla = "SP" if dest_actual == "San Pedro" else "CP" if dest_actual == "Villa Carlos Paz" else ""

if not dest_actual:
    # --- CASO HOME: MENU SIEMPRE VISIBLE ---
    links_html = f"""
        <span class="eleccion-texto">Elegí tu destino:</span>
        <a href="./?nav=Home&destino=San+Pedro" class="btn-destino" target="_self">SAN PEDRO</a>
        <a href="./?nav=Home&destino=Villa+Carlos+Paz" class="btn-destino" target="_self">CARLOS PAZ</a>
    """
    navbar_final = f"""
        <div class="navbar">
            <div class="logo-box-home">
                <a href="./?nav=Home" target="_self"><img src="{logo_url}"></a>
            </div>
            <div class="nav-links-visible">
                {links_html}
            </div>
        </div>
    """
else:
    # --- CASO LANDING: MENU COLAPSABLE (Details/Summary) ---
    links_html = f"""
        <a href="./?nav=Home" class="nav-item" target="_self">VOLVER AL HOME</a>
        <div class="dropdown">
            <button class="dropbtn">CONOCÉ TU VIAJE ▼</button>
            <div class="dropdown-content">
                <a href="./?nav=Transporte&destino={dest_actual}" target="_self">Transporte</a>
                <a href="./?nav=Hoteleria&destino={dest_actual}" target="_self">Hotelería</a>
                <a href="./?nav=Comidas&destino={dest_actual}" target="_self">Comidas</a>
                <a href="./?nav=Excursiones&destino={dest_actual}" target="_self">Excursiones</a>
                <a href="./?nav=Actividades&destino={dest_actual}" target="_self">Actividades</a>
                <a href="./?nav=Seguro&destino={dest_actual}" target="_self">Seguro / Coordinación</a>
            </div>
        </div>
        <div class="dropdown">
            <button class="dropbtn">ARMÁ TU VIAJE ▼</button>
            <div class="dropdown-content">
                <a href="./?nav=Tarifas&destino={dest_actual}" target="_self">Tarifas</a>
                <a href="./?nav=Adhesion&destino={dest_actual}" target="_self">Ficha de Adhesión</a>
            </div>
        </div>
    """
    navbar_final = f"""
        <div class="navbar">
            <details class="menu-desplegable">
                <summary class="logo-box-summary">
                    <img src="{logo_url}">
                    <span class="menu-label">MENÚ ☰</span>
                </summary>
                <div class="nav-links-collapsed">
                    {links_html}
                </div>
            </details>
        </div>
    """

# Inyección única de la Navbar construida
st.markdown(navbar_final, unsafe_allow_html=True)

# 6. RENDERIZADO DE CONTENIDO
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

if nav_actual == "Home":
    if dest_actual == "San Pedro":
        render_landing_sp()
    elif dest_actual == "Villa Carlos Paz":
        render_landing_cp()
    else:
        render_landing()

elif nav_actual == "Transporte": render_transporte(dest_actual)
elif nav_actual == "Hoteleria": render_hoteleria(dest_actual)
elif nav_actual == "Comidas": render_comidas(dest_actual)
elif nav_actual == "Excursiones": render_excursiones(dest_actual)
elif nav_actual == "Actividades": render_nocturnas(dest_actual)
elif nav_actual == "Seguro": render_seguro(dest_actual)
elif nav_actual == "Tarifas": render_tarifas(dest_actual)
elif nav_actual == "Adhesion": render_adhesion(logo_url)

st.markdown('</div>', unsafe_allow_html=True)
