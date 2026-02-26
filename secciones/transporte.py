import streamlit as st
import os

def render_transporte(destino):
    # Título principal
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🚌 TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Rutas de imágenes
    img_micro_local = "assets/micros.png" 
    img_avion_local = "assets/AVION.jpg"

    # --- CASO 1: VILLA CARLOS PAZ (Avión + Micro) ---
    if "Villa Carlos Paz" in destino:
        # SECCIÓN AÉREA
        st.subheader("✈️ Opción Aérea: Aerolíneas Argentinas")
        if os.path.exists(img_avion_local):
            # Cambiamos use_container_width por un width fijo para achicarla
            st.image(img_avion_local, caption="Vuelos por la mañana de ida y por la tarde/noche en el regreso", width=650)
        else:
            st.error(f"⚠️ No se encontró: {img_avion_local}")
            
        st.write("Optimizamos el tiempo con vuelos en nuestra aerolínea de bandera.")
        st.divider()
        
        # SECCIÓN TERRESTRE
        st.subheader("🚍 Opción Terrestre")
        if os.path.exists(img_micro_local):
            # Ajustamos también el tamaño del micro
            st.image(img_micro_local, caption="Nuestras unidades de Serrano Turismo", width=650)
            st.info("ℹ️ Toda nuestra flota cumple estrictamente con las normativas de la CNRT.")
        else:
            st.error(f"⚠️ No se encontró: {img_micro_local}")
            
        st.write(f"Nuestras unidades de **Serrano Turismo** te llevan a **{destino}** recorriendo los mejores caminos cordobeses.")

        # Características
        st.markdown("### ✨ Características de nuestro servicio:")
        st.markdown("""
        * ✅ **Buses de última generación:** Unidades modernas con máximo confort.
        * ✅ **Empresas de transporte Charter:** Seguridad y exclusividad garantizada.
        * ✅ **Exclusividad:** El mismo bus queda a disposición del grupo durante todos los días del viaje.
        """)

    # --- CASO 2: SAN PEDRO ---
    elif "San Pedro" in destino:
        st.subheader("🚍 Transporte Terrestre Exclusivo")
        if os.path.exists(img_micro_local):
            st.image(img_micro_local, caption="Unidades equipadas para tu confort", width=650)
            st.info("ℹ️ Toda nuestra flota cumple estrictamente con las normativas de la CNRT.")
            
        st.write(f"Viajá con la tranquilidad de **Serrano Turismo** a **{destino}**.")
        st.markdown("""
        * **Unidades con Mix de asientos (Semicama/Cama).**
        * **Aire acondicionado y calefacción.**
        * **Coordinadores a bordo.**
        """)
