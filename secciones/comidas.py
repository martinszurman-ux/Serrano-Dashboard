import streamlit as st

def render_comidas(destino):
    # Título de la sección
    st.write(f"### 🍽️ Servicio de Comidas - {destino}")
    
    # Mensaje de bienvenida estética
    st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #444444;">
            <p style="color: #444444; font-size: 1.1rem; font-weight: 600; margin: 0;">
                Nuestra propuesta gastronómica está diseñada para brindar una alimentación equilibrada, 
                variada y de alta calidad durante todo el viaje en {destino}.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # Columnas para organizar la info
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🥗 Régimen de Pensión Completa")
        st.write("""
        * **Desayuno Buffet:** Infusiones, jugos, tostadas, frutas y pastelería.
        * **Almuerzo:** Plato principal, guarnición, postre y bebida.
        * **Merienda:** Merienda temática o clásica según actividad.
        * **Cena:** Entrada, plato principal, postre y bebida.
        """)

    with col2:
        st.markdown("#### 🛡️ Dietas Especiales")
        st.info("""
        Contamos con menús adaptados para:
        * Celíacos (Sin TACC)
        * Vegetarianos / Veganos
        * Alérgicos e Intolerantes
        
        *Es importante informar estas condiciones en la Ficha de Adhesión.*
        """)

    st.divider()
    
    # Espacio para futuras fotos
    st.write("#### 📸 Galería de Menús")
    st.warning("Próximamente: Fotos reales de nuestros platos y salones comedores.")
