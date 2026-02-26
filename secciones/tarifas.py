import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    def seleccionar_plan(indice):
        st.session_state[f"sel_index_{folder}"] = indice

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
        .benefit-item {
            display: flex; align-items: center; gap: 10px;
            padding: 8px 0; border-bottom: 1px solid #f1f1f1;
            color: #495057; font-size: 0.95rem;
        }
        .benefit-icon { color: #2e7d32; font-weight: bold; }
        .promo-box-text {
            font-size: 0.75rem; font-weight: 800; color: #d32f2f;
            line-height: 1.3; text-transform: uppercase; margin-top: 10px;
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
                clase_card = "selected-plan" if es_activo else ""
                st.markdown(f'<div class="plan-card-container {clase_card}"><div><span class="day-number">{numero}</span><span class="transport-icon">{icono}</span></div><div class="day-text">{resto}</div></div>', unsafe_allow_html=True)
                if st.button("Seleccionar", key=f"btn_plan_{folder}_{i}", use_container_width=True):
                    st.session_state[session_key] = i
                    st.rerun()

        v = df.iloc[st.session_state[session_key]]
        st.divider()
        
        # Widgets de Montos
        col_opc, col_monto, col_cash = st.columns(3)

        def clean_val(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col_opc:
            st.markdown("<p style='text-align:center; color:#6c757d; font-size:0.85rem; font-weight:700; text-transform:uppercase;'>Opciones de Pago</p>", unsafe_allow_html=True)
            opciones_c = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            cuota_sel = st.pills("Cuotas", options=opciones_c, default=opciones_c[0], label_visibility="collapsed", key=f"pills_{folder}")
            if not cuota_sel: cuota_sel = opciones_c[0]

        c_db = cuota_sel.replace(' ', '_')
        val_c = clean_val(v[c_db])
        val_cont = clean_val(v['Contado'])

        with col_monto:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p style='color:#6c757d; font-size:0.8rem; font-weight:700;'>MONTO {cuota_sel.upper()}</p>
                    <p style='color:#212529; font-size:2.2rem; font-weight:800; margin:0;'>${val_c:,.0f}</p>
                    <div class="promo-box-text">Abonando del 1 al 10 en oficina:<br>10% OFF en la última cuota</div>
                </div>
            """, unsafe_allow_html=True)

        with col_cash:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p style='color:#6c757d; font-size:0.8rem; font-weight:700;'>💎 PAGO CONTADO</p>
                    <p style='color:#2e7d32; font-size:2.2rem; font-weight:800; margin:0;'>${val_cont * 0.9:,.0f}</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.write("### 📊 Tabla Comparativa")
        df_format = df.copy()
        df_format.columns = [c.replace('_', ' ') for c in df_format.columns]
        for col in df_format.columns.drop('Programa'):
            df_format[col] = df_format[col].apply(clean_val)
        st.table(df_format.set_index('Programa').style.format("$ {:,.0f}"))

        # Beneficios
        st.write("#### 🛡️ Beneficios y Servicios Incluidos")
        beneficios = [
            "Liberados para niños y acompañantes.",
            "Descuentos según formas de pago.",
            "Opciones de pago personalizadas.",
            "Ayudas complementarias incluidas.",
            "Fiesta de Egresados.",
            "Descuentos en Camperas.",
            "DJ + Luces para recaudar fondos."
        ]
        c1, c2 = st.columns(2)
        for i, b in enumerate(beneficios):
            with c1 if i % 2 == 0 else c2:
                st.markdown(f'<div class="benefit-item"><span class="benefit-icon">✓</span>{b}</div>', unsafe_allow_html=True)
    else:
        st.error("CSV no encontrado.")
