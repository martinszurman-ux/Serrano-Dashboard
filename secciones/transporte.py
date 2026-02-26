import streamlit as st

def render_transporte(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🚌 TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Definimos las rutas de las imágenes
    img_micro = "assets/micro_serrano_caratula.jpg"
    img_avion = "http://googleusercontent.com/image_collection/image_retrieval/820812993248442781_0"

    # --- CASO 1: VILLA CARLOS PAZ (Ambas opciones juntas) ---
    if "Villa Carlos Paz" in destino:
        st.subheader("✈️ Opción Aérea")
        st.image(img_avion, caption="Vuelos con Aerolíneas Argentinas", use_container_width=True)
        st.write("Contamos con cupos confirmados y traslados exclusivos aeropuerto-hotel-aeropuerto.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.divider()
        
        st.subheader("🚍 Opción Terrestre")
        st.image(img_micro, caption="Nuestras unidades de última generación", use_container_width=True)
        st.write("Unidades equipadas con el máximo confort para el viaje a las sierras.")

    # --- CASO 2: SAN PEDRO (Solo Micro) ---
    else:
        st.subheader("🚍 Transporte Terrestre")
        st.image(img_micro, caption="Unidad habilitada por CNRT", use_container_width=True)
        st.write("Viajá seguro a San Pedro en nuestras unidades exclusivas con doble chofer profesional.")

    # --- INFORMACIÓN COMÚN ---
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ **Seguridad:** Seguimiento GPS 24hs y cinturones inerciales.")
    with col2:
        st.success("🛋️ **Confort:** Aire acondicionado, calefacción y toilette a bordo.")

    st.info(f"💡 Todas las opciones de transporte para **{destino}** cumplen con las normativas vigentes para garantizar un viaje placentero.")
