import streamlit as st

def render_transporte(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🚌 TRANSPORTE A {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # --- LÓGICA POR DESTINO ---
    if "Villa Carlos Paz" in destino:
        st.subheader("✈️ Opción Aérea")
        st.write("✈️ **Aerolíneas Argentinas:** Optimizamos tu tiempo con cupos confirmados en nuestra aerolínea de bandera.")
        st.write("• Incluye traslados exclusivos aeropuerto-hotel-aeropuerto.")
        
        st.divider()
        
        st.subheader("🚍 Opción Terrestre")
        st.markdown("""
        * **Buses de última generación.**
        * **Empresas de transporte Charter.**
        * **Mismo bus a disposición del grupo durante todos los días del viaje.**
        """)

    else: # SAN PEDRO
        st.subheader("🚍 Transporte Terrestre")
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
        st.write("• Control de velocidad reglamentado")
        
    with col2:
        st.markdown("🛋️ **Confort**")
        st.write("• Aire acondicionado y calefacción")
        st.write("• Pantallas LED y sonido central")
        st.write("• Toilette a bordo")
        st.write("• Butacas reclinables de alta gama")

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 Todas nuestras unidades pasan por rigurosos controles técnicos antes de cada salida para garantizar un viaje seguro.")
