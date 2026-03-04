import streamlit as st
from utilidades.footer import generar_footer  # Importamos tu utilidad

def render_landing_cp():
    # 1. Hero Section
    st.image("assets/landingcarlospazimagen.png", use_container_width=True)
    
    st.title("☀️ Villa Carlos Paz: El Corazón del Valle de Punilla")
    st.markdown("""
    **Villa Carlos Paz** no es solo un destino, es una experiencia completa. 
    Desde el icónico Reloj Cuclú hasta las noches vibrantes de teatro, la ciudad ofrece el equilibrio perfecto entre sierras y entretenimiento.
    """)

    st.divider()

    # 2. Métricas Rápidas
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Distancia de CBA", "36 km")
    col_b.metric("Clima Promedio", "25°C")
    col_c.metric("Cartelera Teatral", "+50 Obras")

    st.divider()

    # 3. Secciones Destacadas con Tabs
    st.subheader("📍 ¿Qué hacer en la Villa?")
    
    tab1, tab2, tab3 = st.tabs(["Naturaleza", "Entretenimiento", "Gastronomía"])

    with tab1:
        st.markdown("""
        ### El contacto con la sierra
        * **Cerro de la Cruz:** Un ascenso con la mejor vista panorámica de la ciudad.
        * **Costanera del Lago:** 5 km de recorrido ideal para caminatas, mates o running.
        * **Balneario El Fantasio:** El clásico río para refrescarse en las tardes de verano.
        """)

    with tab2:
        st.markdown("""
        ### La ciudad que nunca duerme
        * **Teatros:** Disfrutá de las producciones más importantes del país en la calle 9 de Julio.
        * **Complejo Aerosilla:** Un viaje a las alturas con actividades de aventura.
        * **Pekos Multiparque:** Diversión garantizada para los más chicos.
        """)

    with tab3:
        st.markdown("""
        ### Sabores de Punilla
        * **Alfajores regionales:** Un clásico imperdible.
        * **Cenas frente al Lago:** Gastronomía de nivel en la Av. Atlantis.
        * **Cervecerías Artesanales:** El punto de encuentro tras el río.
        """)

    # 4. CTA y Formulario
    st.info("💡 **Dato Pro:** Si vas en temporada alta, reservá tus entradas de teatro con anticipación.")

    with st.container(border=True):
        st.subheader("📩 ¿Querés recibir una guía de precios?")
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Tu nombre")
        with col2:
            fecha = st.date_input("¿Cuándo pensás viajar?")
        
        email = st.text_input("Tu email:")
        
        if st.button("Descargar Guía de Carlos Paz 🚀"):
            if nombre and email:
                st.success(f"¡Genial {nombre}! Te enviamos la guía a {email}.")
            else:
                st.warning("Por favor, completa los campos.")

    # --- AQUÍ LLAMAMOS AL FOOTER ---
    st.divider()
    generar_footer()

# Para testing individual
if __name__ == "__main__":
    render_landing_cp()
