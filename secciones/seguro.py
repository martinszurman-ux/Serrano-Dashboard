import streamlit as st

def render_seguro(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🏥 ASISTENCIA Y SEGURIDAD TOTAL</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # --- SECCIÓN 1: RESPALDO MÉDICO ---
    st.markdown("### 🛡️ Cobertura Médica Nacional")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("🏢 **Aseguradora:** San Cristóbal Seguros.")
        st.info("🩺 **Prestador:** Assistravel (Inmediata y permanente).")

    with col2:
        st.success("👨‍⚕️ **Médico en Hotel:** Presencia física las 24 hs.")
        st.success("💊 **Medicamentos:** Sistema 'en mano' para respuesta eficaz.")

    # Detalle rápido de cobertura
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; font-size: 0.95rem;'>
        <b>Cobertura Total:</b> Traslados sanitarios, internaciones, cirugías, rayos, odontología, preexistencias y seguimiento post-viaje.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- SECCIÓN 2: EL PLATO FUERTE - VIAXLAB ---
    st.markdown("---")
    st.markdown("### 📱 Tecnología Exclusiva: VIAXLAB APP")
    st.write("Impulsamos la seguridad mediante Inteligencia Artificial para una gestión optimizada en tiempo real.")

    # Destacamos Viaxlab con un diseño especial
    col_v1, col_v2 = st.columns([1, 1.2])

    with col_v1:
        st.image("https://play-lh.googleusercontent.com/9nF_XvI_X_nK7WkYV6XF3Zq9uXv6vW7fJ8X_XvV-XvV_XvV_XvV_XvV_XvV_XvV=w240-h480-rw", width=200, caption="Disponible en App Store y Google Play")
        st.markdown("🔗 **Ficha Médica Digital:** Todos los pasajeros portan una pulsera vinculada a la App.")

    with col_v2:
        st.markdown("""
        #### 🚀 Herramientas de Control y Comunicación:
        * 📍 **Tracking en tiempo real:** Seguimiento preciso de cada grupo y pasajero.
        * 📅 **Itinerario dinámico:** Acceso a horarios y actividades actualizadas al instante.
        * 💬 **Mensajería Directa:** Comunicación constante entre pasajeros, coordinadores y la agencia.
        * 📸 **Galería de Fotos:** Un solo lugar para revivir los momentos del viaje.
        * ⚕️ **Gestión Segura:** Datos médicos y fichas de salud siempre a mano para los profesionales.
        """)

    st.warning("💡 **Seguridad y Control:** Viaxlab permite a nuestros coordinadores ajustar horarios al instante y gestionar grupos grandes con la máxima eficiencia operativa del mercado.")

    st.markdown("---")
    st.caption("🛡️ Serrano Turismo utiliza tecnología de vanguardia para que la única preocupación de los chicos sea disfrutar.")
