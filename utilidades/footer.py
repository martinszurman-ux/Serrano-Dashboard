import streamlit as st
import streamlit.components.v1 as components

def render_footer():
    """Renderiza el footer institucional con direcciones centradas y WhatsApp flotante"""
    
    # 1. Inyectamos la librería de iconos y el estilo del botón flotante en la APP GLOBAL
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
        /* Eliminar márgenes de Streamlit */
        .main .block-container { padding-bottom: 0rem !important; }
        footer {display: none !important;}

        /* Botón WhatsApp Flotante y Animado */
        .wa-float-global {
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
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            text-decoration: none !important;
            animation: slideInLeft 0.8s ease-out, pulse-green 2s infinite;
        }

        @keyframes slideInLeft {
            from { opacity: 0; transform: translateX(-50px); }
            to { opacity: 1; transform: translateX(0); }
        }
        @keyframes pulse-green {
            0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
            100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
        </style>
        
        <a href="https://wa.me/5491156096283" class="wa-float-global" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)

    # 2. El Footer (contenido estático)
    footer_html = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { margin: 0; padding: 0; font-family: sans-serif; background-color: white; }
        .footer-container {
            border-top: 1px solid #eee;
            padding: 20px 40px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .col { flex: 1; }
        
        /* Estilo para SERRANO TURISMO en gris oscuro */
        .brand h4 { 
            color: #333333; 
            margin: 0; 
            font-size: 14px; 
            font-weight: 800;
            text-transform: uppercase;
        }
        .brand p { color: #888; font-size: 11px; margin: 2px 0; }

        /* Centrado perfecto de direcciones */
        .address { 
            flex: 2; 
            text-align: center; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
        }
        .address p { 
            color: #666; 
            font-size: 11.5px; 
            margin: 2px 0; 
            white-space: nowrap; 
        }

        .socials { text-align: right; }
        .socials a { color: #333; font-size: 18px; margin-left: 15px; text-decoration: none; }
        
        @media (max-width: 800px) {
            .footer-container { flex-direction: column; text-align: center; gap: 10px; }
            .address { white-space: normal; }
            .socials { text-align: center; }
        }
    </style>
    
    <div class="footer-container">
        <div class="col brand">
            <h4>SERRANO TURISMO</h4>
            <p>29 años de trayectoria. © 2026</p>
        </div>
        
        <div class="address">
            <p><i class="fas fa-map-marker-alt" style="color:#d9534f"></i> Av. Rivadavia 4532 - Galería Alefa (local 10) - C.A.B.A.</p>
            <p><i class="fas fa-map-marker-alt" style="color:#d9534f"></i> Del Cimarrón 1846 - 1er Piso - Of. 4 - Parque Leloir</p>
            <p><i class="fas fa-phone-alt"></i> 11-4847-6467</p>
        </div>
        
        <div class="col socials">
            <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
            <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook-f"></i></a>
        </div>
    </div>
    """
    
    # Ajustamos el alto para que no sobre espacio pero quepan las 3 líneas
    components.html(footer_html, height=110)
