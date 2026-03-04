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

# 3. CAPTURAR ESTADO DE NAVEGACIÓN
# Usamos st.query_params directamente
params = st.query_params
seccion_activa = params.get("nav", "Home")
destino_elegido = params.get("destino", None)

# 4. CSS MAESTRO
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
    .main .block-container { padding-top: 0rem !important; }
    .stApp { background-color: white !important; }

    .navbar {
        display: flex; 
        justify-content: space-between; 
        align-items: center;
        padding: 0.5rem 5rem; 
        background-color: white; 
        border-bottom: 1px solid #eeeeee;
        position: fixed; top: 0; left: 0; right: 0; 
        z-index: 999999; 
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        height: 70px;
    }
    
    .nav-links { 
        display: flex; 
        gap: 10px; 
        align-items: center;
        justify-content: center;
        flex-grow: 1;
    }

    .dest-badge {
        background-color: #2c2c2c; 
        color: white; 
        padding: 4px 10px;
        border-radius: 4px; 
        font-weight: 800; 
        font-size: 14px; 
        margin-left: 15px;
    }

    .dropdown { position: relative; display: inline-block; }
    
    .dropbtn {
        background: transparent; 
        color: #333; 
        padding: 10px 15px;
        font-size: 14px; 
        font-weight: 600; 
        border: none; 
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }
    
    .dropdown-content {
        display: none; 
        position: absolute; 
        background-color: white;
        min-width: 220px; 
        box-shadow: 0px 8px 16px rgba(0,0,0,0.1);
        z-index: 100; 
        border-radius: 8px; 
        border: 1px solid #f0f0f0;
    }
    
    .dropdown-content a {
        color: #444; 
        padding: 12px 16px; 
        text-decoration: none; 
        display: block; 
        font-size: 13px;
    }
    
    .dropdown-content a:hover { background-color: #f8f9fa; color: #007bff; }
    .dropdown:hover .dropdown-content { display: block; }

    .content-wrapper { margin-top: 90px; padding: 0 5%; }
    </style>
""", unsafe_allow_html=True)

# 5. LÓGICA DEL NAVBAR
# Definimos las siglas
sigla = ""
if destino_elegido == "Villa Carlos Paz": sigla = "CP"
elif destino_elegido == "San Pedro": sigla = "SP"

# Construimos el menú dinámico
menu_html = f'<a href="/?nav=Home" class="dropbtn">Home</a>'

if destino_elegido:
    menu_html += f"""
    <div class="dropdown">
        <button class="dropbtn">Conocé tu viaje de egresados ▼</button>
        <div class="dropdown-content">
            <a href="/?nav=Transporte&destino={destino_elegido}" target="_self">🚌 Transporte</a>
            <a href="/?nav=Hoteleria&destino={destino_elegido}" target="_self">🏨 Hotelería</a>
            <a href="/?nav=Comidas&destino={destino_elegido}" target="_self">🍽️ Comidas</a>
            <a href="/?nav=Excursiones&destino={destino_elegido}" target="_self">🏞️ Excursiones</a>
            <a href="/?nav=Actividades&destino={destino_elegido}" target="_self">🌙 Actividades</a>
            <a href="/?nav=Seguro&destino={destino_elegido}" target="_self">🏥 Seguro/Coordinación</a>
        </div>
    </div>
    <div class="dropdown">
        <button class="dropbtn">Armá tu viaje de egresados ▼</button>
        <div class="dropdown-content">
            <a href="/?nav=Tarifas&destino={destino_elegido}" target="_self">💰 Tarifas</a>
            <a href="/?nav=Adhesion&destino={destino_elegido}" target="_self">📝 Ficha de Adhesión</a>
        </div>
    </div>
    <div class="dest-badge">{sigla}</div>
    """

# Renderizado final del Navbar
admin_dot = ""
if params.get("admin") == "true":
    admin_dot = '<a href="/?nav=Admin&admin=true" style="text-decoration:none; color:#eee; font-size:10px;">.</a>'

st.markdown(f"""
    <div class="navbar">
        <div style="width:150px;">
            <a href="/?nav=Home" target="_self"><img src="{LOGO_URL}" width="100"></a>
        </div>
        <div class="nav-links">
            {menu_html}
        </div>
        <div style="width:150px; text-align:right;">
            {admin_dot}
        </div>
    </div>
""", unsafe_allow_html=True)

# 6. RENDERIZADO DE CONTENIDO
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Lógica de renderizado según sección
if seccion_activa == "Home" or not destino_elegido:
    render_landing()
elif seccion_activa == "Transporte":
    render_transporte(destino_elegido)
elif seccion_activa == "Hoteleria":
    render_hoteleria(destino_elegido)
elif seccion_activa == "Comidas":
    render_comidas(destino_elegido)
elif seccion_activa == "Excursiones":
    render_excursiones(destino_elegido)
elif seccion_activa == "Actividades":
    render_nocturnas(destino_elegido)
elif seccion_activa == "Seguro":
    render_seguro(destino_elegido)
elif seccion_activa == "Tarifas":
    render_tarifas(destino_elegido)
elif seccion_activa == "Adhesion":
    render_adhesion(LOGO_URL)
elif seccion_activa == "Admin":
    render_admin()

st.markdown('</div>', unsafe_allow_html=True)
