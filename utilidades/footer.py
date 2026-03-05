import streamlit as st

def render_footer():
    """
    Renderiza el footer institucional, el botón de WhatsApp flotante 
    y elimina por completo los elementos de marca de Streamlit.
    """
    
    # CSS para ocultar 'Hosted with Streamlit', el menú de hamburguesa y el header
    st.markdown("""
        <style>
            /* Ocultar elementos nativos de Streamlit */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Ajuste para eliminar el espacio en blanco que deja el footer oculto */
            .main .block-container {
                padding-bottom: 1rem !important;
            }

            /* Estilos del Footer Personalizado */
            .custom-footer {
                background-color: #ffffff;
                border-top: 1px solid #f0f2f6;
                padding: 30px 40px;
                margin-top: 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                width: 100%;
                box-sizing: border-box;
                font-family: 'Source Sans Pro', sans-serif;
            }

            .f-col { flex: 1; min-width: 250px; margin: 10px 0; }

            /* Marca - Gris Oscuro */
            .f-brand h4 {
                color: #333333 !important;
                font-weight: 800 !important;
                font-size: 1.1rem !important;
                margin: 0 !important;
                text-transform: uppercase;
            }
            .f-brand p { color: #888; font-size: 0.85rem; margin-top: 5px; }

            /* Direcciones Centradas */
            .f-address {
                flex: 2;
                text-align: center;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .f-address p {
                color: #555 !important;
                font-size: 0.9rem !important;
                margin: 4px 0 !important;
                line-height: 1.2 !important;
            }
            .f-address i { color: #d9534f; margin-right: 8px; }

            /* Redes Sociales */
            .f-social { text-align: right; }
            .f-social a {
                color: #333 !important;
                font-size: 1.6rem;
                margin-left: 20px;
                text-decoration: none !important;
                transition: 0.3s;
            }
            .f-social a:hover { color: #E1306C !important; }

            /* WhatsApp Flotante a la Izquierda */
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
                box-shadow: 0 4px 15px rgba(0,0,0,0.25);
                text-decoration: none !important;
                animation: slideFromLeft 0.8s ease-out, pulseWa 2s infinite;
            }

            @keyframes slideFromLeft {
                from { opacity: 0; transform: translateX(-60px); }
                to { opacity: 1; transform: translateX(0); }
            }
            @keyframes pulseWa {
                0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
                70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
                100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
            }

            @media (max-width: 768px) {
                .custom-footer { flex-direction: column; text-align: center; }
                .f-social, .f-address { text-align: center; }
                .f-social a { margin: 10px; }
            }
        </style>

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

        <div class="custom-footer">
            <div class="f-col f-brand">
                <h4>SERRANO TURISMO</h4>
                <p>29 años de trayectoria. © 2026</p>
            </div>

            <div class="f-col f-address">
                <p><i class="fas fa-map-marker-alt"></i> Av. Rivadavia 4532 - Galería Alefa (Local 10) - CABA</p>
                <p><i class="fas fa-map-marker-alt"></i> Del Cimarrón 1846 - 1er Piso (Of. 4) - Parque Leloir</p>
                <p><i class="fas fa-phone-alt" style="color:#555"></i> 11-4847-6467</p>
            </div>

            <div class="f-col f-social">
                <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
                <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook-f"></i></a>
            </div>
        </div>

        <a href="https://wa.me/5491156096283" class="wa-float" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
