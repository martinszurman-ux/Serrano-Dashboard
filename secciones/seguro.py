import streamlit as st

def render_seguro():
    st.markdown("""
        <style>
        .med-container {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 20px; padding: 25px; text-align: center;
            border: 1px solid #e0e0e0; box-shadow: 8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff;
            margin-bottom: 15px; min-height: 380px; display: flex;
            flex-direction: column; justify-content: center; align-items: center;
        }
        .med-icon { font-size: 4rem; margin-bottom: 20px; }
        .med-title { color: #495057; font-size: 1.2rem; font-weight: 800; text-transform: uppercase; margin-bottom: 15px; min-height: 50px; display: flex; align-items: center; }
        .med-text { color: #6c757d; font-size: 0.95rem; line-height: 1.5; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align: center; padding: 20px; background: #f8f9fa; border-radius: 20px; border: 1px solid #eee; margin-bottom: 30px;">
            <img src="https://assistravel.com/web/image/website/1/logo/Assistravel?unique=966a426" width="280">
            <h2 style="color: #495057; font-weight: 800; margin-top: 15px;">COBERTURA MÉDICA NACIONAL</h2>
        </div>
    """, unsafe_allow_html=True)

    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.markdown('<div class="med-container"><div class="med-icon">🏥</div><div class="med-title">Asistencia en Destino</div><p class="med-text">Atención primaria y especialistas las 24 hs.</p></div>', unsafe_allow_html=True)
    with col_m2:
        st.markdown('<div class="med-container"><div class="med-icon">💊</div><div class="med-title">Servicio de Farmacia</div><p class="med-text">Cobertura completa en medicamentos recetados.</p></div>', unsafe_allow_html=True)
    with col_m3:
        st.markdown('<div class="med-container"><div class="med-icon">🛡️</div><div class="med-title">Seguro de Accidentes</div><p class="med-text">Responsabilidad Civil y Accidentes Personales.</p></div>', unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 📲 Control y Seguimiento en Tiempo Real (App Viaxlab)")
