import streamlit as st

def render_transporte(destino):
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚌 LOGÍSTICA Y TRANSPORTE</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Creamos dos solapas para organizar la info
    tab1, tab2 = st.tabs(["🚍 Transporte Terrestre", "✈️ Conexión Aérea"])

    with tab1:
        st.subheader("Unidades de Última Generación")
        col_img_1, col_img_2, col_img_3 = st.columns([1, 4, 1])
        with col_img_2:
            # Usamos la foto del micro que guardaste en assets
            st.image("assets/micro_serrano_caratula.jpg", caption="Unidad de Serrano Turismo", use_container_width=True)
        
        st.write(f"Viajá a **{destino}** con el máximo confort. Nuestras unidades cuentan con doble chofer profesional, habilitación CNRT y seguimiento satelital.")

    with tab2:
        st.subheader("Vuelos Nacionales con Aerolíneas Argentinas")
        
        # Mostramos la imagen del avión
        st.image("http://googleusercontent.com/image_collection/image_retrieval/820812993248442781_0", 
                 caption="Alianza estratégica con nuestra aerolínea de bandera", 
                 use_container_width=True)
        
        st.write(f"""
        Para los contingentes que prefieren optimizar los tiempos de viaje a **{destino}**, 
        contamos con cupos confirmados en **Aerolíneas Argentinas**.
        
        **Beneficios del Servicio Aéreo:**
        * Traslados exclusivos Aeropuerto - Hotel - Aeropuerto.
        * Despacho de equipaje incluido.
        * Coordinación permanente desde el check-in.
        """)
        
        st.info("✈️ **Nota:** Consultá disponibilidad de fechas y tarifas diferenciales para la opción aérea.")

    st.divider()
    st.markdown("### 🛠️ Seguridad Garantizada")
    st.write("Tanto en bus como en avión, todos nuestros pasajeros viajan bajo estrictas normas de seguridad y asistencia permanente.")
