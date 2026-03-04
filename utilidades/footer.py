import streamlit as st
import streamlit.components.v1 as components

def render_footer():
    """Renderiza un footer ultra-compacto y el botón de WhatsApp animado a la izquierda"""
    
    # CSS para eliminar el espacio en blanco que Streamlit deja abajo por defecto
    st.markdown("""
        <style>
        .main .block-container {
            padding-bottom: 1rem !important;
        }
        /* Animación del botón de WhatsApp */
        @keyframes slideInLeft {
            from { opacity: 0; transform: translateX(-50px); }
            to { opacity: 1; transform: translateX(0); }
        }
        @keyframes pulse-green {
            0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
            100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }

        .wa-link {
            position: fixed; 
            bottom: 30px; 
            left: 30px; /* Movido a la izquierda */
            background-color: #25d366; 
            color: white !important;
            width: 55px; height: 55px; 
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 28px; 
            z-index: 99999; 
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            text-decoration: none !important;
            animation: slideInLeft 0.8s ease-out, pulse-green 2s infinite;
        }
        .wa-link:hover {
            transform: scale(1.1);
            transition: 0.3s;
        }
        </style>
        <a href="https://wa.me/5491156096283" class="wa-link" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)

    footer_html = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { 
            margin: 0; 
            padding: 0;
            font-family: 'Source Sans Pro', sans-serif; 
            overflow: hidden; /* Evita scroll interno del iframe */
        }
        .footer-wrapper {
            background-color: #ffffff;
            border-top: 1px solid #f0f0f0;
            padding: 15px 40px;
            display: grid;
            grid-template-columns: 1.5fr 1.5fr 1fr;
            align-items: center;
            color: #444;
        }
        .col h4 {
            color: #1a1a1a;
            margin: 0;
            font-size: 13px;
            text-transform: uppercase;
            font-weight: 700;
        }
        .col p {
            margin: 2px 0;
            font-size: 12px;
            color: #777;
        }
        .socials { display: flex; gap: 15px; justify-content: flex-end; }
        .socials a {
            color: #333;
            font-size: 18px;
            text-decoration: none;
        }
        @media (max-width: 600px) {
            .footer-wrapper { 
                grid-template-columns: 1fr; 
                text-align: center; 
                padding: 10px;
            }
            .socials { justify-content: center; margin-top: 10px; }
        }
    </style>
    
    <div class="footer-wrapper">
        <div class="col">
            <h4>Serrano Turismo</h4>
            <p>29 años de trayectoria. © 2026</p>
        </div>
        <div class="col">
            <p>📍 CABA | Leloir | San Pedro</p>
            <p>📍 Av. Rivadavia 4532 - Galería Alefa (local 10) C1042AAP - C.A.B.A.</p>
            <p>📍 Del Cimarrón 1846 - 1er Piso - Of. 4 C.P.: 1714 - Parque Leloir Ituzaingo</p>            
            <p>📞 11-4847-6467</p>
        </div>
        <div class="col">
            <div class="socials">
                <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
                <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook-f"></i></a>
            </div>
        </div>
    </div>
    """
    
    # Reducimos el height a 80px para que sea una línea discreta
    components.html(footer_html, height=80)
