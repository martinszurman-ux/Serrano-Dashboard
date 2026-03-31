import streamlit as st
import os
from utilidades.footer import render_footer

def render_transporte(destino):
    # CSS Inyectado para forzar que las imágenes nunca desborden el ancho de pantalla
    st.markdown("""
        <style>
        img {
            max-width: 100%;
            height: auto;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título dinámico
    titulo_emoji = "✈️ 🚌" if "Villa Carlos Paz" in destino else "🚌"
    st.markdown(f"<h2 style='text-align: center; color: #1E3A8A; font-size: 1.5rem;'>{titulo_emoji} TRANSPORTE A {destino.upper()}</h2>", unsafe_allow_html=True)
    st.divider()

    img_micro_local = "assets/micros.png" 
    img_avion_local = "assets/AVION.jpg"

    # --- CASO 1: VILLA CARLOS PAZ ---
    if "Villa Carlos Paz" in destino:
        st.subheader("✈️ Opción Aérea: Aerolíneas Argentinas")
        
        # Sistema de columnas: En PC deja aire a los lados, en Móvil se apilan
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            if os.path.exists(img_avion_local):
                st.image(img_avion_local, caption="Volamos en Aerolineas Argentinas", use_container_width=True)
            else:
                st.error(f"⚠️ No se encontró: {img_avion_local}")
            
        st.write("Optimizamos tu tiempo con cupos confirmados en nuestra aerolínea de bandera.")
        st.divider()
        
        st.subheader("🚍 Opción Terrestre")
        col_m1, col_m2, col_m3 = st.columns([1, 6, 1])
        with col_m2:
            if os.path.exists(img_micro_local):
                st.image(img_micro_local, caption="Nuestras unidades de Serrano Turismo", use_container_width=True)
            else:
                st.error(f"⚠️ No se encontró: {img_micro_local}")

    # --- CASO 2: SAN PEDRO ---
    elif "San Pedro" in destino:
        st.subheader("🚍 Transporte Terrestre Exclusivo")
        col_s1, col_s2, col_s3 = st.columns([1, 6, 1])
        with col_s2:
            if os.path.exists(img_micro_local):
                st.image(img_micro_local, caption="Unidades equipadas para tu confort", use_container_width=True)
            else:
                st.error(f"⚠️ No se encontró: {img_micro_local}")
            
        st.write(f"Viajá con la tranquilidad de **Serrano Turismo**.")

    # --- CARACTERÍSTICAS COMUNES ---
    st.markdown("### ✨ Características de nuestro servicio:")
    st.info("""
    * ✅ **Buses de última generación:** Unidades modernas con máximo confort.
    * ✅ **Empresas de transporte Charter:** Seguridad y exclusividad garantizada.
    * ✅ **Exclusividad:** El bus queda a disposición del grupo para los traslados.
    """)

    render_footer()
