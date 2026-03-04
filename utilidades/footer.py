import streamlit as st
import streamlit.components.v1 as components

def render_footer():
    """Renderiza el footer institucional y el botón de WhatsApp unificados"""
    
    # Inyectamos CSS global para quitar el margen de Streamlit en todas las páginas
    st.markdown("""
        <style>
        .main .block-container { padding-bottom: 0rem !important; }
        footer {display: none !important;} /* Oculta el footer por defecto de Streamlit */
        </style>
    """, unsafe_allow_html=True)

    footer_html = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <style>
        body { 
            margin: 0; padding: 0;
            font-family: 'Source Sans Pro', sans-serif; 
            background-color: transparent;
        }
        
        .footer-wrapper {
            background-color: #ffffff;
            border-top: 1px solid #f0f0f0;
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #444;
        }

        .col-info { flex: 2; }
        .col-address { flex: 3; text-align: center; }
        .col-social { flex: 1; text-align: right; }

        h4 {
            color: #333333 !important; /* Gris oscuro para el título */
            margin: 0;
            font-size: 14px;
            text-transform: uppercase;
            font-weight: 800;
        }

        p {
            margin: 2px 0;
            font-size: 11px;
            color: #777;
            line-height: 1.3;
        }

        .socials a {
            color: #333;
            font-size: 20px;
            margin-left: 15px;
            text-decoration: none;
            transition: 0.3s;
        }

        /* BOTÓN WHATSAPP INTEGRADO */
        .wa-float {
            position: fixed;
            bottom: 20px;
            left: 20px;
            background-color: #25d366;
            color: white !important;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 25px;
            z-index: 9999;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            text-decoration: none !important;
            animation: slideIn 0.8s ease-out, pulse 2s infinite;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-30px); }
            to { opacity: 1; transform: translateX(0); }
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { box-shadow: 0 0 0 12px rgba(37, 211, 102, 0); }
            100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }

        @media (max-width: 768px) {
            .footer-wrapper { flex-direction: column; text-align: center; padding: 10px; }
            .col-social { text-align: center; margin-top: 10px; }
            .col-address { margin: 10px 0; }
        }
    </style>
    
    <div class="footer-wrapper">
        <div class="col-info">
            <h4>SERRANO TURISMO</h4>
            <p>29 años de trayectoria impecable. © 2026</p>
        </div>
        
        <div class="col-address">
            <p>📍 Av. Rivadavia 4532 - Galería Alefa (local 10) - C.A.B.A.</p>
            <p>📍 Del Cimarrón 1846 - Of. 4 - Parque Leloir</p>
            <p>📞 11-4847-6467</p>
        </div>
        
        <div class="col-social">
            <div class="socials">
                <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
                <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook-f"></i></a>
            </div>
        </div>
    </div>

    <a href="https://wa.me/5491156096283" class="wa-float" target="_blank">
        <i class="fab fa-whatsapp"></i>
    </a>
    """
    
    # Aumentamos un poquito a 100px para que las direcciones no se corten
    components.html(footer_html, height=100)
