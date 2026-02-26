import streamlit as st

def render_excursiones(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🏞️ EXCURSIONES EN {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    if "Villa Carlos Paz" in destino:
        st.markdown("### ✨ Nuestro Plan de Actividades Exclusivo")
        st.write("Combinamos aventura, relax y mucha diversión para que cada día sea inolvidable.")
        
        # Diseño en 3 columnas para que entren todas de forma armónica
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("🥾 **MOUNTAIN TREKKING**\n\nExploración por los senderos serranos con las mejores vistas.")
            st.info("🚗 **CITY TOUR**\n\nRecorrido por los puntos emblemáticos y la costanera.")
            st.info("🍩 **FÁBRICA DE ALFAJORES**\n\nVisita técnica y degustación de los clásicos regionales.")

        with col2:
            st.success("🎢 **CRAZY DONKEY**\n\nUn día de pura adrenalina en el parque de aventuras.")
            st.success("💦 **PARQUE ACUÁTICO**\n\nToboganes, piletas y diversión bajo el sol.")
            st.success("🚀 **JUMPING GAMES**\n\nDesafío de altura y saltos en camas elásticas.")

        with col3:
            st.warning("🏖️ **BEACH DAY**\n\nRelax y actividades recreativas a la vera del lago.")
            st.warning("👑 **KING PARK**\n\nEntretenimiento de vanguardia y juegos mecánicos.")
            st.warning("🐒 **COCOGUANA**\n\nParque aéreo y tirolesas en un entorno natural único.")

    else:
        # Espacio para las excursiones de San Pedro cuando las definamos
        st.info("Estamos terminando de coordinar las mejores actividades para San Pedro. ¡Próximamente!")

    # Nota al pie
    st.markdown("---")
    st.caption("⚠️ *El orden de las excursiones está sujeto a condiciones climáticas y logística de la coordinación.*")
