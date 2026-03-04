import streamlit as st

def render_landing():
    # URL de la imagen en tu GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS TOTAL - AJUSTADO PARA ELIMINAR ESPACIO FINAL
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        /* 1. RESET ESTRUCTURAL AGRESIVO */
        header {visibility: hidden;}
        footer {display: none !important;} /* Elimina el footer nativo de Streamlit */
        
        .main .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important; /* Elimina espacio al final */
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }

        /* Fuerza al contenedor de la aplicación a no tener scroll extra */
        [data-testid="stVerticalBlock"] {
            gap: 0px !important;
        }

        [data-testid="stVerticalBlock"] > div:first-child {
            margin-top: -100px !important;
        }

        /* 2. HERO SECTION */
        .hero-container {
            padding: 0px 8% 0px 8%; 
            background-color: white;
            display: flex;
            align-items: center;
        }
        .hero-title {
            font-size: 4rem !important;
            font-weight: 800;
            color: #1a1a1a;
            line-height: 1;
        }
        .img-hero-style {
            width: 100%;
            max-width: 450px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        /* 3. SECCIÓN EXPERIENCIAS (Gris Full Width) */
        .experiences-outer {
            background-color: #d1d5db;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            padding: 80px 0;
        }
        
        .experiences-inner {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
            padding: 0 20px;
        }

        /* 4. SPACERS SIMÉTRICOS (Blanco antes y después) */
        .simetric-spacer {
            background-color: white;
            height: 80px; 
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
        }

        /* 5. FOOTER FINAL (Ajuste para que sea el fin absoluto) */
        .footer-full {
            background-color: #1a1a1a;
            color: white;
            padding: 60px 8% 60px 8%;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 30px;
            margin-bottom: -50px !important; /* "Pisa" el posible margen final */
        }

        /* WHATSAPP */
        .whatsapp-btn {
            position: fixed; bottom: 25px; right: 25px;
            background-color: #25d366; color: white !important;
            width: 55px; height: 55px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 28px; z-index: 9999;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CONTENIDO ---

    # 1. HERO SECTION
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    c1, c2 = st.columns([1.2, 0.8])
    with c1:
        st.markdown('<div style="margin-top:20px; padding-right: 20px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown("""
            <p style="font-size:1.15rem; color:#444; margin-top:20px; line-height:1.6; text-align: justify;">
                Tu aventura de egresados empieza acá.<br>
                Más de 100.000 egresados de Buenos Aires ya confiaron en nosotros. 
                Con 29 años de experiencia, Serrano Turismo es sinónimo de transparencia y cumplimiento, 
                transformando cada viaje en una experiencia inolvidable con la seriedad que tu familia busca.
            </p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div style="text-align:right;"><img src="{LANDING_IMG}" class="img-hero-style"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. SPACER ANTES
    st.markdown('<div class="simetric-spacer"></div>', unsafe_allow_html=True)

    # 3. SECCIÓN EXPERIENCIAS
    st.markdown("""
        <div class="experiences-outer">
            <div class="experiences-inner">
                <h2 style="font-size:2.5rem; font-weight:700; margin-bottom:50px; color:#1a1a1a;">Experiencias Inolvidables</h2>
                <div style="display: flex; justify-content: center; gap: 40px; flex-wrap: wrap;">
                    <div style="flex:1; min-width:250px; text-align:center;">
                        <div style="width:110px; height:110px; background:white; border-radius:50%; margin:0 auto 20px; display:flex; align-items:center; justify-content:center; font-size:2.8rem; box-shadow:0 4px 15px rgba(0,0,0,0.05);">🚌</div>
                        <h4 style="font-weight:700;">Transporte Premium</h4>
                        <p style="color:#4b5563; font-size:0.9rem;">Unidades modernas de última generación.</p>
                    </div>
                    <div style="flex:1; min-width:250px; text-align:center;">
                        <div style="width:110px; height:110px; background:white; border-radius:50%; margin:0 auto 20px; display:flex; align-items:center; justify-content:center; font-size:2.8rem; box-shadow:0 4px 15px rgba(0,0,0,0.05);">🏨</div>
                        <h4 style="font-weight:700;">Hoteles Propios</h4>
                        <p style="color:#4b5563; font-size:0.9rem;">Exclusividad y seguridad en los destinos.</p>
                    </div>
                    <div style="flex:1; min-width:250px; text-align:center;">
                        <div style="width:110px; height:110px; background:white; border-radius:50%; margin:0 auto 20px; display:flex; align-items:center; justify-content:center; font-size:2.8rem; box-shadow:0 4px 15px rgba(0,0,0,0.05);">🛡️</div>
                        <h4 style="font-weight:700;">Seguridad 24/7</h4>
                        <p style="color:#4b5563; font-size:0.9rem;">Coordinación y asistencia médica integral.</p>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. SPACER DESPUÉS
    st.markdown('<div class="simetric-spacer"></div>', unsafe_allow_html=True)

    # 5. FOOTER FINAL (Sin espacio blanco después)
    st.markdown("""
        <div class="footer-full">
            <div style="flex:1; min-width:250px;">
                <h4 style="margin-bottom:15px; font-weight:700; color:white;">SERRANO TURISMO</h4>
                <p style="color:#999; font-size:0.85rem;">29 años de trayectoria impecable.</p>
            </div>
            <div style="flex:1; min-width:250px;">
                <h4 style="margin-bottom:15px; font-weight:700; color:white;">CONTACTO</h4>
                <p style="color:#999; font-size:0.85rem;">📍 CABA: Av. Rivadavia 4532<br>📍 Ituzaingó: Del Cimarrón 1846<br>📞 11-4847-6467</p>
            </div>
            <div style="flex:1; min-width:200px;">
                <h4 style="margin-bottom:15px; font-weight:700; color:white;">REDES</h4>
                <div style="display:flex; gap:15px;">
                    <a href="https://instagram.com/serrano_turismo" target="_blank" style="color:white; font-size:1.5rem;"><i class="fab fa-instagram"></i></a>
                    <a href="https://facebook.com/serranoturismo" target="_blank" style="color:white; font-size:1.5rem;"><i class="fab fa-facebook-f"></i></a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 6. WHATSAPP
    st.markdown('<a href="https://wa.me/5491156096283" class="whatsapp-btn" target="_blank"><i class="fab fa-whatsapp"></i></a>', unsafe_allow_html=True)
