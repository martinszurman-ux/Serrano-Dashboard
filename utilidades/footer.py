# utilidades/footer.py
import streamlit as st

def render_footer():
    """Renderiza el footer institucional de Serrano Turismo con look moderno en blanco"""
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        /* Contenedor Principal del Footer */
        .footer-container {
            background-color: #ffffff;
            color: #444;
            padding: 40px 0px;
            margin-top: 50px;
            border-top: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 30px;
            font-family: 'Source Sans Pro', sans-serif;
        }
        
        /* Columnas */
        .footer-col {
            flex: 1;
            min-width: 250px;
        }
        
        .footer-col h4 {
            color: #1a1a1a !important;
            font-weight: 800 !important;
            font-size: 1.1rem !important;
            margin-bottom: 20px !important;
            letter-spacing: 0.5px;
        }
        
        .footer-col p {
            color: #666 !important;
            font-size: 0.95rem !important;
            line-height: 1.6;
        }

        /* Iconos de Redes */
        .social-links {
            display: flex;
            gap: 20px;
            margin-top: 10px;
        }
        
        .social-links a {
            color: #444 !important;
            font-size: 1.5rem;
            transition: color 0.3s ease;
            text-decoration: none !important;
        }
        
        .social-links a:hover {
            color: #007bff !important; /* Un toque de color al pasar el mouse */
        }

        /* Botón WhatsApp */
        .whatsapp-btn {
            position: fixed; 
            bottom: 30px; 
            right: 30px; /* Movido a la derecha, suele ser más estándar */
            background-color: #25d366; 
            color: white !important;
            width: 60px; 
            height: 60px; 
            border-radius: 50%;
            display: flex; 
            align-items: center; 
            justify-content: center;
            font-size: 32px; 
            z-index: 99999;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            text-decoration: none !important;
            animation: pulse-green 2s infinite;
        }

        @keyframes pulse-green {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { transform: scale(1.05); box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
        </style>
        
        <div class="footer-container">
            <div class="footer-col">
                <h4>SERRANO TURISMO</h4>
                <p>29 años de trayectoria impecable brindando experiencias inolvidables.</p>
                <p style="font-size:0.8rem !important; margin-top:20px; color:#999 !important;">
                    © 2026 Todos los derechos reservados.
                </p>
            </div>
            
            <div class="footer-col">
                <h4>CONTACTO</h4>
                <p>
                    📍 <b>CABA:</b> Av. Rivadavia 4532<br>
                    📍 <b>Ituzaingó:</b> Parque Leloir<br>
                    📍 <b>San Pedro:</b> Costanera<br>
                    📞 11-4847-6467
                </p>
            </div>
            
            <div class="footer-col">
                <h4>SEGUINOS</h4>
                <div class="social-links">
                    <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook-f"></i></a>
                </div>
            </div>
        </div>
        
        <a href="https://wa.me/5491156096283" class="whatsapp-btn" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
