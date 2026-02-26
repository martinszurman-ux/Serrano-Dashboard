import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    def seleccionar_plan(indice):
        st.session_state[f"sel_index_{folder}"] = indice

    # CSS PROFESIONAL: Degradados Mate y Estética Premium
    st.markdown("""
        <style>
        /* Estilos de Tarjetas de Itinerario (Bloqueados) */
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

        /* BOTONES CON DEGRADADO MATE PROFESIONAL */
        .stButton > button {
            background: linear-gradient(145deg, #f0f0f0, #e6e6e6) !important;
            color: #495057 !important;
            border: 1px solid #d1d1d1 !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05) !important;
        }
        .stButton > button:hover {
            background: linear-gradient(145deg, #e6e6e6, #d9d9d9) !important;
            border-color: #bcbcbc !important;
            transform: translateY(-1px);
        }
        /* Botón seleccionado (Mate Oscuro) */
        .selected-btn button {
            background: linear-gradient(145deg, #495057, #343a40) !important;
            color: white !important;
            border: none !important;
            box-shadow: inset 2px 2px 4px rgba(0,0,0,0.3) !important;
        }

        /* PILLS (CUOTAS) CON DEGRADADO MATE */
        div[data-testid="stPills"] button {
            background: linear-gradient(145deg, #ffffff, #f9f9f9) !important;
            border: 1px solid #e0e0e0 !important;
            padding: 10px 20px !important;
            font-weight: 700 !important;
        }
        div[data-testid="stPills"] button[aria-selected="true"] {
            background: linear-gradient(145deg, #d32f2f, #b71c1c) !important;
            color: white !important;
            border: none !important;
        }

        /* WIDGETS 3D */
        .widget-3d-inner {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 15px; padding: 20px; text-align: center;
            border: 1px solid #ddd;
            box-shadow: inset 3px 3px 6px #d1d1d1, inset -3px -3px 6px #ffffff;
            min-height: 190px; display: flex; flex-direction: column; 
            justify-content: center; align-items: center;
        }

        /* TEXTOS DE DISCLAIMER */
        .promo-box-text {
            font-size: 0.7rem; font-weight: 800; color: #d32f2f;
            line-height: 1.2; text-transform: uppercase; margin-top: 10px;
        }
        .benefit-item {
            display: flex; align-items: center; gap: 10px;
            padding: 8px 0; border-bottom: 1px solid #f1f1f1;
            color: #495057; font-size: 0.95rem;
        }
        .benefit-icon { color: #2e7d32; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        st.write("### 📅 Seleccioná tu itinerario")
        
        session_key = f"sel_index_{folder}"
        if session_key not in st.session_state:
            st.session_state[session_key] = 0

        # Render de Itinerarios (Bloqueado)
        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))
        for i, plan in enumerate(planes):
            partes = plan.split(' ', 1)
            numero, resto = partes[0], (partes[1] if len(partes) > 1 else "Días")
            icono = "🚌" if "bus" in plan.lower() else "✈️"
            with cols_p[i]:
                es_activo = st.session_state[session_key] == i
                clase_card = "selected-plan" if es_activo else ""
                st.markdown(f'<div class="plan-card-container {clase_card}"><div><span class="day-number">{numero}</span><span class="transport-icon">{icono}</span></div><div class="day-text">{resto}</div></div>', unsafe_allow_html=True)
                if es_activo: st.markdown('<div class="selected-btn">', unsafe_allow_html=True)
                if st.button("Seleccionar", key=f"btn_{folder}_{i}", use_container_width=True):
                    st.session_state[session_key] = i
                    st.rerun()
                if es_activo: st.markdown('</div>', unsafe_allow_html=True)

        v = df.iloc[st.session_state[session_key]]
        st.divider()

        # --- SECCIÓN DE PAGOS ---
        col_opc, col_monto, col_cash = st.columns(3)

        def clean_val(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col_opc:
            st.markdown("<p style='text-align:center; color:#6c757d; font-size:0.85rem; font-weight:700; text-transform:uppercase;'>Opciones de Pago</p>", unsafe_allow_html=True)
            # Agregamos "1 Pago" a las opciones
            opciones_csv = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            opciones_finales = ["1 Pago"] + opciones_csv
            
            cuota_sel = st.pills("Cuotas", options=opciones_finales, default=opciones_finales[1], label_visibility="collapsed", key=f"pills_{folder}")
            if not cuota_sel: cuota_sel = opciones_finales[1]

        val_contado_base = clean_val(v['Contado'])

        # Lógica de Monto según selección
        with col_monto:
            if cuota_sel == "1 Pago":
                monto_display = "N/A"
                label_monto = "CUOTAS"
            else:
                c_db = cuota_sel.replace(' ', '_')
                monto_display = f"${clean_val(v[c_db]):,.0f}"
                label_monto = f"MONTO {cuota_sel.upper()}"

            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p style='color:#6c757d; font-size:0.8rem; font-weight:700;'>{label_monto}</p>
                    <p style='color:#212529; font-size:2.5rem; font-weight:800; margin:0;'>{monto_display}</p>
                </div>
            """, unsafe_allow_html=True)

        # Widget de Contado con Disclaimer
        with col_cash:
            # Si es 1 Pago, mostramos el total de contado. Si son cuotas, el total con el 10% de la oficina.
            monto_cash = val_contado_base * 0.9
            
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p style='color:#6c757d; font-size:0.8rem; font-weight:700;'>💎 PAGO CONTADO</p>
                    <p style='color:#2e7d32; font-size:2.5rem; font-weight:800; margin:0;'>${monto_cash:,.0f}</p>
                    <div class="promo-box-text">
                        TODOS LOS PLANES EN CUOTAS ABONANDO<br>
                        DEL 1 AL 10 EN LA OFICINA 10% DE DESCUENTO<br>
                        QUE SE APLICA EN LA ULTIMA CUOTA
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        # Tabla Comparativa (Bloqueada)
        df_format = df.copy()
        df_format.columns = [c.replace('_', ' ') for c in df_format.columns]
        for col in df_format.columns.drop('Programa'):
            df_format[col] = df_format[col].apply(clean_val)
        st.table(df_format.set_index('Programa').style.format("$ {:,.0f}"))

        # Beneficios (Bloqueado)
        st.write("#### 🛡️ Beneficios y Servicios Incluidos")
        beneficios = [
            "Liberados para niños y acompañantes.", "Descuentos según formas de pago.",
            "Opciones de pago según necesidad familiar.", "Ayudas complementarias incluidas.",
            "Fiesta de Egresados.", "Importantes descuentos en Camperas.",
            "DJ + Luces y sonido para evento privado."
        ]
        c1, c2 = st.columns(2)
        for i, b in enumerate(beneficios):
            with c1 if i % 2 == 0 else c2:
                st.markdown(f'<div class="benefit-item"><span class="benefit-icon">✓</span>{b}</div>', unsafe_allow_html=True)
    else:
        st.error("CSV no encontrado.")
