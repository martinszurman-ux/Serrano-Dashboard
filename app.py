import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Serrano Turismo", layout="wide", initial_sidebar_state="collapsed")

# 2. ESTADO
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
    st.error(f"Error: {e}")
    st.stop()

# 4. CSS PARA EL NAVBAR
st.markdown("""
    <style>
    [data-testid="stHeader"], [data-testid="stSidebar"] { display: none !important; }
    .main .block-container { padding-top: 1rem !important; }
    
    /* Estilo de botones de navegación */
    div[data-testid="column"] button {
        background-color: transparent !important;
        border: 1px solid #eee !important;
        font-weight: 600 !important;
        color: #333 !important;
        width: 100%;
    }
    div[data-testid="column"] button:hover {
        border-color: #007bff !important;
        color: #007bff !important;
    }
    .sigla {
        background: #000; color: #fff; padding: 5px; 
        border-radius: 5px; text-align: center; font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 5. NAVBAR DINÁMICO
logo_url = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# Si NO hay destino elegido, mostramos Logo + San Pedro + Carlos Paz
if not st.session_state.destino:
    c1, c2, c3, c4 = st.columns([2, 2, 2, 4])
    with c1:
        st.image(logo_url, width=120)
    with c2:
        if st.button("📍 SAN PEDRO"):
            st.session_state.destino = "San Pedro"
            st.session_state.nav = "Home"
            st.rerun()
    with c3:
        if st.button("📍 CARLOS PAZ"):
            st.session_state.destino = "Villa Carlos Paz"
            st.session_state.nav = "Home"
            st.rerun()
else:
    # Si YA hay destino, mostramos Logo + Home + Conoce + Arma + Sigla
    c1, c2, c3, c4, c5 = st.columns([1.5, 1, 2.5, 2.5, 0.5])
    with c1:
        st.image(logo_url, width=100)
    with c2:
        if st.button("🏠 Home"):
            st.session_state.destino = None
            st.session_state.nav = "Home"
            st.rerun()
    with c3:
        op_conoce = st.selectbox("Conocé tu viaje", ["Seleccionar...", "🚌 Transporte", "🏨 Hotelería", "🍽️ Comidas", "🏞️ Excursiones", "🌙 Actividades", "🏥 Seguro"], label_visibility="collapsed")
        if op_conoce != "Seleccionar...":
            mapa = {"🚌 Transporte": "Transporte", "🏨 Hotelería": "Hoteleria", "🍽️ Comidas": "Comidas", "🏞️ Excursiones": "Excursiones", "🌙 Actividades": "Actividades", "🏥 Seguro": "Seguro"}
            st.session_state.nav = mapa[op_conoce]
            st.rerun()
    with c4:
        op_arma = st.selectbox("Armá tu viaje", ["Seleccionar...", "💰 Tarifas", "📝 Adhesión"], label_visibility="collapsed")
        if op_arma != "Seleccionar...":
            mapa_arma = {"💰 Tarifas": "Tarifas", "📝 Adhesión": "Adhesion"}
            st.session_state.nav = mapa_arma[op_arma]
            st.rerun()
    with c5:
        sigla = "SP" if st.session_state.destino == "San Pedro" else "CP"
        st.markdown(f'<div class="sigla">{sigla}</div>', unsafe_allow_html=True)

st.divider()

# 6. RENDERIZADO
d = st.session_state.destino
n = st.session_state.nav

if n == "Home": render_landing()
elif n == "Transporte": render_transporte(d)
elif n == "Hoteleria": render_hoteleria(d)
elif n == "Comidas": render_comidas(d)
elif n == "Excursiones": render_excursiones(d)
elif n == "Actividades": render_nocturnas(d)
elif n == "Seguro": render_seguro(d)
elif n == "Tarifas": render_tarifas(d)
elif n == "Adhesion": render_adhesion(logo_url)
elif n == "Admin": render_admin()
