import streamlit as st

def render_seguro(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🏥 ASISTENCIA Y SEGURO MÉDICO</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # --- ENCABEZADO: RESPALDO ---
    st.markdown("### 🛡️ Respaldo y Cobertura Nacional")
    st.write("Trabajamos con las empresas más importantes del país para garantizar una respuesta inmediata y eficaz en todo momento.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.info("🏢 **Aseguradora:** San Cristóbal Seguros.")
        st.info("🩺 **Prestador Médico:** Assistravel.")

    with col2:
        st.success("👨‍⚕️ **Médico permanente:** A disposición las 24 hs en el hotel.")
        st.success("💊 **Medicamentos en mano:** Respuesta eficaz sin demoras.")

    st.markdown("---")

    # --- DETALLES DE COBERTURA ---
    st.markdown("### 📋 Alcance de la Cobertura Total")
    st.write("La cobertura es inmediata y permanente desde el inicio hasta el fin del tour, incluyendo tramos de ruta y seguimiento post-viaje.")

    # Usamos una lista de checks para que sea fácil de leer
    cobertura_html = """
    <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
        <ul style='list-style-type: none; padding-left: 0;'>
            <li>✅ <b>Traslados:</b> Terrestres y aéreos (regulares y sanitarios).</li>
            <li>✅ <b>Atención Médica:</b> Internaciones, cirugías mayor y menor.</li>
            <li>✅ <b>Insumos:</b> Material descartable, rayos, yesos y odontología.</li>
            <li>✅ <b>Medicamentos:</b> Incluidos en la atención inmediata.</li>
            <li>✅ <b>Preexistencias:</b> Cobertura de agudizaciones de cuadros previos.</li>
            <li>✅ <b>Seguimiento:</b> Asistencia post-viaje hasta el alta médica definitiva.</li>
        </ul>
    </div>
    """
    st.markdown(cobertura_html, unsafe_allow_html=True)

    st.markdown("---")

    # --- TECNOLOGÍA Y RED ---
    col_a, col_b = st.columns([1.5, 1])

    with col_a:
        st.markdown("### 📱 Tecnología de Vanguardia")
        st.write("**VIAXLAB APP:** Todos nuestros pasajeros están identificados con una pulsera de seguimiento que contiene su ficha médica digital para una atención precisa y rápida.")

    with col_b:
        st.markdown("### 🏥 Red Sanitaria")
        st.write("Contamos con más de **45 Clínicas y Sanatorios** de alta complejidad en todo el trayecto y destino.")

    st.warning("⚠️ **Dato clave:** La cobertura opera con el sistema de 'medicamentos en mano', lo que significa que el pasajero recibe el tratamiento de forma inmediata sin necesidad de trámites extras.")
