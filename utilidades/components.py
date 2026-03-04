# utils.py
import streamlit as st

def render_footer():
    """Renderiza el footer institucional de Serrano Turismo"""
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        .footer-full {
            background-color: #1a1a1a;
            color: white;
            padding: 60px 8% 80px 8%;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 40px;
            margin-bottom: -100px !important;
        }
        
        /* WhatsApp a la izquierda */
        .whatsapp-btn {
            position: fixed; bottom: 30px; left: 30px; 
            background-color: #25d366; color: white !important;
            width: 60px; height: 60px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 32px; z-index: 9999;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            text-decoration: none !important;
            animation: pulse-green 2s infinite;
        }

        @keyframes pulse-green {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { transform: scale(1.05); box-shadow: 0 0 0 20px rgba(37, 211, 102, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
        </style>
        
        <div class="footer-full">
            <div style="flex:1; min-width:280px;">
                <h4 style="margin-bottom:20px; font-weight:700; color:white;">SERRANO TURISMO</h4>
                <p style="color:#aaa; font-size:0.9rem;">29 años de trayectoria impecable.</p>
            </div>
            <div style="flex:1; min-width:280px;">
                <h4 style="margin-bottom:20px; font-weight:700; color:white;">CONTACTO</h4>
                <p style="color:#aaa; font-size:0.9rem;">📍 CABA: Av. Rivadavia 4532<br>📍 Ituzaingó: Parque Leloir<br>📞 11-4847-6467</p>
            </div>
            <div style="flex:1; min-width:200px;">
                <h4 style="margin-bottom:20px; font-weight:700; color:white;">REDES</h4>
                <div style="display:flex; gap:20px;">
                    <a href="https://instagram.com/serrano_turismo" target="_blank" style="color:white; font-size:1.8rem;"><i class="fab fa-instagram"></i></a>
                    <a href="https://facebook.com/serranoturismo" target="_blank" style="color:white; font-size:1.8rem;"><i class="fab fa-facebook-f"></i></a>
                </div>
            </div>
        </div>
        
        <a href="https://wa.me/5491156096283" class="whatsapp-btn" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
