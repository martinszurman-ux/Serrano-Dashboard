import streamlit as st

# Por esto:
def render_landing_cp():
    st.image("assets/landingcarlospazimagen.png", use_container_width=True)
    
    st.title("☀️ Villa Carlos Paz: El Corazón del Valle de Punilla")
    st.markdown("""
    **Villa Carlos Paz** no es solo un destino, es una experiencia completa. 
    Desde el icónico Reloj Cuclú hasta las noches vibrantes de teatro, la ciudad ofrece el equilibrio perfecto entre sierras y entretenimiento.
    """)

    st.divider()

    # 2. Métricas Rápidas (Para dar info de un vistazo)
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
        * **Pekos Multiparque:** Diversión garantizada para los más chicos (y no tan chicos).
        """)

    with tab3:
        st.markdown("""
        ### Sabores de Punilla
        * **Alfajores regionales:** No te podés ir sin probar los clásicos cordobeses.
        * **Cenas frente al Lago:** Restaurantes de primer nivel sobre la Av. Atlantis.
        * **Cervecerías Artesanales:** El punto de encuentro tras un día de río.
        """)

    # 4. Sección de Llamado a la Acción (CTA)
    st.info("💡 **Dato Pro:** Si vas en temporada alta, reservá tus entradas de teatro con anticipación.")

    # Formulario de consulta
    with st.container(border=True):
        st.subheader("📩 ¿Querés recibir una guía de precios?")
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Tu nombre")
        with col2:
            fecha = st.date_input("¿Cuándo pensás viajar?")
        
        email = st.text_input("Tu email para enviarte la guía:")
        
        if st.button("Descargar Guía de Carlos Paz 🚀"):
            if nombre and email:
                st.success(f"¡Genial {nombre}! Te enviamos la guía a {email}. ¡Nos vemos en las sierras!")
            else:
                st.warning("Por favor, completa los campos para continuar.")

# Para testing individual
if __name__ == "__main__":
    render()
