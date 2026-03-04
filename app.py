import streamlit as st

def render_landing_sp():
    # 1. CSS LIMPIO Y SIN ERRORES
    st.markdown("""
        <style>
        /* Ajuste para subir el contenido al máximo */
        .block-container { padding-top: 1rem !important; }
        
        .hero-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: -30px;
            margin-bottom: 40px;
        }

        .hero-title {
            font-size: 3.8rem !important;
            font-weight: 800;
            line-height: 1.1;
            color: #1a1a1a;
        }

        /* Sección Gris de lado a lado */
        .grey-box {
            background-color: #f1f3f5;
            margin-left: -15vw;
            margin-right: -15vw;
            padding: 60px 15vw;
            text-align: center;
        }

        .exp-card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
            height: 100%;
        }

        .exp-icon { font-size: 3rem; margin-bottom: 15px; display: block; }

        /* Footer Negro Proporcionado */
        .footer-black {
            background-color: #1a1a1a;
            color: #888;
            margin-left: -15vw;
            margin-right: -15vw;
            margin-bottom: -100px;
            padding: 40px 15vw;
            display: flex;
            justify-content: space-between;
        }
        
        .footer-black h4 { color: white; margin-bottom: 10px; font-size: 14px; }
        .footer-black p { font-size: 13px; margin: 2px 0; }
        </style>
    """, unsafe_allow_html=True)

    # 2. HERO SECTION
    col_1, col_2 = st.columns([1, 1.2], gap="large")
    
    with col_1:
        st.markdown('<div style="margin-top: 50px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">San Pedro <br>Inolvidable</h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#666;">Viví tu viaje de egresados en el corazón de la provincia.</p>', unsafe_allow_html=True)
        st.markdown('<br><a href="/?nav=Transporte&destino=San+Pedro" target="_self" style="background:black; color:white; padding:15px 30px; text-decoration:none; border-radius:8px; font-weight:bold;">VER TRANSPORTE</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_2:
        st.image("https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg", use_container_width=True)

    # 3. SECCIÓN GRIS (Side-to-Side)
    st.markdown('<div class="grey-box">', unsafe_allow_html=True)
    st.markdown('<h2 style="margin-bottom:40px; font-weight:700;">Experiencias Serrano</h2>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="exp-card"><span class="exp-icon">🚌</span><h4>Buses Premium</h4><p>Unidades semicama con la mejor tecnología.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="exp-card"><span class="exp-icon">🏨</span><h4>Hoteles Top</h4><p>Ubicación estratégica y confort garantizado.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="exp-card"><span class="exp-icon">🍽️</span><h4>Comidas VIP</h4><p>Menú variado con las mejores marcas.</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. FOOTER NEGRO
    st.markdown("""
        <div class="footer-black">
            <div>
                <h4>SERRANO TURISMO</h4>
                <p>Especialistas en grupos.</p>
                <p>© 2026 Todos los derechos reservados.</p>
            </div>
            <div>
                <h4>CONTACTO</h4>
                <p>WhatsApp: 11-4847-6467</p>
                <p>Ituzaingó, Buenos Aires</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
