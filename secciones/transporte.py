import streamlit as st
import os

def render_transporte(destino):
    # Título principal con estilo
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🚌 TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Rutas de imágenes
    img_micro_local = "assets/micros.png" 
    img_avion = "https://images.unsplash.com/photo-1436491865332-7a61a109c0f3?auto=format&fit=crop&q=80&w=1000"

    # --- CASO 1: VILLA CARLOS PAZ (Avión + Micro) ---
    if "Villa Carlos Paz" in destino:
        # SECCIÓN AÉREA
        st.subheader("✈️ Opción Aérea: Aerolíneas Argentinas")
        st.image(img_avion, caption="Vuelos exclusivos para Serrano Turismo", use_container_width=True)
        st.write("Optimizamos tu tiempo con cupos confirmados en nuestra aerolínea de bandera.")
        
        st.divider()
        
        # SECCIÓN TERRESTRE
        st.subheader("🚍 Opción Terrestre")
        
        # Verificamos si la imagen existe en la carpeta assets
        if os.path.exists(img_micro_local):
            st.image(img_micro_local, caption="Nuestras unidades de Serrano Turismo", use_container_width=True)
            # WIDGET DE NORMATIVA (Justo debajo de la foto)
            st.info("ℹ️ Toda nuestra flota cumple estrictamente con las normativas de la CNRT.")
        else:
            st.error(f"⚠️ No se encontró el archivo en: {img_micro_local}. Verificá el nombre del archivo.")
            
        st.write(f"Nuestras unidades de **Serrano Turismo** te llevan a **{destino}** recorriendo los mejores caminos cordobeses durante el día, para que no te pierdas nada del paisaje.")

        # Detalles del servicio
        st.markdown("### ✨ Características de nuestro servicio:")
        st.markdown("""
        * ✅ **Buses de última generación:** Unidades modernas con máximo confort.
        * ✅ **Empresas de transporte Charter:** Seguridad y exclusividad garantizada.
        * ✅ **Exclusividad:** El mismo bus queda a disposición del grupo durante todos los días del viaje para los traslados a excursiones.
        """)

    # --- CASO 2: SAN PEDRO (O cualquier otro destino) ---
    elif "San Pedro" in destino:
        st.subheader("🚍 Transporte Terrestre Exclusivo")
        
        if os.path.exists(img_micro_local):
            st.image(img_micro_local, caption="Unidades equipadas para tu confort", use_container_width=True)
            # WIDGET DE NORMATIVA (Repetido aquí para este destino)
            st.info("ℹ️ Toda nuestra flota cumple estrictamente con las normativas de la CNRT.")
            
        st.write(f"Viajá con la tranquilidad de **Serrano Turismo**. Traslados directos a **{destino}** con coordinación permanente.")
        
        st.markdown("""
        * **Unidades con Mix de asientos (Semicama/Cama).**
        * **Aire acondicionado y calefacción.**
        * **Coordinadores a bordo.**
        """)
        
