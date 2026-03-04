# utilidades/footer.py
import streamlit as st

def render_footer():
    """Renderiza el footer minimalista blanco compatible con todas las secciones"""
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        /* Forzamos que el contenedor de Streamlit no corte el footer */
        .main .block-container {
            padding-bottom: 0px !important;
        }

        .custom-footer {
            background-color: #ffffff;
            border-top: 1px solid #f0f2f6;
            padding: 40px 20px;
            margin-top: 50px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 30px;
            width: 100%;
        }

        .footer-section {
            flex: 1;
            min-width: 250px;
            color: #666666;
            font-family: sans-serif;
        }

        .footer-section h4 {
            color: #1a1a1a !important;
            font-weight: 700 !important;
            margin-bottom: 15px !important;
            font-size: 1rem !important;
            text-transform: uppercase;
        }

        .footer-section p {
            font-size: 0.9rem !important;
            line-height: 1.5 !important;
            margin-bottom: 8px !important;
        }

        .social-icons {
            display: flex;
            gap: 15px;
        }

        .social-icons a {
            color: #444 !important;
            font-size: 1.4rem;
            text-decoration: none !important;
            transition: 0.3s;
        }

        .social-icons a:hover {
            color: #e4405f !important; /* Color Instagram */
        }

        /* Botón WhatsApp */
        .wa-float {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: #25d366;
            color: white !important;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            z-index: 9999;
            text-decoration: none !important;
        }
        </style>

        <div class="custom-footer">
            <div class="footer-section">
                <h4>Serrano Turismo</h4>
                <p>29 años de trayectoria impecable brindando experiencias inolvidables.</p>
                <p style="color: #999 !important; font-size: 0.8rem !important; margin-top: 20px;">
                    © 2026 Todos los derechos reservados.
                </p>
            </div>

            <div class="footer-section">
                <h4>Contacto</h4>
                <p>📍 <b>CABA:</b> Av. Rivadavia 4532</p>
                <p>📍 <b>Ituzaingó:</b> Parque Leloir</p>
                <p>📍 <b>San Pedro:</b> Costanera</p>
                <p>📞 11-4847-6467</p>
            </div>

            <div class="footer-section">
                <h4>Seguinos</h4>
                <div class="social-icons">
                    <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook-f"></i></a>
                </div>
            </div>
        </div>

        <a href="https://wa.me/5491156096283" class="wa-float" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
