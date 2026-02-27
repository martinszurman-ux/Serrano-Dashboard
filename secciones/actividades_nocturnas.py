import streamlit as st

def render_nocturnas(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🌙 ACTIVIDADES NOCTURNAS EN {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    if "Villa Carlos Paz" in destino:
        st.markdown("### 🕺 Diversión y Eventos Exclusivos")
        st.write("Cada noche una temática diferente en los mejores complejos de la Villa.")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("🎭 **NOCHE DE DISFRACES**\n\nCreatividad y premios al mejor outfit del grupo.")
            st.info("👕 **FIESTA DE LA REMERA**\n\nEl evento clásico para lucir el diseño del viaje.")
        with col2:
            st.success("🎪 **SHOW DE TALENTOS**\n\nMomento para que cada uno brille en el escenario.")
            st.success("🎡 **PEKOS NOCTURNO**\n\nUna visita especial con juegos y sorpresas.")
        with col3:
            st.warning("🍔 **CENAS TEMÁTICAS**\n\nGastronomía variada con shows en vivo y animación.")
            st.warning("💫 **DESPEDIDA**\n\nCierre emotivo para sellar la experiencia del grupo.")

    elif "San Pedro" in destino:
        st.markdown("### ✨ Noches de Integración y Magia")
        st.write("Momentos diseñados para fortalecer los lazos de amistad y la diversión compartida.")

        col1, col2 = st.columns(2)
        with col1:
            st.error("🎉 **FIESTA DE BIENVENIDA**\n\nRealizaremos una fiesta de disfraces en el complejo **Macoco** (exclusivo para los chicos de Serrano) con juegos, desfiles y concursos.")
            st.success("🧩 **JUEGOS NOCTURNOS**\n\nEn el marco del hotel realizaremos actividades como fiesta de disfraces, búsqueda del tesoro y fiestas temáticas.")
        with col2:
            st.warning("🔥 **CENA DE VELAS Y FOGÓN**\n\nEl grupo se reúne para cerrar la noche con el Fogón y afianzar los lazos de amistad de la primaria, permitiendo la libre expresión y reflexión del viaje.")

    else:
        st.info("La agenda nocturna se confirmará según la disponibilidad de fechas locales.")

    st.markdown("---")
    st.caption("✨ *Todas las actividades nocturnas cuentan con la supervisión de nuestro equipo de animación propia y seguridad.*")
