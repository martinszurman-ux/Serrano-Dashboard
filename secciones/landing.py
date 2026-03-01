import streamlit as st

def render_landing():
    # Estilo de bienvenida
    st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h1 style="color: #2c2c2c; font-size: 3rem; margin-bottom: 0;">¡Bienvenidos a Serrano Turismo!</h1>
            <p style="color: #666; font-size: 1.2rem;">Tu aventura educativa comienza aquí.</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Layout de presentación
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("🌟 Experiencias Inolvidables")
        st.write("""
            En **Serrano Turismo**, nos especializamos en crear viajes que combinan 
            aprendizaje, seguridad y diversión. Con más de 20 años de trayectoria, 
            acompañamos a instituciones educativas en la formación de recuerdos 
            que duran toda la vida.
        """)
        st.info("👈 Utilizá el menú lateral para explorar los detalles de tu próximo viaje.")

    with col2:
        st.subheader("📍 Nuestros Destinos")
        st.write("""
            * **Villa Carlos Paz:** Naturaleza, parques temáticos y sierras.
            * **San Pedro:** Historia, río y actividades al aire libre.
        """)
        st.success("Seleccioná tu destino en el menú para ver tarifas y cronogramas específicos.")

    st.divider()

    # Footer de la landing
    st.markdown("""
        <div style="text-align: center; color: #888; font-size: 0.9rem; margin-top: 30px;">
            Hacé clic en <b>Ficha de Adhesión</b> para comenzar tu inscripción formal.
        </div>
    """, unsafe_allow_html=True)
