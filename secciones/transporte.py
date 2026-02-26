import streamlit as st

def render_transporte(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🚌 TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # ENLACES DE IMÁGENES (Carga Directa)
    # He actualizado los enlaces para asegurar que se vean en Streamlit Cloud
    img_micro = "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&q=80&w=1000"
    img_avion = "https://images.unsplash.com/photo-1436491865332-7a61a109c0f3?auto=format&fit=crop&q=80&w=1000"

    # --- CASO 1: VILLA CARLOS PAZ (Avión + Micro) ---
    if "Villa Carlos Paz" in destino:
        st.subheader("✈️ Opción Aérea: Aerolíneas Argentinas")
        st.image(img_avion, caption="Vuelos exclusivos para Serrano Turismo", use_container_width=True)
        st.write("Optimizamos tu tiempo con cupos confirmados en nuestra aerolínea de bandera.")
        
        st.divider()
        
        st.subheader("🚍 Opción Terrestre")
        st.image(img_micro, caption="Unidades de Serrano Turismo", use_container_width=True)
        
        st.markdown("""
        * **Buses de última generación.**
        * **Empresas de transporte Charter.**
        * **Mismo bus a disposición del grupo durante todos los días del viaje.**
        """)

    # --- CASO 2: SAN PEDRO (Solo Micro) ---
    else:
        st.subheader("🚍 Transporte Terrestre")
        st.image(img_micro, caption="Servicio exclusivo de Serrano Turismo", use_container_width=True)
        
        st.markdown("""
        * **Buses de última generación.**
        * **Empresas de transporte Charter.**
        * **Mismo bus a disposición del grupo durante todos los días del viaje.**
        """)
        st.write(f"Traslados directos a {destino} con unidades habilitadas por la CNRT.")

    # --- CARACTERÍSTICAS TÉCNICAS (SIEMPRE VISIBLES) ---
    st.markdown("---")
    st.markdown("### 🛠️ Equipamiento y Seguridad")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("🔒 **Seguridad**")
        st.write("• Doble chofer profesional")
        st.write("• Seguimiento GPS en tiempo real")
        st.write("• Cinturones de seguridad inerciales")
    with col2:
        st.markdown("🛋️ **Confort**")
        st.write("• Aire acondicionado y calefacción")
        st.write("• Pantallas LED y sonido central")
        st.write("• Toilette a bordo")

    st.info("💡 Todas nuestras unidades pasan por rigurosos controles técnicos antes de cada salida.")
