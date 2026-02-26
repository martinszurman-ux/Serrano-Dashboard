import streamlit as st
import os

def render_hoteleria(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🏨 HOTELERÍA EN {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    ruta_base = "assets/"

    # --- LISTA DE CARACTERÍSTICAS (Unificada con tildes) ---
    features_html = """
    ✔️ Habitaciones triples y cuádruples con sommier, Aire Acondicionado y baño privado.<br>
    ✔️ Comedor restaurante. Cocina casera.<br>
    ✔️ SUM (Salón de Usos Múltiples).<br>
    ✔️ Teatro / Disco.<br>
    ✔️ Canchas de vóley, fútbol y fútbol-tenis.<br>
    ✔️ Piletas con guardavidas permanente.<br>
    ✔️ Amplios parques.<br>
    ✔️ Espacios cubiertos para actividades recreativas.<br>
    ✔️ Servicio de WiFi.<br>
    ✔️ Consultorio médico.<br>
    ✔️ Seguridad las 24 hs.
    """

    # --- CASO 1: VILLA CARLOS PAZ ---
    if "Villa Carlos Paz" in destino:
        # OPCIÓN 1: HOTEL PARQUE
        st.subheader("🏢 Opción 1: Hotel Parque")
        col1, col2 = st.columns([1.2, 1])
        with col1:
            img_parque = os.path.join(ruta_base, "hotel parque.jpeg")
            if os.path.exists(img_parque):
                st.image(img_parque, use_container_width=True)
            else:
                st.error("⚠️ Imagen 'hotel parque.jpeg' no encontrada.")
        with col2:
            st.markdown(f"<div style='font-size: 0.9rem; line-height: 1.5;'>{features_html}</div>", unsafe_allow_html=True)

        st.divider()

        # OPCIÓN 2: HOTEL CAPILLA DEL LAGO
        st.subheader("🏨 Opción 2: Hotel Capilla del Lago")
        col3, col4 = st.columns([1.2, 1])
        with col3:
            img_capilla = os.path.join(ruta_base, "capilla.jpeg")
            if os.path.exists(img_capilla):
                st.image(img_capilla, use_container_width=True)
            else:
                st.error("⚠️ Imagen 'capilla.jpeg' no encontrada.")
        with col4:
            st.markdown(f"<div style='font-size: 0.9rem; line-height: 1.5;'>{features_html}</div>", unsafe_allow_html=True)

    # --- CASO 2: SAN PEDRO ---
    elif "San Pedro" in destino:
        # OPCIÓN 1: HOTEL DE TURISMO DE SAN PEDRO
        st.subheader("🏢 Opción 1: Hotel de Turismo de San Pedro")
        col5, col6 = st.columns([1.2, 1])
        with col5:
            img_turismo = os.path.join(ruta_base, "hotel_turismo_sp.jpg")
            if os.path.exists(img_turismo):
                st.image(img_turismo, use_container_width=True)
            else:
                st.info("📸 [Imagen Hotel de Turismo - Próximamente]")
        with col6:
            st.markdown(f"<div style='font-size: 0.9rem; line-height: 1.5;'>{features_html}</div>", unsafe_allow_html=True)

        st.divider()

        # OPCIÓN 2: HOTEL LA RUEDA
        st.subheader("🏡 Opción 2: Hotel La Rueda")
        col7, col8 = st.columns([1.2, 1])
        with col7:
            img_rueda = os.path.join(ruta_base, "hotel_la_rueda.jpg")
            if os.path.exists(img_rueda):
                st.image(img_rueda, use_container_width=True)
            else:
                st.info("📸 [Imagen Hotel La Rueda - Próximamente]")
        with col8:
            st.markdown(f"<div style='font-size: 0.9rem; line-height: 1.5;'>{features_html}</div>", unsafe_allow_html=True)
