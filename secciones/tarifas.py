import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # Función de actualización de estado
    def seleccionar_plan(indice):
        st.session_state[f"sel_index_{folder}"] = indice

    # CSS Refinado para integración total y marca JEO
    st.markdown("""
        <style>
        .plan-card-click {
            border-radius: 15px; padding: 15px; background: white;
            border: 2px solid #eee; transition: all 0.3s ease;
            min-height: 140px; position: relative;
            display: flex; flex-direction: column; justify-content: center;
        }
        .selected-plan { 
            border: 3px solid #d32f2f !important; 
            background-color: #fff5f5 !important;
        }
        .card-top {
            display: flex; justify-content: center; align-items: center;
            gap: 12px; margin-bottom: 5px;
        }
        .day-number { color: #d32f2f; font-size: 3.2rem; font-weight: 900; line-height: 1; }
        .transport-icon-big { font-size: 2.5rem; }
        .day-text-bottom { 
            color: #495057; font-size: 0.85rem; font-weight: 700; 
            text-transform: uppercase; text-align: center;
        }

        /* Botón transparente */
        .stButton button {
            background-color: transparent !important; border: none !important;
            color: transparent !important; height: 140px !important;
            width: 100% !important; position: absolute; top: 0; left: 0;
            z-index: 10; cursor: pointer;
        }

        /* WIDGET 3D INTEGRADO */
        .widget-3d-inner {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 15px; 
            padding: 20px; 
            text-align: center;
            border: 1px solid #ddd;
            box-shadow: inset 3px 3px 6px #d1d1d1, inset -3px -3px 6px #ffffff;
            min-height: 160px;
            display: flex; 
            flex-direction: column; 
            justify-content: center;
            align-items: center;
        }
        
        /* Marca JEO */
        .jeo-mark {
            font-size: 5rem;
            font-weight: 900;
            color: rgba(0,0,0,0.05);
            text-align: center;
            margin: 20px 0;
            letter-spacing: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        st.write("### 📅 Seleccioná tu itinerario")
        
        session_key = f"sel_index_{folder}"
        if session_key not in st.session_state:
            st.session_state[session_key] = 0

        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))

        for i, plan in enumerate(planes):
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) > 1 else "Días"
            icono = "🚌" if "bus" in plan.lower() else "✈️"

            with cols_p[i]:
                es_activo = st.session_state[session_key] == i
                clase_activa = "selected-plan" if es_activo else ""
                
                st.markdown(f"""
                    <div class="plan-card-click {clase_activa}">
                        <div class="card-top">
                            <div class="day-number">{numero}</div>
                            <div class="transport-icon-big">{icono}</div>
                        </div>
                        <div class="day-text-bottom">{resto}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                st.button(f"Plan_{i}", key=f"btn_{folder}_{i}", on_click=seleccionar_plan, args=(i,))

        # --- MARCA DE VERIFICACIÓN JEO ---
        st.markdown('<div class="jeo-mark">JEO</div>', unsafe_allow_html=True)

        v = df.iloc[st.session_state[session_key]]
        st.divider()

        # SECCIÓN DE WIDGETS
        col_opc, col_monto, col_cash = st.columns(3)

        def clean_val(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        # WIDGET 1: OPCIONES DE PAGO (INTEGRADO)
        with col_opc:
            st.markdown('<div class="widget-3d-inner">', unsafe_allow_html=True)
            st.markdown("<p class='widget-title'>Opciones de Pago</p>", unsafe_allow_html=True)
            opciones_c = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            cuota_sel = st.pills("Cuotas", options=opciones_c, default=opciones_c[0],
