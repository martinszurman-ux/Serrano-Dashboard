import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # Lógica de selección
    session_key = f"sel_index_{folder}"
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # CSS: Limpieza y diseño de botones
    st.markdown("""
        <style>
        .plan-card-container {
            border-radius: 15px; padding: 15px; background: white;
            border: 2px solid #eee; transition: all 0.3s ease;
            min-height: 180px; display: flex; flex-direction: column; 
            justify-content: space-between; align-items: center;
        }
        .selected-plan { 
            border: 3px solid #d32f2f !important; 
            background-color: #fff5f5 !important;
        }
        .card-top { display: flex; justify-content: center; align-items: center; gap: 10px; }
        .day-number { color: #d32f2f; font-size: 2.8rem; font-weight: 900; line-height: 1; }
        .transport-icon-big { font-size: 2rem; }
        .day-text-bottom { color: #495057; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; margin-bottom: 10px;}

        /* Título de Opciones Centrado */
        .pago-header {
            text-align: center; width: 100%; margin-top: 20px;
            color: #6c757d; font-size: 0.9rem; font-weight: 800; text-transform: uppercase;
        }

        /* Botones de cuotas XL */
        div[data-testid="stPills"] { display: flex; justify-content: center; width: 100%; }
        div[data-testid="stPills"] button {
            padding: 12px 25px !important; font-size: 1rem !important;
            font-weight: 800 !important; border-radius: 10px !important;
        }
        
        .widget-3d-inner {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 15px; padding: 20px; text-align: center;
            border: 1px solid #ddd;
            box-shadow: inset 3px 3px 6px #d1d1d1, inset -3px -3px 6px #ffffff;
            min-height: 140px; display: flex; flex-direction: column; 
            justify-content: center; align-items: center;
        }

        /* Tabla Contable */
        th { text-align: center !important; font-weight: bold !important; background-color: #f2f2f2 !important; }
        td { text-align: center !important; }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        st.write("### 📅 Seleccioná tu itinerario")
        
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
                
                # Render visual de la tarjeta
                st.markdown(f"""
                    <div class="plan-card-container {clase_activa}">
                        <div class="card-top">
                            <div class="day-number">{numero}</div>
                            <div class="transport-icon-big">{icono}</div>
                        </div>
                        <div class="day-text-bottom">{resto}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botón de selección explícito adentro de la columna
                if st.button("Seleccionar", key=f"sel_{folder}_{i}", use_container_width=True, type="primary" if es_activo else "secondary"):
                    st.session_state[session_key] = i
                    st.rerun()

        v = df.iloc[st.session_state[session_key]]
        st.divider()

        # --- SECCIÓN DE PAGOS Y MONTOS ---
        col_opc, col_monto, col_cash = st.columns(3)

        def clean_val(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col_opc:
            st.markdown("<p class='pago-header'>Opciones de Pago</p>", unsafe_allow_html=True)
            opciones_c = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            cuota_sel = st.pills("Cuotas", options=opciones_c, default=opciones_c[0], label_visibility="collapsed", key=f"p_{folder}")
            if not cuota_sel: cuota_sel = opciones_c[0]

        c_db = cuota_sel.replace(' ', '_')
        val_c = clean_val(v[c_db])
        val_cont = clean_val(v['Contado'])

        with col_monto:
            st.markdown(f"""<div class="widget-3d-inner"><p style='color:#6c757d; font-size:0.8rem; font-weight:700;'>MONTO {cuota_sel.upper()}</p><p style='color:#212529; font-size:2.2rem; font-weight:800; margin:0;'>${val_c:,.0f}</p></div>""", unsafe_allow_html=True)

        with col_cash:
            st.markdown(f"""<div class="widget-3d-inner"><p style='color:#6c757d; font-size:0.8rem; font-weight:700;'>💎 EFECTIVO (10% OFF)</p><p style='color:#495057; font-size:2.2rem; font-weight:800; margin:0;'>${val_cont * 0.9:,.0f}</p></div>""", unsafe_allow_html=True)

        st.divider()
        st.write("### 📊 Tabla Comparativa de Planes")
        df_format = df.copy()
        df_format.columns = [c.replace('_', ' ') for c in df_format.columns]
        for col in df_format.columns.drop('Programa'):
            df_format[col] = df_format[col].apply(clean_val)

        st.table(df_format.set_index('Programa').style.format("$ {:,.0f}"))
    else:
        st.error("CSV no encontrado.")
