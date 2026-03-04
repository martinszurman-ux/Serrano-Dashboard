import streamlit as st
from utilidades.footer import render_footer  # Importación corregida

def render_landing_cp():
    # 1. Hero Section
    st.image("assets/landingcarlospazimagen.png", use_container_width=True)
    
    st.title("☀️ Villa Carlos Paz: El Corazón del Valle de Punilla")
    st.markdown("""
    **Villa Carlos Paz** no es solo un destino, es una experiencia completa. 
    Desde el icónico Reloj Cuclú hasta las noches vibrantes de teatro.
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
        st.markdown("* **Cerro de la Cruz**\n* **Costanera del Lago**\n* **Balneario El Fantasio**")
    with tab2:
        st.markdown("* **Teatros de la calle 9 de Julio**\n* **Complejo Aerosilla**\n* **Pekos Multiparque**")
    with tab3:
        st.markdown("* **Alfajores regionales**\n* **Cenas frente al Lago**\n* **Cervecerías Artesanales**")

    # 4. Formulario de contacto
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
                st.success(f"¡Enviado a {email}!")
            else:
                st.warning("Completa los campos.")

    # --- LLAMADA AL FOOTER ---
    render_footer()

if __name__ == "__main__":
    render_landing_cp()
