import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # CSS Mejorado: Integración total y eliminación de botones visibles
    st.markdown("""
        <style>
        /* Widget de Selección de Plan (Días en Rojo) */
        .plan-card-click {
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            background: white;
            border: 2px solid #eee;
            transition: all 0.3s ease;
            min-height: 140px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        .selected-plan { border: 3px solid #d32f2f !important; background-color: #fff5f5 !important; }
        
        .day-number { color: #d32f2f; font-size: 3.5rem; font-weight: 900; line-height: 1; margin-bottom: 0; }
        .day-text { color: #495057; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; }

        /* Widget 3D Hundido (Neumórfico) para montos y opciones */
        .widget-3d-inner {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 15px;
            padding: 15px;
            text-align: center;
            border: 1px solid #ddd;
            box-shadow: inset 3px 3px 6px #d1d1d1, inset -3px -3px 6px #ffffff;
            min-height: 130px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        /* Ocultar el texto de los botones de selección pero mantener su funcionalidad */
        .stButton button {
            background-color: transparent !important;
            border: none !important;
            color: transparent !important;
            height: 140px !important;
            width: 100% !important;
            position: absolute;
            top: 0; left: 0;
            z-index: 10;
        }
        .stButton button:hover { background-color: rgba(0,0,0,0.02) !important; }
        
        /* Ajuste para que las Pills se vean bien dentro del widget */
        div[data-testid="stPills"] {
            background: transparent !important;
            padding: 0 !important;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        
        st.write("### 📅 Seleccioná tu itinerario")
        
        if f'sel_{folder}' not in st.session_state:
            st.session_state[f'sel_{folder}'] = 0

        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))

        for i, plan in enumerate(planes):
            # Extraer número y transporte (ej: "6 dias en bus")
            # Basado en 
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) > 1 else "Días"
            icono = "🚌" if "bus" in plan.lower() else "✈️"

            with cols_p[i]:
                es_activo = st.session_state[f'sel_{folder}'] == i
                clase_activa = "selected-plan" if es_activo else ""
                
                # Capa visual
                st.markdown(f"""
                    <div class="plan-card-click {clase_activa}">
                        <div class="day-number">{numero}</div>
                        <div class="day-text">{resto}</div>
                        <div style="font-size: 1.2rem;">{icono}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # El botón ahora es invisible y cubre toda la tarjeta
                if st.button(f"Invisible_{i}", key=f"inv_{folder}_{i}"):
                    st.session_state[f'sel_{folder}'] = i
                    st.rerun()

        v = df.iloc[st.session_state[f'sel_{folder}']]
        st.divider()

        # --- SECCIÓN DE WIDGETS 3D NIVELADOS ---
        col_opc, col_monto, col_cash = st.columns(3)

        def clean(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        # Widget 1: OPCIONES DE PAGO INTEGRADAS
        with col_opc:
            st.markdown('<div class="widget-3d-inner">', unsafe_allow_html=True)
            st.markdown("<p class='widget-title' style='margin-bottom:10px;'>Opciones de Pago</p>", unsafe_allow_html=True)
            cols_cuponera = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            cuota_sel = st.pills("Selector", options=cols_cuponera, default=cols_cuponera[0], label_visibility="collapsed", key=f"pill_{folder}")
            st.markdown('</div>', unsafe_allow_html=True)

        c_db = cuota_sel.replace(' ', '_')
        val_cuota = clean(v[c_db])
        val_contado = clean(v['Contado'])

        # Widget 2: MONTO DINÁMICO
        with col_monto:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class='widget-title'>Monto {cuota_sel}</p>
                    <p class='widget-value'>${val_cuota:,.0f}</p>
                    <p class='promo-subtitle'>Cuota fija en pesos</p>
                </div>
            """, unsafe_allow_html=True)

        # Widget 3: EFECTIVO (OFICINA)
        with col_cash:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class='widget-title'>💎 Efectivo (Oficina)</p>
                    <p class='widget-value' style='color: #495057;'>${val_contado * 0.9:,.0f}</p>
                    <p class='promo-subtitle'>Bonificación 10% incluida</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver tarifario detallado"):
            st.table(df.set_index('Programa'))
        
        # Nota sobre flexibilidad [cite: 120, 250, 391]
        st.info("Nota: Se pueden pautar otros planes en base a lo que cada familia necesite.")
    else:
        st.error("Error: No se pudo cargar el archivo de tarifas.")
