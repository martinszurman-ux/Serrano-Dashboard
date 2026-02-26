import streamlit as st

def render_excursiones(destino):
    st.markdown(f'<div class="header-container"><div class="header-text-overlay">EXCURSIONES - {destino.upper()}</div></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    if destino == "Villa Carlos Paz":
        exc1, icon1 = "Mundo Cocoguana (Parque Acuático)", "💦"
        exc2, icon2 = "Peko's Multiparque", "🎢"
    else:
        exc1, icon1 = "La Campiña de Mónica y César", "🍊"
        exc2, icon2 = "Vuelta al Obligado (Histórica)", "⚔️"

    with col1:
        st.markdown(f'<div class="widget-3d-grad"><div style="font-size: 3rem;">{icon1}</div><p class="widget-title">{exc1}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="widget-3d-grad"><div style="font-size: 3rem;">{icon2}</div><p class="widget-title">{exc2}</p></div>', unsafe_allow_html=True)
