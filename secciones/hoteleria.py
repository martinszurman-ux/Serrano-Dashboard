import streamlit as st

def render_hoteleria(destino):
    st.markdown(f'<div class="header-container"><div class="header-text-overlay">HOTELERÍA - {destino.upper()}</div></div>', unsafe_allow_html=True)
    
    if destino == "Villa Carlos Paz":
        h1, h2 = "Hotel Parque", "Hotel Capilla del Lago"
        desc = "Habitaciones con somier, AA, baño privado, piletas con guardavidas y canchas deportivas."
    else:
        h1, h2 = "Hotel de Turismo San Pedro", "Complejo La Rueda"
        desc = "Habitaciones con AA, pileta exterior y climatizada, amplios parques y juegos inflables."

    st.markdown(f"""
        <div class="widget-3d-grad">
            <div style="font-size: 3rem;">🏨</div>
            <p class='widget-title'>Alojamiento Exclusivo</p>
            <h3 style="color: #495057;">{h1} / {h2}</h3>
            <p style="color: #6c757d;">{desc}</p>
        </div>
    """, unsafe_allow_html=True)
