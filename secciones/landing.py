import streamlit as st

def render_landing():
    # Link directo de la imagen
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS General y para elementos específicos
    st.markdown("""
        <style>
        /* Importar iconos de FontAwesome */
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

        /* Reset general para asegurar que el footer se pegue al fondo */
        .main .block-container {
            padding-bottom: 0rem;
        }

        /* HERO SECTION */
        .hero-title {
            font-size: 4.2rem !important;
            font-weight: 800;
            color: #1a1a1a;
            line-height: 1.1;
            margin-bottom: 15px;
        }
        .hero-subtitle {
            font-size: 1.3rem;
            color: #555;
            margin-bottom: 35px;
        }
        .img-hero-style {
            width: 100%;
            max-width: 500px;
            border-radius: 25px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }

        /* EXPERIENCIAS */
        .section-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 700;
            margin: 80px 0 50px 0;
            color: #1a1a1a;
        }
        .exp-card { text-align: center; padding: 20px; }
        .exp-circle {
            width: 130px; height: 130px; background-color: #f8f9fa;
            border-radius: 50%; margin: 0 auto 25px auto;
            display: flex; align-items: center; justify-content: center;
            font-size: 3rem; border: 1px solid #eee;
            box-shadow: 0 5px 15px rgba(0,0,0,0.03);
        }

        /* FOOTER CORREGIDO (SIN ESPACIOS EN BLANCO) */
        .footer-fixed-container {
            background-color: #1a1a1a;
            color: white;
            padding: 60px 5%;
            margin-top: 100px;
            
            /* Truco para extender de borde a borde */
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 30px;
        }
        .footer-col { flex: 1; min-width: 250px; padding: 10px; }
        .footer-col h4 { color: #fff; margin-bottom: 20px; font-size: 1.1rem; letter-spacing: 1px; font-weight: 700; }
        .footer-col p { color: #aaa; font-size: 0.9rem; line-height: 1.7; margin-bottom: 10px; }
        
        /* Iconos Redes Sociales en Footer */
        .social-icons { margin-top: 20px; display: flex; gap: 20px; }
        .social-icons a { 
            color: #aaa; font-size: 1.5rem; transition: all 0.3s ease; 
            display: inline-block;
        }
        .social-icons a:hover { color: #fff; transform: scale(1.2); }

        /* BOTÓN WHATSAPP FLOTANTE Y ANIMADO */
        .whatsapp-float {
            position: fixed;
            width: 60px;
            height: 60px;
            bottom: 40px;
            right: 40px;
            background-color: #25d366;
            color: #FFF;
            border-radius: 50px;
            text-align: center;
            font-size: 30px;
            box-shadow: 2px 2px 3px #999;
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none !important;
            transition: all 0.3s ease;
            
            /* Animación de pulso */
            animation: pulse-green 2s infinite;
        }
        .whatsapp-float:hover {
            background-color: #128C7E;
            transform: scale(1.1);
        }

        @keyframes pulse-green {
            0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
            100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
        </style>
    """, unsafe_allow_html=True)

    # 1. HERO SECTION
    col_text, col_img = st.columns([1.2, 1], gap="large")

    with col_text:
        st.markdown('<div style="margin-top:80px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura de egresados empieza acá.<br>Experiencias diseñadas para crear recuerdos inolvidables.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_img:
        st.markdown(f'<img src="{LANDING_IMG}" class="img-hero-style">', unsafe_allow_html=True)

    # 2. EXPERIENCIAS
    st.markdown('<h2 class="section-title">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown('<div class="exp-card"><div class="exp-circle">🚌</div><h4>Transporte Premium</h4><p>Unidades modernas de última generación para un viaje seguro y confortable.</p></div>', unsafe_allow_html=True)
    with e2:
        st.markdown('<div class="exp-card"><div class="exp-circle">🏨</div><h4>Hoteles Propios</h4><p>Alojamiento exclusivo con infraestructura y servicios pensados para estudiantes.</p></div>', unsafe_allow_html=True)
    with e3:
        st.markdown('<div class="exp-card"><div class="exp-circle">🏞️</div><h4>Coordinación Total</h4><p>Equipo profesional las 24hs acompañando y guiando cada actividad.</p></div>', unsafe_allow_html=True)

    # 3. FOOTER CORREGIDO CON REDES SOCIALES
    st.markdown("""
        <div class="footer-fixed-container">
            <div class="footer-col">
                <h4>SERRANO TURISMO</h4>
                <p>Más de 28 años de trayectoria impecable en turismo estudiantil, garantizando seguridad y diversión.</p>
            </div>
            <div class="footer-col">
                <h4>CONTACTO</h4>
                <p>📍 Rivadavia 4532 - CABA</p>
                <p>📍 Del Cimarrón 1846 - Ituzaingo</p>
                <p>📞 11-4847-6467</p>
                <p>✉️ info@serranoturismo.com.ar</p>
            </div>
            <div class="footer-col">
                <h4>SÍGUENOS</h4>
                <p>Conoce nuestras últimas aventuras y novedades en redes sociales.</p>
                <div class="social-icons">
                    <a href="https://www.facebook.com/serranoturismo/" target="_blank"><i class="fab fa-facebook-f"></i></a>
                    <a href="https://www.instagram.com/serrano_turismo/" target="_blank"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. BOTÓN WHATSAPP FLOTANTE ANIMADO
    # Reemplaza el número de teléfono (sin espacios ni símbolos)
    WHATSAPP_LINK = "https://wa.me/5491156096283?text=Hola%20Serrano%20Turismo,%20quería%20consultar%20por..."
    
    st.markdown(f"""
        <a href="{WHATSAPP_LINK}" class="whatsapp-float" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
