import streamlit as st

def render_transporte(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🚌 TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Enlaces directos de la web para evitar errores de archivo
    img_micro_web = "http://googleusercontent.com/image_collection/image_retrieval/3737429268457166555_0"
    img_avion_web = "http://googleusercontent.com/image_collection/image_retrieval/12197398189739676714_0"

    # --- CASO 1: VILLA CARLOS PAZ (Avión + Micro) ---
    if "Villa Carlos Paz" in destino:
        st.subheader("✈️ Opción Aérea: Aerolíneas Argentinas")
        st.image(img_avion_web, caption="Vuelos exclusivos para Serrano Turismo", use_container_width=True)
        st.write("Optimizamos tu tiempo con cupos confirmados en nuestra aerolínea de bandera.")
        
        st.divider()
        
        st.subheader("🚍 Opción Terrestre")
        st.image(img_micro_web, caption="Unidades de última generación", use_container_width=True)
        st.write("Viajá con el máximo confort en unidades equipadas para largas distancias.")

    # --- CASO 2: SAN PEDRO (Solo Micro) ---
    else:
        st.subheader("🚍 Transporte Terrestre")
        st.image(img_micro_web, caption="Servicio exclusivo de Serrano Turismo", use_container_width=True)
        st.write(f"Traslados directos a {destino} con unidades habilitadas por la CNRT.")

    # --- DETALLES DE SERVICIO (SIEMPRE VISIBLES) ---
    st.markdown("---")
    st.markdown("### 🛠️ Equipamiento y Características")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("🔒 **Seguridad y Técnica**")
        st.write("• Doble chofer profesional")
        st.write("• Seguimiento GPS en tiempo real")
        st.write("• Cinturones de seguridad inerciales")
        st.write("• Control de velocidad reglamentado")
        
    with col2:
        st.markdown("🛋️ **Confort a Bordo**")
        st.write("• Aire acondicionado y calefacción")
        st.write("• Pantallas LED y sonido central")
        st.write("• Toilette a bordo")
        st.write("• Butacas reclinables de alta gama")

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 Todas nuestras unidades pasan por rigurosos controles técnicos antes de cada salida para garantizar un viaje seguro.")
