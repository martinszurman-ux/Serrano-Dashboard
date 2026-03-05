import streamlit as st

def render_footer():
    """Versión blindada: Oculta Streamlit, centra direcciones y arregla WhatsApp"""
    
    # 1. CSS de Limpieza y Estilo (Separado para evitar errores de renderizado)
    st.markdown("""
        <style>
            /* ELIMINAR MARCAS DE STREAMLIT */
            #MainMenu {visibility: hidden;}
            footer {display: none !important;}
            header {visibility: hidden;}
            .stApp [data-testid="stToolbar"] {display: none;}
            
            /* CONTENEDOR FOOTER */
            .footer-final {
                background-color: white;
                border-top: 1px solid #eee;
                padding: 30px 20px;
                margin-top: 50px;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                align-items: center;
                gap: 20px;
            }

            .f-item { flex: 1; min-width: 200px; }

            /* TEXTOS */
            .f-brand-text {
                color: #333333 !important;
                font-weight: 800;
                font-size: 1.1rem;
                margin: 0;
                text-transform: uppercase;
            }
            
            /* CENTRADO DE DIRECCIONES */
            .f-center {
                flex: 2;
                text-align: center;
                color: #666;
                font-size: 0.9rem;
            }
            .f-center p { margin: 5px 0 !important; }

            /* WHATSAPP IZQUIERDA REAL */
            .wa-float-new {
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
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                text-decoration: none !important;
            }
        </style>
        
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True)

    # 2. ESTRUCTURA HTML (Simple y robusta)
    st.markdown(f"""
        <div class="footer-final">
            <div class="f-item">
                <p class="f-brand-text">SERRANO TURISMO</p>
                <p style="color:#999; font-size:0.8rem; margin-top:5px;">29 años de trayectoria. © 2026</p>
            </div>
            
            <div class="f-item f-center">
                <p>📍 Av. Rivadavia 4532 - Galería Alefa (Local 10) - CABA</p>
                <p>📍 Del Cimarrón 1846 - 1er Piso (Of. 4) - Parque Leloir</p>
                <p>📞 11-4847-6467</p>
            </div>
            
            <div class="f-item" style="text-align:right;">
                <a href="https://instagram.com/serrano_turismo" target="_blank" style="color:#333; font-size:1.5rem; margin-left:15px;"><i class="fab fa-instagram"></i></a>
                <a href="https://facebook.com/serranoturismo" target="_blank" style="color:#333; font-size:1.5rem; margin-left:15px;"><i class="fab fa-facebook-f"></i></a>
            </div>
        </div>

        <a href="https://wa.me/5491156096283" class="wa-float-new" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
