import streamlit as st

def render_nocturnas(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🌙 ACTIVIDADES NOCTURNAS EN {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    if "Villa Carlos Paz" in destino:
        st.markdown("### 🌌 Noches Mágicas y Exclusivas")
        st.write("La diversión no termina cuando cae el sol. Diseñamos cada noche para que sea segura, privada y emocionante.")

        # --- EVENTO 1: JUEGOS ---
        with st.expander("🎭 1. JUEGOS NOCTURNOS Y TEMÁTICOS", expanded=True):
            st.markdown("""
            En el marco del hotel realizaremos actividades recreativas diseñadas por nuestros coordinadores:
            * **Fiesta de disfraces.**
            * **Búsqueda del tesoro nocturna.**
            * **Fiestas temáticas exclusivas.**
            """)

        # --- EVENTO 2: CENA DE VELAS ---
        with st.expander("🕯️ 2. CENA DE VELAS", expanded=True):
            st.markdown("""
            **Una noche especial:** Tendremos una cena a la luz de las velas llena de sorpresas y emociones, pensada para compartir los mejores momentos del viaje en un clima de distinción.
            """)

        # --- EVENTO 3: MOLINO ROJO ---
        st.error("🚀 **MATINÉE SERRANO VIP - EXCLUSIVO**")
        st.markdown("""
        **Noche de Fiesta Privada en la Disco MOLINO ROJO:** Contamos con la **exclusividad total** del lugar para nuestros pasajeros. Una noche de boliche real pero en un entorno 100% controlado y privado.
        """)

        # --- EVENTO 4: POOL PARTY ---
        st.info("💦 **POOL PARTY NOCTURNA**")
        st.markdown("""
        Disfrutaremos de una noche increíble en una **pileta climatizada** con show de láser y luces. Un marco de diversión y seguridad absoluta para vivir una fiesta diferente bajo el agua.
        """)

        # --- EVENTO 5: FOGÓN ---
        with st.expander("🔥 5. EL FOGÓN DE LA AMISTAD", expanded=True):
            st.markdown("""
            El momento más emotivo del viaje. El grupo se reúne para cerrar la experiencia:
            * **Afianzar lazos:** Reflexión sobre la etapa escolar que termina.
            * **Libre expresión:** Cantos, charlas y momentos para compartir lo vivido.
            * **Cierre del viaje:** Un espacio de unión antes del regreso.
            """)

    else:
        st.info("🌙 Las actividades nocturnas de San Pedro incluyen fogones tradicionales y juegos recreativos en el hotel. ¡Consultanos por el cronograma detallado!")

    st.markdown("---")
    st.caption("🛡️ *Todas las actividades nocturnas cuentan con presencia permanente de nuestros coordinadores y seguridad privada.*")
