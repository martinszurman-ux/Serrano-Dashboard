import streamlit as st

def render():
    # Configuración de cabecera
    st.title("☀️ Villa Carlos Paz: El Corazón del Valle de Punilla")
    st.subheader("Tu próxima aventura comienza aquí")

    # Banner principal o Imagen destacada
    st.image("https://images.unsplash.com/photo-1590059392253-ba1914940562?auto=format&fit=crop&q=80", 
             caption="Vista del Lago San Roque", use_container_width=True)

    # Introducción
    st.markdown("""
    ### ¡Bienvenido a la Perla de Córdoba!
    Villa Carlos Paz combina la serenidad de sus sierras con una vibrante vida nocturna y cartelera teatral. 
    Es el destino ideal tanto para familias como para jóvenes que buscan diversión y naturaleza.
    """)

    # Sección de Atractivos
    st.divider()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("🎭 **Teatro y Show**")
        st.caption("La mejor cartelera de espectáculos del país durante todo el verano.")

    with col2:
        st.write("🌊 **Lago San Roque**")
        st.caption("Deportes acuáticos, paseos en catamarán y la emblemática costanera.")

    with col3:
        st.write("🚠 **Aerosilla**")
        st.caption("Vistas panorámicas increíbles de toda la ciudad y las sierras.")

    # Sección Informativa / Datos clave
    st.divider()
    st.info("📌 **Tip de viajero:** No olvides visitar el famoso Reloj Cuclú y caminar por la costanera al atardecer.")

    # Formulario de Contacto / Lead Magnet
    with st.expander("📩 ¿Quieres recibir más información sobre paquetes?"):
        with st.form("contacto_carlospaz"):
            nombre = st.text_input("Nombre completo")
            email = st.text_input("Correo electrónico")
            mensaje = st.text_area("¿Qué te gustaría visitar?")
            
            submit = st.form_submit_button("¡Enviar consulta!")
            if submit:
                st.success(f"¡Gracias {nombre}! Pronto te enviaremos novedades a {email}.")

# Si quieres probarlo directamente ejecutando este archivo:
if __name__ == "__main__":
    render()
