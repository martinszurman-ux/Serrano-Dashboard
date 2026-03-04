import streamlit as st

def render_landing():
    # URL de la imagen que vas a subir a GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/tu_usuario/tu_repo/main/assets/Landing_image.jpeg"

    # Estilos específicos para la Landing
    st.markdown("""
        <style>
        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            color: #1a1a1a;
            line-height: 1;
            margin-bottom: 10px;
        }
        .hero-subtitle {
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 30px;
        }
        .dest-button {
            background-color: #2c2c2c;
            color: white !important;
            padding: 10px 25px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            margin-right: 10px;
            transition: 0.3s;
        }
        .dest-button:hover {
            background-color: #555;
        }
        .hero-img {
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # Contenedor del Hero (Título + Imagen lateral)
    col_text, col_img = st.columns([1, 1], gap="large")

    with col_text:
        st.markdown("<div style='margin-top: 50px;'>", unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura educativa comienza aquí.</p>', unsafe_allow_html=True)
        
        # Botones de destino que refrescan la página con el parámetro
        c1, c2, c3 = st.columns([1,1,2])
        with c1:
            if st.button("Carlos Paz", use_container_width=True):
                st.query_params["destino"] = "Carlos Paz"
                st.rerun()
        with c2:
            if st.button("San Pedro", use_container_width=True):
                st.query_params["destino"] = "San Pedro"
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col_img:
        # Mostramos la imagen con un tamaño controlado
        st.image(LANDING_IMG, use_container_width=True)

    # Espacio para las siguientes secciones del wireframe
    st.markdown("<br><br>", unsafe_allow_html=True)
