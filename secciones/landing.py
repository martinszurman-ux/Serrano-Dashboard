import streamlit as st

def show_landing():
    # --- HERO SECTION ---
    st.markdown("""
        <div style="text-align: center; padding: 2rem 0rem;">
            <h1 style="font-size: 3rem; color: #1E3A8A;">EXPERIENCIAS INOLVIDABLES</h1>
            <p style="font-size: 1.5rem; color: #555;">28 años brindando servicio de excelencia en viajes de egresados y educativos.</p>
        </div>
    """, unsafe_allow_html=True)

    # Imagen principal (puedes cambiar el link por una local)
    st.image("https://serranoturismo.com.ar/images/slider/slide-1.jpg", use_container_width=True)

    st.divider()

    # --- SECCIÓN DE SERVICIOS ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎓 Viajes de Egresados")
        st.write("Especialistas en nivel primario. Destinos exclusivos en Sierras de Córdoba y San Pedro, diseñados para la seguridad y diversión de los más chicos.")
        if st.button("Ver Destinos Egresados"):
            st.session_state.page = "Egresados" # Lógica para navegar

    with col2:
        st.subheader("📚 Viajes Educativos")
        st.write("Programas pedagógicos que transforman el aprendizaje en una aventura. Experiencias adaptadas a cada institución escolar.")
        if st.button("Explorar Programas"):
            st.session_state.page = "Educativos"

    st.divider()

    # --- FORTALEZAS (Basado en la web) ---
    st.header("¿Por qué elegir Serrano Turismo?")
    
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        st.metric(label="Trayectoria", value="28 Años")
        st.caption("Dedicación exclusiva.")
    with f2:
        st.metric(label="Seguridad", value="APP Propia")
        st.caption("Seguimiento en tiempo real.")
    with f3:
        st.metric(label="Pensión", value="Full")
        st.caption("Comida casera y sana.")
    with f4:
        st.metric(label="Atención", value="24hs")
        st.caption("Médica y profesional.")

    # --- CALL TO ACTION ---
    st.info("📍 Ubícanos en Av. Rivadavia 4532, CABA o en Parque Leloir.")
