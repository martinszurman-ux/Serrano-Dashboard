import streamlit as st

def render_landing_sp():
    # URL de imagen de fondo de ejemplo (cambiala por la tuya)
    IMG_HERO = "https://tu-link-de-imagen.jpg"

    st.markdown("""
        <style>
        /* 1. ELIMINAR ESPACIO SUPERIOR EXCESIVO */
        .content-wrapper { margin-top: 50px !important; } /* Ajustamos el margen del app.py */
        
        .hero-container {
            margin-top: -40px; /* Subimos el título y la imagen */
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 40px;
        }

        .hero-title {
            font-size: 4rem !important;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 10px;
        }

        /* 2. SECCIÓN EXPERIENCIAS CON FONDO GRIS LADO A LADO */
        .full-width-grey {
            background-color: #f1f3f5;
            margin-left: -10vw; /* Rompe el contenedor de Streamlit hacia la izquierda */
            margin-right: -10vw; /* Rompe hacia la derecha */
            padding: 60px 10vw; /* Devuelve el contenido al centro */
            text-align: center;
        }
        
        .section-title {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 40px;
            color: #1a1a1a;
        }

        .exp-card { text-align: center; }
        .exp-circle {
            width: 140px; height: 140px;
            background-color: white;
            border-radius: 50%;
            margin: 0 auto 20px auto;
            display: flex; align-items: center; justify-content: center;
            font-size: 2.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }

        /* 3. FOOTER PROPORCIONADO Y SIN ESPACIO BLANCO */
        .footer-full {
            background-color: #1a1a1a;
            color: white;
            margin-left: -10vw;
            margin-right: -10vw;
            margin-bottom: -100px; /* Elimina el espacio blanco final de Streamlit */
            padding: 40px 10vw; /* Menos padding para que no sea tan alto */
            display: flex;
            justify-content: space-between;
            gap: 20px;
        }
        .footer-col { flex: 1; }
        .footer-col h4 { font-size: 0.9rem; letter-spacing: 1px; margin-bottom: 15px; color: #fff; }
        .footer-col p { font-size: 0.8rem; color: #aaa; line-height: 1.5; margin: 0; }
        </style>
    """, unsafe_allow_html=True)

    # --- CUERPO DE LA PÁGINA ---

    # Hero Section
    col_txt, col_img = st.columns([1, 1.2])
    with col_txt:
        st.markdown('<div class="hero-container"><div>', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#555;">Tu escapada perfecta a San Pedro.</p>', unsafe_allow_html=True)
        # Botón de acción rápido
        st.markdown('<a href="/?nav=Transporte&destino=San+Pedro" target="_self" style="text-decoration:none; background:black; color:white; padding:12px 25px; border-radius:5px; font-weight:bold; display:inline-block; margin-top:20px;">EXPLORAR VIAJE</a>', unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)
    
    with col_img:
        # Usamos st.image para que mantenga proporciones si querés, o el HTML previo
        st.image("https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg", use_container_width=True)

    # Sección Experiencias (Gris de lado a lado)
    st.markdown('<div class="full-width-grey">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    
    # Usamos columnas de Streamlit dentro del div gris
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="exp-card"><div class="exp-circle">🚌</div><h4>Transporte</h4><p>Unidades de última generación.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="exp-card"><div class="exp-circle">🏨</div><h4>Hotelería</h4><p>Confort en el centro del destino.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="exp-card"><div class="exp-circle">🍽️</div><h4>Gastronomía</h4><p>Menú completo y variado.</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer Ajustado
    st.markdown("""
        <div class="footer-full">
            <div class="footer-col">
                <h4>SERRANO TURISMO</h4>
                <p>29 años creando experiencias inolvidables para egresados.</p>
            </div>
            <div class="footer-col">
                <h4>CONTACTO</h4>
                <p>WhatsApp: +54 9 11 1234-5678</p>
                <p>Email: info@serranoturismo.com</p>
            </div>
            <div class="footer-col" style="text-align:right;">
                <h4>SIGUENOS</h4>
                <p>Instagram | Facebook</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
