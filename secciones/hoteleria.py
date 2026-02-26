import streamlit as st
import os

def render_hoteleria(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🏨 HOTELERÍA EN {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    ruta_base = "assets/"

    # --- CASO 1: VILLA CARLOS PAZ ---
    if "Villa Carlos Paz" in destino:
        # OPCIÓN 1: HOTEL PARQUE
        st.subheader("🏢 Opción 1: Hotel Parque")
        img_parque = os.path.join(ruta_base, "hotel_parque.jpg")
        if os.path.exists(img_parque):
            st.image(img_parque, caption="Instalaciones del Hotel Parque", width=650)
        else:
            st.info("📸 [Imagen Hotel Parque - Próximamente]")
        
        st.markdown("""
        * **Ubicación estratégica:** Cercano al centro y puntos de interés.
        * **Servicios:** Amplias habitaciones, salón de usos múltiples y áreas recreativas.
        * **Régimen:** Pensión completa con menú estudiantil/deportivo.
        """)

        st.divider()

        # OPCIÓN 2: HOTEL CAPILLA DEL LAGO
        st.subheader("🏨 Opción 2: Hotel Capilla del Lago")
        img_capilla = os.path.join(ruta_base, "hotel_capilla.jpg")
        if os.path.exists(img_capilla):
            st.image(img_capilla, caption="Vista del Hotel Capilla del Lago", width=650)
        else:
            st.info("📸 [Imagen Hotel Capilla del Lago - Próximamente]")
        
        st.markdown("""
        * **Exclusividad y confort:** Ubicado en una zona privilegiada con vistas al lago.
        * **Instalaciones:** Piscina, áreas verdes y salones climatizados.
        * **Atención personalizada:** Servicio enfocado en grupos y delegaciones.
        """)

    # --- CASO 2: SAN PEDRO ---
    elif "San Pedro" in destino:
        # OPCIÓN 1: HOTEL DE TURISMO DE SAN PEDRO
        st.subheader("🏢 Opción 1: Hotel de Turismo de San Pedro")
        img_turismo = os.path.join(ruta_base, "hotel_turismo_sp.jpg")
        if os.path.exists(img_turismo):
            st.image(img_turismo, caption="Fachada Hotel de Turismo", width=650)
        else:
            st.info("📸 [Imagen Hotel de Turismo - Próximamente]")
        
        st.markdown("""
        * **Un clásico frente al río:** Excelente ubicación para disfrutar de la costanera.
        * **Instalaciones:** Habitaciones confortables y amplios salones para el grupo.
        """)

        st.divider()

        # OPCIÓN 2: HOTEL LA RUEDA
        st.subheader("🏡 Opción 2: Hotel La Rueda")
        img_rueda = os.path.join(ruta_base, "hotel_la_rueda.jpg")
        if os.path.exists(img_rueda):
            st.image(img_rueda, caption="Instalaciones Hotel La Rueda", width=650)
        else:
            st.info("📸 [Imagen Hotel La Rueda - Próximamente]")
        
        st.markdown("""
        * **Tranquilidad y Servicio:** Un ambiente ideal para el descanso del contingente.
        * **Gastronomía:** Reconocido por su excelente servicio de comedor para delegaciones.
        """)

    # --- NOTA COMÚN ---
    st.info("🛎️ **Nota:** La asignación definitiva del hotel se confirma según disponibilidad al momento de la reserva del grupo.")
