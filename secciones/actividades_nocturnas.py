import streamlit as st
from utilidades.footer import render_footer

def render_nocturnas(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🌙 ACTIVIDADES NOCTURNAS EN {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    if "Villa Carlos Paz" in destino:
        st.markdown("### 🕺 Diversión y Eventos Exclusivos")
        st.write("Noches diseñadas para crear recuerdos inolvidables con la máxima seguridad.")
        
        # Usamos 2 columnas para que las 5 actividades queden bien distribuidas
        col1, col2 = st.columns(2)

        with col1:
            st.info("🧩 **JUEGOS NOCTURNOS**\n\nEn el marco del hotel realizaremos actividades como fiesta de disfraces, búsqueda del tesoro y fiestas temáticas.")
            st.success("🎭 **MATINÉE SERRANO VIP**\n\nNoche de Fiesta Privada en la Disco **MOLINO ROJO**, contando con la exclusividad del lugar para nuestros pasajeros.")
            st.warning("🔥 **FOGÓN**\n\nEl grupo se reúne para cerrar la noche y afianzar los lazos de amistad de la primaria, permitiendo la libre expresión y reflexión del viaje.")

        with col2:
            st.error("🕯️ **CENA DE VELAS**\n\nNoche especial donde tendremos una cena a la luz de las velas llena de sorpresas y emociones.")
            st.info("💦 **POOL PARTY**\n\nFiesta increíble en pileta climatizada con show de láser y luces en un marco de total diversión y seguridad.")

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

 # --- 5. FOOTER INSTITUCIONAL ---
    # Invocamos la función del archivo utilidades/footer.py
    render_footer()
