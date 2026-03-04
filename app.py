import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Debe ser lo primero)
st.set_page_config(
    page_title="Serrano Turismo", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. LÓGICA DE NAVEGACIÓN (Lectura de la URL)
# Usamos query_params para que la navegación sea sólida al refrescar
query_params = st.query_params
nav_actual = query_params.get("nav", "Home")
dest_actual = query_params.get("destino", None)

# Sincronizamos con la sesión interna
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

# 4. CSS MAESTRO (Ajustes de Logo, Menú, Hover y Footer de lado a lado)
st.markdown("""
    <style>
    /* Reset de Streamlit */
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
    
    /* 1. ELIMINAR FRANJA BLANCA FINAL */
    .main .block-container { 
        padding-top: 0rem !important; 
        padding-bottom: 0rem !important; /* Quitamos el espacio de abajo */
        max-width: 100% !important;
    }
    .stApp { background-color: white !important; }

    /* Navbar Fija */
    .navbar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 0 60px; height: 80px; background-color: white;
        border-bottom: 1px solid #f0f0f0; position: fixed;
        top: 0; left: 0; right: 0; z-index: 9999;
    }

    .logo-box img { max-height: 55px; width: auto; }
    .nav-links { display: flex; align-items: center; gap: 35px; }

    .nav-item {
        color: black !important; text-decoration: none !important; 
        font-size: 13px; font-weight: 700; text-transform: uppercase;
        letter-spacing: 0.5px; transition: 0.2s;
    }
    .nav-item:hover { color: #555 !important; }

    /* DROPDOWN */
    .dropdown { position: relative; display: inline-block; }
    .dropbtn {
        color: black !important; font-size: 13px; font-weight: 700;
        text-decoration: none !important; border: none; background: none;
        cursor: pointer; text-transform: uppercase; padding: 30px 0;
    }
    .dropdown-content {
        display: none; position: absolute; background-color: white;
        min-width: 240px; box-shadow: 0px 8px 16px rgba(0,0,0,0.08);
        z-index: 1000; border-radius: 8px; border: 1px solid #f0f0f0; top: 75px;
    }
    .dropdown:hover .dropdown-content { display: block; }
    .dropdown-content a {
        color: #444; padding: 12px 20px; text-decoration: none;
        display: block; font-size: 13px; transition: 0.2s;
    }

    /* Sigla */
    .sigla-badge {
        background: #000; color: #fff; padding: 4px 10px;
        border-radius: 4px; font-weight: bold; font-size: 11px;
    }

    .content-wrapper { margin-top: 100px; padding: 0 5%; }

    /* 2. FOOTER PROPORCIONADO Y DE LADO A LADO */
    .footer-container {
        background-color: #1a1a1a;
        color: #888;
        padding: 30px 10% !important; /* Padding reducido para que no sea tan ancho */
        margin-left: -10vw !important;
        margin-right: -10vw !important;
        margin-bottom: -5rem !important; /* Empuja el footer hacia el final absoluto */
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
    }
    .footer-col h4 { color: white; font-size: 14px; margin-bottom: 10px; }
    .footer-col p { font-size: 12px; margin-bottom: 5px; }
    </style>
""", unsafe_allow_html=True)

# 5. CONSTRUCCIÓN DEL NAVBAR DINÁMICO
logo_url = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"
sigla = "SP" if dest_actual == "San Pedro" else "CP" if dest_actual == "Villa Carlos Paz" else ""

if not dest_actual:
    # Caso A: No hay destino (Menú de Selección)
    links_html = f"""
        <a href="./?nav=Home&destino=San+Pedro" class="nav-item" target="_self">SAN PEDRO</a>
        <a href="./?nav=Home&destino=Villa+Carlos+Paz" class="nav-item" target="_self">CARLOS PAZ</a>
    """
else:
    # Caso B: Destino elegido (Menú Completo)
    links_html = f"""
        <a href="./?nav=Home" class="nav-item" target="_self">HOME</a>
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
        <div class="sigla-badge">{sigla}</div>
    """

# Inyección del Navbar
st.markdown(f"""
    <div class="navbar">
        <div class="logo-box">
            <a href="./?nav=Home" target="_self">
                <img src="{logo_url}">
            </a>
        </div>
        <div class="nav-links">{links_html}</div>
        <div style="width:110px;"></div>
    </div>
""", unsafe_allow_html=True)

# 6. RENDERIZADO DE CONTENIDO SEGÚN LA NAVEGACIÓN
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

