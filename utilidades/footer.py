import streamlit as st
import streamlit.components.v1 as components

def render_footer():
    """Renderiza un footer compacto y profesional usando un componente aislado"""
    
    footer_html = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { margin: 0; font-family: 'Source Sans Pro', sans-serif; }
        .footer-wrapper {
            background-color: #ffffff;
            border-top: 1px solid #eeeeee;
            padding: 20px 40px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            color: #444;
        }
        .col h4 {
            color: #1a1a1a;
            margin: 0 0 10px 0;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .col p {
            margin: 3px 0;
            font-size: 13px;
            color: #666;
            line-height: 1.4;
        }
        .socials { margin-top: 10px; }
        .socials a {
            color: #333;
            font-size: 18px;
            margin-right: 15px;
            text-decoration: none;
        }
        @media (max-width: 600px) {
            .footer-wrapper { grid-template-columns: 1fr; text-align: center; }
        }
    </style>
    
    <div class="footer-wrapper">
        <div class="col">
            <h4>Serrano Turismo</h4>
            <p>29 años de trayectoria.</p>
            <p style="font-size: 11px; color: #999;">© 2026 Reservados.</p>
        </div>
        <div class="col">
            <h4>Contacto</h4>
            <p>📍 CABA | Parque Leloir | San Pedro</p>
            <p>📞 11-4847-6467</p>
        </div>
        <div class="col">
            <h4>Seguinos</h4>
            <div class="socials">
                <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
                <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook-f"></i></a>
            </div>
        </div>
    </div>
    """
    
    # El height controla qué tan "gigante" se ve. 150px es compacto.
    components.html(footer_html, height=150)

    # El botón de WhatsApp lo dejamos fuera del componente para que flote sobre toda la app
    st.markdown("""
        <style>
        .wa-link {
            position: fixed; bottom: 30px; right: 30px;
            background-color: #25d366; color: white !important;
            width: 55px; height: 55px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 28px; z-index: 9999; box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            text-decoration: none !important;
        }
        </style>
        <a href="https://wa.me/5491156096283" class="wa-link" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
