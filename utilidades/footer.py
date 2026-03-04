import streamlit as st

def render_footer():
    """Renderiza el footer con direcciones centradas y WhatsApp flotante real"""
    
    # Inyectamos TODO vía markdown para evitar que el iframe bloquee el botón de WhatsApp
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            /* 1. Limpieza de márgenes de Streamlit */
            .main .block-container { padding-bottom: 2rem !important; }
            footer { display: none !important; }

            /* 2. Contenedor del Footer */
            .custom-footer {
                background-color: #ffffff;
                border-top: 1px solid #eeeeee;
                padding: 30px 5%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                gap: 20px;
                margin-top: 50px;
            }

            .footer-col { flex: 1; min-width: 200px; }

            /* 3. Estilo de Marca (Gris Oscuro) */
            .brand-name {
                color: #333333 !important;
                font-weight: 800 !important;
                font-size: 1.1rem !important;
                margin: 0 !important;
                text-transform: uppercase;
            }
            .brand-sub { color: #888; font-size: 0.85rem; margin-top: 5px; }

            /* 4. DIRECCIONES CENTRADAS (Corrección definitiva) */
            .address-center {
                flex: 2;
                text-align: center;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .address-center p {
                margin: 4px 0 !important;
                color: #555 !important;
                font-size: 0.9rem !important;
                line-height: 1.4;
            }
            .icon-red { color: #d9534f; margin-right: 8px; }

            /* 5. Redes Sociales */
            .social-right { text-align: right; }
            .social-right a {
                color: #333 !important;
                font-size: 1.5rem;
                margin-left: 20px;
                text-decoration: none !important;
                transition: transform 0.3s;
            }
            .social-right a:hover { transform: scale(1.2); }

            /* 6. WHATSAPP FLOTANTE CON ANIMACIÓN */
            .wa-float {
                position: fixed;
                bottom: 30px;
                left: 30px;
                background-color: #25d366;
                color: white !important;
                width: 60px;
                height: 60px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 30px;
                z-index: 999999;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                text-decoration: none !important;
                animation: slideLeft 0.8s ease-out, pulseGreen 2s infinite;
            }

            @keyframes slideLeft {
                from { opacity: 0; transform: translateX(-50px); }
                to { opacity: 1; transform: translateX(0); }
            }
            @keyframes pulseGreen {
                0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
                70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
                100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
            }

            /* Responsive */
            @media (max-width: 768px) {
                .custom-footer { flex-direction: column; text-align: center; }
                .address-center, .social-right { text-align: center; }
                .social-right a { margin: 0 10px; }
            }
        </style>

        <div class="custom-footer">
            <div class="footer-col">
                <h4 class="brand-name">SERRANO TURISMO</h4>
                <p class="brand-sub">29 años de trayectoria. © 2026</p>
            </div>

            <div class="footer-col address-center">
                <p><i class="fas fa-map-marker-alt icon-red"></i> Av. Rivadavia 4532 - Galería Alefa (Local 10) - CABA</p>
                <p><i class="fas fa-map-marker-alt icon-red"></i> Del Cimarrón 1846 - 1er Piso (Of. 4) - Parque Leloir</p>
                <p><i class="fas fa-phone-alt"></i> 11-4847-6467</p>
            </div>

            <div class="footer-col social-right">
                <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
                <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook-f"></i></a>
            </div>
        </div>

        <a href="https://wa.me/5491156096283" class="wa-float" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
