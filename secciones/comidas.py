import streamlit as st
import os

def render_comidas(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🍽️ RÉGIMEN DE COMIDAS - {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    ruta_base = "assets/"

    # --- TEXTO DETALLADO (Lado derecho) ---
    features_html = """
    ✔️ <b>Pensión completa:</b> desayuno, almuerzo, merienda, cena y quinta comida.<br><br>
    ✔️ <b>Menú buffet libre:</b> Variedad y calidad garantizada.<br><br>
    ✔️ <b>Hidratación:</b> Provisión de agua mineral libre las 24hs.<br><br>
    ✔️ <b>Sistema Todo Incluido:</b> Sándwiches, alfajores, bizcochuelos, frutas, helados, gaseosas y jugos libre todos los días.<br><br>
    ✔️ <b>Servicio en Ruta:</b> Desayuno y almuerzo en el viaje de ida. Almuerzo y merienda en el regreso en nuestros paradores exclusivos.<br><br>
    ✔️ <b>Estaciones Saludables:</b> Disponibles en excursiones y hotel.<br><br>
    ✔️ <b>Menú Diferenciado:</b> Atención especial en dietas médicas o celíacas.
    """

    # --- LÓGICA DE IMÁGENES POR DESTINO ---
    if "Villa Carlos Paz" in destino:
        fotos = [
            "desayuno.jpg",
            "almuerzo.jpg",
            "refrigerio.jpg",
            "dietas.png"
        ]
    else:  # SAN PEDRO
        fotos = [
            "desayuno san pedro.jpg",
            "comida san pedro 1.jpeg",
            "comida san pedro.jpeg",
            "dietas.png"
        ]

    # --- DISEÑO DE COLUMNAS ---
    col_izq, col_der = st.columns([1.2, 1])

    with col_izq:
        # Mostramos las 4 fotos en una grilla de 2x2
        c1, c2 = st.columns(2)
        
        # Foto 1 y 2
        with c1:
            img1 = os.path.join(ruta_base, fotos[0])
            if os.path.exists(img1): st.image(img1, use_container_width=True)
            
            img3 = os.path.join(ruta_base, fotos[2])
            if os.path.exists(img3): st.image(img3, use_container_width=True)
            
        # Foto 3 y 4
        with c2:
            img2 = os.path.join(ruta_base, fotos[1])
            if os.path.exists(img2): st.image(img2, use_container_width=True)
            
            img4 = os.path.join(ruta_base, fotos[3])
            if os.path.exists(img4): st.image(img4, use_container_width=True)

    with col_der:
        st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 25px; border-radius: 15px; border-left: 5px solid #1E3A8A;'>
                <div style='font-size: 1.0rem; line-height: 1.6; color: #333;'>
                    {features_html}
                </div>
            </div>
        """, unsafe_allow_html=True)
