import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Descubrí San Pedro", page_icon="📍", layout="wide")

# 2. Estilo CSS para fijar el Header y mejorar el Footer
st.markdown("""
    <style>
    /* Estilo para el Header */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 30px;
    }
    .nav-logo {
        font-size: 24px;
        font-weight: bold;
        color: #2e7d32;
        text-decoration: none;
    }
    /* Estilo para el Footer */
    .footer {
        position: relative;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1b5e20;
        color: white;
        text-align: center;
        padding: 20px 0;
        margin-top: 50px;
        border-radius: 10px 10px 0 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER / MENÚ ---
# Simulamos un menú de navegación
with st.container():
    col_logo, col_nav = st.columns([1, 2])
    with col_logo:
        st.markdown('<a class="nav-logo" href="#">🌿 San Pedro Travel</a>', unsafe_allow_html=True)
    with col_nav:
        # Creamos botones horizontales que funcionen como menú
        sub_col1, sub_col2, sub_col3, sub_col4 = st.columns(4)
        sub_col1.button("Inicio", key="nav_inicio")
        sub_col2.button("Actividades", key="nav_act")
        sub_col3.button("Alojamiento", key="nav_aloj")
        sub_col4.button("Contacto", key="nav_cont")

# --- SECCIÓN HERO ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<h1 style="color: #1b5e20; font-size: 45px;">San Pedro:<br>Tu escapada perfecta.</h1>', unsafe_allow_html=True)
    st.write("""
        Disfrutá de la tranquilidad del río, el aroma de los azahares 
        y la mejor ensaimada del país. Un lugar detenido en el tiempo.
    """)
    st.button("Explorar Destinos Now", key="hero_btn")

with col2:
    try:
        st.image("assets/landing_sanPedro_imagen", use_container_width=True)
    except:
        st.info("🖼️ Espacio para la imagen de San Pedro")

st.divider()

# --- SECCIÓN DETALLES (Contenido breve) ---
st.header("¿Qué hacer en San Pedro?")
c1, c2, c3 = st.columns(3)
with c1:
    st.subheader("🚣 Río")
    st.write("Paseos y pesca.")
with c2:
    st.subheader("🍰 Gourmet")
    st.write("Ensaimadas típicas.")
with c3:
    st.subheader("🏛️ Historia")
    st.write("Vuelta de Obligado.")

st.divider()

# --- FORMULARIO ---
with st.form("contacto"):
    st.write("### Dejanos tu consulta")
    st.text_input("Email")
    st.form_submit_button("Enviar")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        <p>© 2026 Municipalidad de San Pedro - Dirección de Turismo<br>
        📍 Pellegrini 150, San Pedro, Buenos Aires | 📞 +54 3329 42xxxx</p>
        <p>Seguinos en: Instagram | Facebook | Twitter</p>
    </div>
    """, unsafe_allow_html=True)
