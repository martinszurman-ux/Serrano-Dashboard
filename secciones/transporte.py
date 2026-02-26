import streamlit as st

def render_transporte(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🚌 TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # ENLACES DE IMÁGENES (Representativas de alta calidad)
    # He seleccionado una imagen que evoque un micro de Serrano Turismo
    # circulando por una ruta soleada de Córdoba durante el día.
    img_micro = "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&q=80&w=1000"
    img_avion = "https://images.unsplash.com/photo-1436491865332-7a61a109c0f3?auto=format&fit=crop&q=80&w=1000"

    # --- CASO 1: VILLA CARLOS PAZ (Avión + Micro) ---
    if "Villa Carlos Paz" in destino:
        st.subheader("✈️ Opción Aérea: Aerolíneas Argentinas")
        st.image(img_avion, caption="Vuelos exclusivos para Serrano Turismo", use_container_width=True)
        st.write("Optimizamos tu tiempo con cupos confirmados en nuestra aerolínea de bandera.")
        
        st.divider()
        
        st.subheader("🚍 Opción Terrestre")
        # Aquí describimos la escena que querías:
        st.image(img_micro, caption="Disfrutá del paisaje por las sierras de Córdoba", use_container_width=True)
        st.write(f"Nuestras unidades de **Serrano Turismo** te llevan a **{destino}** recorriendo los mejores caminos cordobeses durante el día, para que no te pierdas nada del paisaje.")

        st.markdown("""
        * **Buses de última generación.**
        * **Empresas de transporte Charter.**
        * **Mismo bus a disposición del grupo durante todos los días del viaje.**
        """)

    # ... (resto del código para San Pedro e info técnica igual)
