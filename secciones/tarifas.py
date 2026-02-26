import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # CSS para los nuevos widgets de selección y 3D mejorados
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
            cursor: pointer;
            min-height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .plan-card-click:hover { transform: translateY(-5px); border-color: #d32f2f; }
        .selected-plan { border: 3px solid #d32f2f !important; background-color: #fff5f5 !important; }
        
        .day-number { color: #d32f2f; font-size: 3.5rem; font-weight: 900; line-height: 1; margin-bottom: 0; }
        .day-text { color: #495057; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; }
        .transport-icon { font-size: 1.5rem; margin-top: 5px; }

        /* Widget 3D con Degradado Interno (Para los montos) */
        .widget-3d-inner {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            border: 1px solid #ddd;
            box-shadow: inset 2px 2px 5px #d1d1d1, inset -2px -2px 5px #ffffff, 5px 5px 10px #e6e6e6;
            height: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        
        # --- SELECTORES DE PLANES TIPO BOTÓN ---
        st.write("### 📅 Seleccioná tu itinerario")
        
        if f'sel_{folder}' not in st.session_state:
            st.session_state[f'sel_{folder}'] = 0

        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))

        for i, plan in enumerate(planes):
            # Extraer número y tipo (ej: "6 dias en bus" -> "6" y "dias en bus")
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) > 1 else ""
            icono = "🚌" if "bus" in plan.lower() else "✈️"

            with cols_p[i]:
                es_activo = st.session_state[f'sel_{folder}'] == i
                clase_activa = "selected-plan" if es_activo else ""
                
                # Render visual del widget
                st.markdown(f"""
                    <div class="plan-card-click {clase_activa}">
                        <div class="day-number">{numero}</div>
                        <div class="day-text">{resto}</div>
                        <div class="transport-icon">{icono}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botón invisible para capturar el click
                if st.button(f"Elegir {i}", key=f"btn_{folder}_{i}", use_container_width=True):
                    st.session_state[f'sel_{folder}'] = i
                    st.rerun()

        # Datos del plan seleccionado
        v = df.iloc[st.session_state[f'sel_{folder}']]
        
        st.divider()

        # --- WIDGETS DE MONTO (AHORA CON OPCIONES DENTRO) ---
        col_opc, col_monto, col_cash = st.columns(3)

        def to_n(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        # Widget 1: OPCIONES DE PAGO (Metido adentro del 3D)
        with col_opc:
            st.markdown('<div class="widget-3d-inner">', unsafe_allow_html=True)
            st.markdown("<p class='widget-title'>Opciones de Pago</p>", unsafe_allow_html=True)
            cols_c = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            cuota_sel = st.pills("Planes", options=cols_c, default=cols_c[0], label_visibility="collapsed", key=f"p_{folder}")
            st.markdown('</div>', unsafe_allow_html=True)

        c_db = cuota_sel.replace(' ', '_')
        val_c = to_n(v[c_db])
        val_cont = to_n(v['Contado'])

        # Widget 2: MONTO DINÁMICO
        with col_monto:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class='widget-title'>Monto {cuota_sel}</p>
                    <p class='widget-value'>${val_c:,.0f}</p>
                    <p class='promo-subtitle'>Cuota fija en pesos</p>
                </div>
            """, unsafe_allow_html=True)

        # Widget 3: EFECTIVO
        with col_cash:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class='widget-title'>💎 Efectivo (Oficina)</p>
                    <p class='widget-value' style='color: #2e7d32;'>${val_cont * 0.9:,.0f}</p>
                    <p class='promo-subtitle'>Bonificación 10% incluida</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver tarifario completo"):
            st.table(df.set_index('Programa'))
    else:
        st.error("No se encontró el archivo de datos.")
