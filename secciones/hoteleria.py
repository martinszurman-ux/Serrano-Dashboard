import streamlit as st
import os

def render_hoteleria(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🏨 HOTELERÍA EN {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    ruta_base = "assets/"

    # --- CASO 1: VILLA CARLOS PAZ ---
    if "Villa Carlos Paz" in destino:
        
        # Lista de características comunes para Carlos Paz
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

        # --- OPCIÓN 1: HOTEL PARQUE ---
        st.subheader("🏢 Opción 1: Hotel Parque")
        col1, col2 = st.columns([1.2, 1]) # Dividimos el espacio
        
        with col1:
            img_parque = os.path.join(ruta_base, "hotel parque.jpeg")
            if os.path.exists(img_parque):
                st.image(img_parque, use_container_width=True)
            else:
                st.error("⚠️ Imagen 'hotel parque.jpeg' no encontrada.")
        
        with col2:
            st.markdown(f"<div style='font-size: 0.95rem; line-height: 1.6;'>{features_html}</div>", unsafe_allow_html=True)

        st.divider()

        # --- OPCIÓN 2: HOTEL CAPILLA DEL LAGO ---
        st.subheader("🏨 Opción 2: Hotel Capilla del Lago")
        col3, col4 = st.columns([1.2, 1])
        
        with col3:
            img_capilla = os.path.join(ruta_base, "capilla.jpeg")
            if os.path.exists(img_capilla):
                st.image(img_capilla, use_container_width=True)
            else:
                st.error("⚠️ Imagen 'capilla.jpeg' no encontrada.")
        
        with col4:
            st.markdown(f"<div style='font-size: 0.95rem; line-height: 1.6;'>{features_html}</div>", unsafe_allow_html=True)

    # --- CASO 2: SAN PEDRO ---
    elif "San Pedro" in destino:
        # Aquí podrías aplicar la misma lógica si los hoteles de San Pedro comparten estas características
        st.subheader("🏢 Opción 1: Hotel de Turismo de San Pedro")
        # ... (resto del código de San Pedro)
        st.subheader("🏡 Opción 2: Hotel La Rueda")
        # ...
