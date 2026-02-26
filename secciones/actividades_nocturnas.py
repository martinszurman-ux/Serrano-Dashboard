import streamlit as st

def render_nocturnas(destino):
    st.markdown(f'<div class="header-container"><div class="header-text-overlay">NOCHE - {destino.upper()}</div></div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="widget-3d-grad">
            <div style="font-size: 3rem;">🕺</div>
            <p class='widget-title'>Eventos y Discotecas</p>
            <p style="color: #6c757d;">
                Ingresos exclusivos a las mejores discotecas. Fiestas temáticas (Disfraz, Flúor, Gala) 
                con coordinación permanente y seguridad privada.
            </p>
        </div>
    """, unsafe_allow_html=True)
