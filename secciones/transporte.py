import streamlit as st
import os

def render_transporte(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🚌 TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Rutas de las imágenes
    # Usamos os.path.join para que funcione bien en cualquier servidor
    ruta_base = os.path.dirname(__file__) # Directorio de 'secciones'
    img_micro = os.path.join(ruta_base, "..", "assets", "micro_serrano_caratula.jpg")
    img_avion = "http://googleusercontent.com/image_collection/image_retrieval/820812993248442781_0"

    # --- LÓGICA POR DESTINO ---
    if "Villa Carlos Paz" in destino:
        st.subheader("✈️ Opción Aérea")
        st.image(img_avion, caption="Vuelos con Aerolíneas Argentinas", use_container_width=True)
        st.divider()
        
        st.subheader("🚍 Opción Terrestre")
        # VERIFICACIÓN DE SEGURIDAD PARA LA IMAGEN LOCAL
        if os.path.exists(img_micro):
            st.image(img_micro, caption="Nuestras unidades de última generación", use_container_width=True)
        else:
            st.warning(f"⚠️ No se encontró la imagen en: {img_micro}. Verificá que el archivo esté en la carpeta 'assets'.")

    else: # SAN PEDRO
        st.subheader("🚍 Transporte Terrestre")
        if os.path.exists(img_micro):
            st.image(img_micro, caption="Unidad habilitada por CNRT", use_container_width=True)
        else:
            st.warning("⚠️ Imagen del micro no encontrada en la carpeta 'assets'.")

    # ... (resto del código de seguridad y confort igual)
