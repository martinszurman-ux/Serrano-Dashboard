# --- SECCIÓN 1: SELECCIONÁ TU ITINERARIO (ESTILO CARRUSEL) ---
        st.write("### 📅 Seleccioná tu itinerario")
        
        # Usamos un contenedor con scroll horizontal si hay muchos
        items_html = ""
        for i, plan in enumerate(planes):
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) > 1 else ""
            icono = "🚌" if "bus" in plan.lower() else "✈️"
            
            es_activo = st.session_state[session_key] == i
            clase_card = "selected-plan" if es_activo else ""
            
            # Generamos el HTML de cada tarjeta para el contenedor
            items_html += f"""
            <div class="plan-card-container {clase_card}" style="min-width: 200px; margin-right: 15px;">
                <div class="header-content">
                    <span class="day-number">{numero}</span>
                    <span class="transport-icon">{icono}</span>
                </div>
                <div class="day-text">{resto}</div>
            </div>
            """

        # Inyectamos el contenedor con scroll horizontal
        st.markdown(f"""
            <div style="display: flex; overflow-x: auto; padding: 20px 10px; width: 100%; -webkit-overflow-scrolling: touch;">
                {items_html}
            </div>
        """, unsafe_allow_html=True)

        # Botones de selección abajo (para que Python capture el click)
        cols_btn = st.columns(len(planes))
        for i in range(len(planes)):
            with cols_btn[i]:
                if st.button(f"Elegir {i+1}", key=f"btn_sel_{i}", use_container_width=True):
                    st.session_state[session_key] = i
                    st.rerun()
