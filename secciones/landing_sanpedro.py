import streamlit as st
import os

def render_landing_sp():
    # --- ESTILO CSS ACTUALIZADO ---
    st.markdown("""
        <style>
        .hero-text {
            font-size: 45px;
            font-weight: bold;
            color: #1b5e20;
            line-height: 1.2;
        }
        /* Estilos para el Footer Unificado */
        .footer-container {
            display: flex;
            justify-content: space-around;
            background-color: #1b5e20; /* Color verde oscuro institucional */
            color: white;
            padding: 40px 20px;
            margin-top: 50px;
            border-radius: 15px 15px 0 0;
            text-align: left;
        }
        .footer-col {
            flex: 1;
            padding: 0 20px;
        }
        .footer-col h4 {
            color: #ffffff;
            margin-bottom: 15px;
            font-size: 1.2rem;
            border-bottom: 2px solid #2e7d32;
            display: inline-block;
        }
        .footer-col p {
            font-size: 0.9rem;
            margin: 5px 0;
            opacity: 0.9;
        }
        </style>
        """, unsafe_allow_html=True)

    # --- CONTENIDO DE LA LANDING ---
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<p class="hero-text">San Pedro:<br>Tu escapada perfecta.</p>', unsafe_allow_html=True)
        st.write("""
            Disfrutá de la tranquilidad del río, el aroma de los azahares 
            y la mejor ensaimada del país. Un lugar detenido en el tiempo.
        """)
        if st.button("Explorar Destinos", key="sp_btn_hero"):
            st.balloons()

    with col2:
        # Intento de carga de imagen con extensión corregida
        ruta_img = "assets/landing_sanPedro_imagen.png" # Ajustar a .png si corresponde
        if os.path.exists(ruta_img):
            st.image(ruta_img, use_container_width=True)
        else:
            st.info("🖼️ [Imagen de San Pedro]")

    st.divider()

    # --- SECCIÓN DETALLES ---
    st.header("¿Qué hacer en San Pedro?")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("🚣 Río y Náutica")
        st.write("Paseos en lancha y kayak.")
    with c2:
        st.subheader("🍰 Gastronomía")
        st.write("Ensaimadas y delicias locales.")
    with c3:
        st.subheader("🏛️ Historia")
        st.write("Museos y Vuelta de Obligado.")

    # --- FOOTER INSTITUCIONAL (Igual a la Home) ---
    st.markdown("""
        <div class="footer-container">
            <div class="footer-col">
                <h4>SERRANO TURISMO</h4>
                <p>© 2026 Todos los derechos reservados.</p>
            </div>
            <div class="footer-col">
                <h4>CONTACTO</h4>
                <p>San Pedro, Buenos Aires</p>
                <p>WhatsApp: 11-4847-6467</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
