import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    # 1. ESCUDO DE INICIALIZACIÓN (Previene el KeyError)
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    session_key = f"sel_index_{folder}"
    
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # 2. ESTILOS (Degradados Mate y Diseño Final)
    st.markdown("""
        <style>
        .plan-card-container {
            border-radius: 15px; padding: 20px; background: white;
            border: 1px solid #eee; text-align: center;
            min-height: 160px; display: flex; flex-direction: column;
            justify-content: center; align-items: center; margin-bottom: 10px;
        }
        .selected-plan { border: 2px solid #d32f2f !important; background-color: #fffafb !important; }
        .day-number { color: #d32f2f; font-size: 3rem; font-weight: 900; line-height: 1; }
        .transport-icon { font-size: 1.8rem; margin-left: 8px; }
        .day-text { color: #6c757d; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; }

        /* BOTONES MATE PROFESIONAL */
        .stButton > button {
            background: linear-gradient(145deg, #f0f0f0, #e6e6e6) !important;
            color: #495057 !important;
            border: 1px solid #d1d1d1 !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05) !important;
        }
        .selected-btn button {
            background: linear-gradient(145deg, #495057, #343a40) !important;
            color: white !important;
            border: none !important;
        }

        /* WIDGETS DE PAGO */
        .widget-3d-inner {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 15px; padding: 20px; text-align: center;
            border: 1px solid #ddd;
            box-shadow: inset 3px 3px 6px #d1d1d1, inset -3px -3px 6px #ffffff;
            min-height: 200px; display: flex; flex-direction: column; 
            justify-content: center; align-items: center;
        }
        .promo-box-text {
            font-size: 0.75rem; font-weight: 600; color: #d32f2f;
            line-height: 1.3; margin-top: 10px;
            padding: 0 5px;
        }
        /* Estilo para tabla contable */
        th { text-align: center !important; font-weight: bold !important; background-color: #f2f2f2 !important; }
        td { text-align: center !important; }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        st.write("### 📅 Seleccioná tu itinerario")
        
        # Grid de itinerarios
        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))
        for i, plan in enumerate(planes):
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) > 1 else "Días"
            icono = "🚌" if "bus" in plan.lower() else "✈️"
            with cols_p[i]:
                es_activo = st.session_state[session_key] == i
                clase_card = "selected-plan" if es_activo else ""
                st.markdown(f'<div class="plan-card-container {clase_card}"><div><span class="day-number">{numero}</span><span class="transport-icon">{icono}</span></div><div class="day-text">{resto}</div></div>', unsafe_allow_html=True)
                
                # Botón de selección con estilo condicional
                if es_activo: st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
                if st.button("Seleccionar", key=f"btn_{folder}_{i}", use_container_width=True):
                    st.session_state[session_key] = i
                    st.rerun()
                if es_activo: st.markdown('</div>', unsafe_allow_html=True)

        # 3. LÓGICA DE CÁLCULO
        idx = st.session_state[session_key]
        if idx >= len(df): idx = 0 
        v = df.iloc[idx]
        
        st.divider()

        # --- WIDGETS DE PAGO ---
        col_opc, col_monto, col_cash = st.columns(3)

        def clean_val(val):
            try:
                return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())
            except:
                return 0.0

        with col_opc:
            st.markdown("<p style='text-align:center; color:#6c757d; font-size:0.85rem; font-weight:700; text-transform:uppercase;'>Opciones de Pago</p>", unsafe_allow_html=True)
            opciones_csv = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            opciones_finales = ["1 Pago"] + opciones_csv
            
            cuota_sel = st.pills("Cuotas", options=opciones_finales, default=opciones_finales[1], label_visibility="collapsed", key=f"pills_{folder}")
            if not cuota_sel: cuota_sel = opciones_finales[1]

        # Cálculos
        val_contado_base = clean_val(v['Contado'])

        with col_monto:
            label = "MONTO CUOTAS"
            
            if cuota_sel == "1 Pago":
                m_display = "No aplica cuotas"
                font_size = "1.5rem" 
            else:
                c_db = cuota_sel.replace(' ', '_')
                m_display = f"${clean_val(v[c_db]):,.0f}"
                font_size = "2.5rem"

            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p style='color:#6c757d; font-size:0.8rem; font-weight:700;'>{label}</p>
                    <p style='color:#212529; font-size:{font_size}; font-weight:800; margin:0;'>{m_display}</p>
                </div>
            """, unsafe_allow_html=True)

        with col_cash:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p style='color:#6c757d; font-size:0.8rem; font-weight:700;'>💎 PAGO CONTADO</p>
                    <p style='color:#2e7d32; font-size:2.5rem; font-weight:800; margin:0;'>${val_contado_base * 0.9:,.0f}</p>
                    <div class="promo-box-text">
                        Pagando todas las cuotas del 1 al 10 de cada mes, en efectivo en nuestras oficinas de Serrano, 
                        obtenés un 10% de descuento sobre el total del viaje, aplicado en la última cuota.
                    </div>
                </div>
            """, unsafe_allow_html=True)

        # 4. TABLA Y BENEFICIOS
        st.divider()
        df_format = df.copy()
        df_format.columns = [c.replace('_', ' ') for c in df_format.columns]
        for col in df_format.columns.drop('Programa'): 
            df_format[col] = df_format[col].apply(clean_val)
        
        st.table(df_format.set_index('Programa').style.format("$ {:,.0f}"))

        st.write("#### 🛡️ Beneficios y Servicios Incluidos")
        beneficios = [
            "Liberados para niños y acompañantes.", 
            "Descuentos según formas de pago.", 
            "Opciones de pago personalizadas.", 
            "Ayudas complementarias incluidas.", 
            "Fiesta de Egresados.", 
            "Importantes descuentos en Camperas.", 
            "DJ + Luces y sonido para evento privado."
        ]
        c1, c2 = st.columns(2)
        for i, b in enumerate(beneficios):
            with c1 if i % 2 == 0 else c2:
                st.markdown(f'<div style="display:flex; align-items:center; gap:10px; padding:8px 0; border-bottom:1px solid #f1f1f1; color:#495057;"><span style="color:#2e7d32; font-weight:bold;">✓</span>{b}</div>', unsafe_allow_html=True)
    else:
        st.error("Archivo de datos no encontrado.")
