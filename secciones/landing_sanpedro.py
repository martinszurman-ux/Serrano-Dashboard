import streamlit as st

def render_landing_sp():
    # --- Configuración (Solo si se corre solo, si viene de main.py esto se ignora) ---
    # st.set_page_config(page_title="Descubrí San Pedro", page_icon="📍", layout="wide")

    # --- Estilo CSS ---
    st.markdown("""
        <style>
        .hero-text {
            font-size: 45px;
            font-weight: bold;
            color: #1b5e20;
        }
        .footer {
            background-color: #1b5e20;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 50px;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    # --- CONTENIDO DE LA LANDING ---
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<p class="hero-text">San Pedro:<br>Tu escapada perfecta.</p>', unsafe_allow_html=True)
        st.write("Disfrutá del río, los azahares y la mejor ensaimada.")
        st.button("Explorar Destinos", key="btn_sp_hero")

    with col2:
        try:
            st.image("assets/landing_sanPedro_imagen", use_container_width=True)
        except:
            st.info("🖼️ Imagen de San Pedro")

    st.divider()

    # --- SECCIÓN DETALLES ---
    st.header("¿Qué hacer en San Pedro?")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("🚣 Río")
        st.write("Navegación y pesca.")
    with c2:
        st.subheader("🍰 Gourmet")
        st.write("Ensaimadas y asados.")
    with c3:
        st.subheader("🏛️ Historia")
        st.write("Vuelta de Obligado.")

    st.divider()

    # --- FOOTER ---
    st.markdown("""
        <div class="footer">
            <p>© 2026 Municipalidad de San Pedro - Turismo</p>
        </div>
        """, unsafe_allow_html=True)
