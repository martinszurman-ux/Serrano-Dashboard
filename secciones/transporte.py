import streamlit as st

def render_transporte(destino):
    st.markdown(f'<div class="header-container"><div class="header-text-overlay">TRANSPORTE - {destino.upper()}</div></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="widget-3d-grad" style="min-height: 320px;">
                <div style="font-size: 3rem;">🚌</div>
                <p class='widget-title'>Buses de Última Generación</p>
                <p style="color: #6c757d; font-size: 0.9rem;">
                    Unidades Mix (Semi-cama y Cama) con aire acondicionado, bar, baño y monitoreo permanente vía <b>GPS</b>. 
                    Viaje íntegramente por Autopista 9, sin rebotes y viajando de día.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="widget-3d-grad" style="min-height: 320px;">
                <div style="font-size: 3rem;">✈️</div>
                <p class='widget-title'>Opción Aérea</p>
                <p style="color: #6c757d; font-size: 0.9rem;">
                    Vuelos exclusivos con <b>Aerolíneas Argentinas</b>. Incluye transfer in-out desde el aeropuerto 
                    y transporte receptivo en destino durante toda la estadía.
                </p>
            </div>
        """, unsafe_allow_html=True)
