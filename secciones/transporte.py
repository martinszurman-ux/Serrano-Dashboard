import streamlit as st
import os
from utilidades.footer import render_footer

def render_transporte(destino):
    # Lógica para el título dinámico con emojis
    if "Villa Carlos Paz" in destino:
        titulo_emoji = "✈️ 🚌"
    else:
        titulo_emoji = "🚌"

    # Título principal con estilo
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>{titulo_emoji} TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Rutas de imágenes
    img_micro_local = "assets/micros.png" 
    img_avion_local = "assets/AVION.jpg"

    # --- CASO 1: VILLA CARLOS PAZ (Avión + Micro) ---
    if "Villa Carlos Paz" in destino:
        # SECCIÓN AÉREA
        st.subheader("✈️ Opción Aérea: Aerolíneas Argentinas")
        if os.path.exists(img_avion_local):
            st.image(img_avion_local, caption="Vuelos exclusivos para Serrano Turismo", width=650)
        else:
            st.error(f"⚠️ No se encontró: {img_avion_local}")
            
        st.write("Optimizamos tu tiempo con cupos confirmados en nuestra aerolínea de bandera.")
        st.divider()
        
        # SECCIÓN TERRESTRE
        st.subheader("🚍 Opción Terrestre")
        if os.path.exists(img_micro_local):
            st.image(img_micro_local, caption="Nuestras unidades de Serrano Turismo", width=650)
        else:
            st.error(f"⚠️ No se encontró: {img_micro_local}")
            
        st.write(f"Unidades exclusivas para **Serrano Turismo** te llevan a **{destino}** recorriendo los mejores caminos cordobeses.")

        # Características (Igualadas)
        st.markdown("### ✨ Características de nuestro servicio:")
        st.markdown("""
        * ✅ **Buses de última generación de un solo piso:** Unidades modernas con máximo confort.
        * ✅ **Empresas de transporte Charter:** Seguridad y exclusividad garantizada.
        * ✅ **Exclusividad:** El mismo bus queda a disposición del grupo durante todos los días del viaje para los traslados a excursiones.
        """)

    # --- CASO 2: SAN PEDRO ---
    elif "San Pedro" in destino:
        st.subheader("🚍 Transporte Terrestre Exclusivo")
        
        if os.path.exists(img_micro_local):
            st.image(img_micro_local, caption="Unidades equipadas para tu confort", width=650)
        else:
            st.error(f"⚠️ No se encontró: {img_micro_local}")
            
        st.write(f"Viajá con la tranquilidad de **Serrano Turismo**. Traslados directos a **{destino}** con coordinación permanente.")
        
        # Características (Ahora igualadas a Carlos Paz)
        st.markdown("### ✨ Características de nuestro servicio:")
        st.markdown("""
        * ✅ **Buses de última generación:** Unidades modernas con máximo confort.
        * ✅ **Empresas de transporte Charter:** Seguridad y exclusividad garantizada.
        * ✅ **Exclusividad:** El mismo bus queda a disposición del grupo durante todos los días del viaje para los traslados a excursiones.
        """)

    # --- 5. FOOTER INSTITUCIONAL ---
    # Invocamos la función del archivo utilidades/footer.py
    render_footer()
