import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # CSS Refinado: Disposición número-ícono y fix de selección
    st.markdown("""
        <style>
        .plan-card-click {
            border-radius: 15px;
            padding: 15px;
            background: white;
            border: 2px solid #eee;
            transition: all 0.3s ease;
            min-height: 140px;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .selected-plan { 
            border: 3px solid #d32f2f !important; 
            background-color: #fff5f5 !important;
            box-shadow: 0 4px 10px rgba(211, 47, 47, 0.1);
        }
        
        /* Contenedor superior: Número e ícono alineados */
        .card-top {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            margin-bottom: 5px;
        }
        
        .day-number { 
            color: #d32f2f; 
            font-size: 3.2rem; 
            font-weight: 900; 
            line-height: 1; 
        }
        .transport-icon-big { 
            font-size: 2.5rem; 
        }
        
        .day-text-bottom { 
            color: #495057; 
            font-size: 0.85rem; 
            font-weight: 700; 
            text-transform: uppercase;
            text-align: center;
        }

        /* Botón invisible que cubre toda la tarjeta */
        .stButton button {
            background-color: transparent !important;
            border: none !important;
            color: transparent !important;
            height: 140px !important;
            width: 100% !important;
            position: absolute;
            top: 0; left: 0;
            z-index: 10;
            cursor: pointer;
        }

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
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        
        # --- LÓGICA DE SELECCIÓN CORREGIDA ---
        st.write("### 📅 Seleccioná tu itinerario")
        
        # Clave única de sesión por destino para evitar conflictos
        session_key = f"sel_index_{folder}"
        if session_key not in st.session_state:
            st.session_state[session_key] = 0

        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))

        for i, plan in enumerate(planes):
            # Lógica de extracción de datos del PDF
            # Basado en duración y transporte
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) > 1 else "Días"
            icono = "🚌" if "bus" in plan.lower() else "✈️"

            with cols_p[i]:
                # Comprobar si este índice es el seleccionado
                es_activo = st.session_state[session_key] == i
                clase_activa = "selected-plan" if es_activo else ""
                
                # Diseño visual solicitado: Número e ícono arriba, texto abajo
                st.markdown(f"""
                    <div class="plan-card-click {clase_activa}">
                        <div class="card-top">
                            <div class="day-number">{numero}</div>
                            <div class="transport-icon-big">{icono}</div>
                        </div>
                        <div class="day-text-bottom">{resto}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # El botón invisible ahora actualiza correctamente el estado
                if st.button(f"Select_{folder}_{i}", key=f"btn_nav_{folder}_{i}"):
                    st.session_state[session_key] = i
                    st.rerun()

        # Obtener datos del plan según la selección actual
        v = df.iloc[st.session_state[session_key]]
        st.divider()

        # --- WIDGETS INFERIORES ---
        col_opc, col_monto, col_cash = st.columns(3)

        def clean_val(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col_opc:
            st.markdown('<div class="widget-3d-inner">', unsafe_allow_html=True)
            st.markdown("<p class='widget-title'>Opciones de Pago</p>", unsafe_allow_html=True)
            cols_c = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            # Usar key dinámica para las pills también
            cuota_sel = st.pills("Cuotas", options=cols_c, default=cols_c[0], label_visibility="collapsed", key=f"pills_val_{folder}")
            st.markdown('</div>', unsafe_allow_html=True)

        c_db = cuota_sel.replace(' ', '_')
        val_c = clean_val(v[c_db])
        val_cont = clean_val(v['Contado'])

        with col_monto:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class='widget-title'>Monto {cuota_sel}</p>
                    <p class='widget-value'>${val_c:,.0f}</p>
                    <p class='promo-subtitle'>Cuota fija mensual</p>
                </div>
            """, unsafe_allow_html=True)

        with col_cash:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class='widget-title'>💎 Efectivo (Oficina)</p>
                    <p class='widget-value' style='color: #495057;'>${val_cont * 0.9:,.0f}</p>
                    <p class='promo-subtitle'>Incluye beneficio 10% OFF</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📊
