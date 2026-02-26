import streamlit as st
import os

def render_transporte(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🚌 TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Definimos la ruta de la imagen que subiste
    # os.path.join asegura que funcione tanto en tu PC como en Streamlit Cloud
    ruta_base = os.path.dirname(__file__) # Directorio de 'secciones'
    # La imagen 'micros.png' debe estar en la carpeta 'assets'
    img_micros = os.path.join(ruta_base, "..", "assets", "micros.png") #

    # --- LÓGICA POR DESTINO ---
    if "Villa Carlos Paz" in destino:
        st.subheader("✈️ Opción Aérea: Aerolíneas Argentinas")
        # Aquí usaríamos una imagen genérica o directa de la web
        st.image("https://images.unsplash.com/photo-1436491865332-7a61a109c0f3?auto=format&fit=crop&q=80&w=1000", caption="Vuelos exclusivos para Serrano Turismo", use_container_width=True)
        st.divider()
        
        st.subheader("🚍 Opción Terrestre")
        # VERIFICACIÓN DE SEGURIDAD PARA LA IMAGEN LOCAL
        if os.path.exists(img_micros): #
            # Usamos st.image con un estilo CSS para el marco
            st.markdown(f"""
            <div style="border: 5px solid #1E3A8A; padding: 10px; border-radius: 15px; text-align: center;">
                <img src="https://raw.githubusercontent.com/AI-Hobbyist/serrano-dashboard/main/assets/micros.png" style="max-width: 100%; border-radius: 10px;">
                <p style="margin-top: 10px; color: #1E3A8A; font-weight: bold;">Unidades de Serrano Turismo</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning(f"⚠️ No se encontró la imagen 'micros.png' en la carpeta 'assets'. Verificá que el archivo exista y que el nombre sea correcto.")

        st.markdown("""
        * **Buses de última generación.**
        * **Empresas de transporte Charter.**
        * **Mismo bus a disposición del grupo durante todos los días del viaje.**
        """)

    else: # SAN PEDRO (Solo Micro)
        st.subheader("🚍 Transporte Terrestre")
        if os.path.exists(img_micros): #
            # Usamos st.image con un estilo CSS para el marco
            st.markdown(f"""
            <div style="border: 5px solid #1E3A8A; padding: 10px; border-radius: 15px; text-align: center;">
                <img src="https://raw.githubusercontent.com/AI-Hobbyist/serrano-dashboard/main/assets/micros.png" style="max-width: 100%; border-radius: 10px;">
                <p style="margin-top: 10px; color: #1E3A8A; font-weight: bold;">Servicio exclusivo de Serrano Turismo</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ No se encontró la imagen 'micros.png' en la carpeta 'assets'.")

        st.markdown("""
        * **Buses de última generación.**
        * **Empresas de transporte Charter.**
        * **Mismo bus a disposición del grupo durante todos los días del viaje.**
        """)
        st.write(f"Traslados directos a {destino} con unidades habilitadas por la CNRT.")

    # ... (resto del código de equipamiento y seguridad igual)
