import streamlit as st
import os

def render_comidas(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🍽️ RÉGIMEN DE COMIDAS - {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    ruta_base = "assets/"

    # --- TEXTO EN UNA SOLA LÍNEA PARA EVITAR ERRORES DE RENDERIZADO ---
    features_html = "<p style='margin-bottom:12px;'>✔️ <b>Pensión completa:</b> desayuno, almuerzo, merienda, cena y quinta comida.</p><p style='margin-bottom:12px;'>✔️ <b>Menú buffet libre:</b> Variedad y calidad garantizada.</p><p style='margin-bottom:12px;'>✔️ <b>Hidratación:</b> Provisión de agua mineral libre las 24hs.</p><p style='margin-bottom:12px;'>✔️ <b>Sistema Todo Incluido:</b> Sándwiches, alfajores, bizcochuelos, frutas, helados, gaseosas y jugos libre todos los días.</p><p style='margin-bottom:12px;'>✔️ <b>Servicio en Ruta:</b> Desayuno y almuerzo en el viaje de ida. Almuerzo y merienda en el regreso en nuestros paradores exclusivos.</p><p style='margin-bottom:12px;'>✔️ <b>Estaciones Saludables:</b> Disponibles en excursiones y hotel.</p><p style='margin-bottom:12px;'>✔️ <b>Menú Diferenciado:</b> Atención especial en dietas médicas o celíacas.</p>" #

    if "Villa Carlos Paz" in destino:
        fotos = ["desayuno.jpg", "almuerzo.jpg", "refrigerio.jpg", "dietas.png"]
    else:
        fotos = ["desayuno san pedro.jpg", "comida san pedro 1.jpeg", "comida san pedro.jpeg", "dietas.png"]

    col_izq, col_der = st.columns([1.2, 1])

    with col_izq:
        c1, c2 = st.columns(2)
        with c1:
            img1 = os.path.join(ruta_base, fotos[0])
            if os.path.exists(img1): st.image(img1, use_container_width=True)
            img3 = os.path.join(ruta_base, fotos[2])
            if os.path.exists(img3): st.image(img3, use_container_width=True)
        with c2:
            img2 = os.path.join(ruta_base, fotos[1])
            if os.path.exists(img2): st.image(img2, use_container_width=True)
            img4 = os.path.join(ruta_base, fotos[3])
            if os.path.exists(img4): st.image(img4, use_container_width=True)

    with col_der:
        # Renderizado directo sin espacios extra
        st.markdown(f"<div style='background-color:#f8f9fa; padding:25px; border-radius:15px; border-left:5px solid #1E3A8A; color:#333; font-size:1.05rem; line-height:1.2;'>{features_html}</div>", unsafe_allow_html=True) #
