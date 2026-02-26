import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    # 1. INICIALIZACIÓN Y BLINDAJE DE SESIÓN
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    session_key = f"sel_index_{folder}"
    
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # 2. ESTILOS CSS (Diseño de Cards, Widgets y Tipografía)
    st.markdown("""
        <style>
        .plan-card-container {
            border-radius: 15px; padding: 20px; background: white;
            border: 1px solid #eee; text-align: center;
            min-height: 140px; display: flex; flex-direction: column;
            justify-content: center; align-items: center; margin-bottom: 10px;
        }
        .selected-plan { border: 2px solid #d32f2f !important; background-color: #fffafb !important; }
        .day-number { color: #d32f2f; font-size: 2.8rem; font-weight: 900; line-height: 1; }
        .transport-icon { font-size: 1.6rem; margin-left: 8px; }
        .day-text { color: #6c757d; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; }

        .widget-3d-inner {
            background: linear-gradient(145deg, #f8f9fa, #ffffff);
            border-radius: 15px; padding: 20px; text-align: center;
            border: 1px solid #ddd;
            box-shadow: inset 2px 2px 5px #edeff0, inset -2px -2px 5px #ffffff;
            min-height: 140px; display: flex; flex-direction: column; 
            justify-content: center; align-items: center;
        }
        .label-widget { color: #6c757d; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 5px; }
        .val-widget { color: #212529; font-size: 1.8rem; font-weight: 800; margin: 0; }
        .val-promo { color: #2e7d32; }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        df.columns = df.columns.str.strip() # Limpia espacios en nombres de columnas
        
        def clean_val(val):
            if pd.isna(val): return 0.0
            clean = str(val).replace('$', '').replace('.', '').replace(',', '').replace('s', '').strip()
            try: return float(clean)
            except: return 0.0

        # --- SECCIÓN 1: SELECCIONÁ TU ITINERARIO ---
        st.write("### 📅 Seleccioná tu itinerario")
        
        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))
        
        for i, plan in enumerate(planes):
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) > 1 else ""
            icono = "🚌" if "bus" in plan.lower() else "✈️"
            
            with cols_p[i]:
                es_activo = st.session_state[session_key] == i
                clase_card = "selected-plan" if es_activo else ""
                
                st.markdown(f'''
                    <div class="plan-card-container {clase_card}">
                        <div><span class="day-number">{numero}</span><span class="transport-icon">{icono}</span></div>
                        <div class="day-text">{resto}</div>
                    </div>
                ''', unsafe_allow_html=True)
                
                if st.button("Seleccionar", key=f"btn_{folder}_{i}", use_container_width=True):
                    st.session_state[session_key] = i
                    st.rerun()

        # Datos del programa seleccionado
        idx = st.session_state[session_key]
        if idx >= len(df): idx = 0
        v = df.iloc[idx]

        # --- SECCIÓN 2: OPCIONES DE PAGO ---
        st.write("") 
        # Excluimos columnas que no son cuotas para el selector
        excluir = ['Programa', 'Contado', 'Valor del Viaje', 'Costo Total', 'Valor del viaje']
        opciones_cuotas = [c.replace('_', ' ') for c in df.columns if c not in excluir]
        opciones_finales = ["1 Pago"] + opciones_cuotas

        c_text, c_pills = st.columns([1, 4])
        with c_text:
            st.markdown("<p style='font-weight:700; color:#495057; margin-top:10px;'>Opciones de Pago:</p>", unsafe_allow_html=True)
        with c_pills:
            cuota_sel = st.pills("Selecciona cuotas", options=opciones_finales, default=opciones_finales[1], label_visibility="collapsed", key=f"pills_{folder}")
            if not cuota_sel: cuota_sel = opciones_finales[1]

        # --- SECCIÓN 3: LÍNEA GRIS Y WIDGETS ---
        st.markdown("<hr style='border-top: 1px solid #bbb; margin: 30px 0;'>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        # Detección dinámica de la columna de valor total
        col_total = next((c for c in df.columns if 'valor' in c.lower() or 'costo' in c.lower()), None)
        val_total_viaje = clean_val(v[col_total]) if col_total else 0.0
        descuento_termino = val_total_viaje * 0.10

        # Widget 1: Valor Final
        with col1:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class="label-widget">💰 Valor Final del Viaje</p>
                    <p class="val-widget">${val_total_viaje:,.0f}</p>
                </div>
            """, unsafe_allow_html=True)

        # Widget 2: Monto Cuota
        with col2:
            if cuota_sel == "1 Pago":
                m_display = f"${clean_val(v['Contado']):,.0f}"
                label_cuota = "Monto Pago Único"
            else:
                c_db = cuota_sel.replace(' ', '_')
                m_display = f"${clean_val(v[c_db]):,.0f}"
                label_cuota = f"Monto de la {cuota_sel}"
            
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class="label-widget">💳 {label_cuota}</p>
                    <p class="val-widget">{m_display}</p>
                </div>
            """, unsafe_allow_html=True)

        # Widget 3: Descuento
        with col3:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class="label-widget">🎁 Descuento Pago Término</p>
                    <p class="val-widget val-promo">-${descuento_termino:,.0f}</p>
                </div>
            """, unsafe_allow_html=True)

        # Texto aclaratorio del descuento
        st.markdown("""
            <p style='font-size: 0.95rem; color: #333333; text-align: center; margin-top: 20px; font-weight: 500;'>
                El descuento por pago en término se aplica sobre la última cuota si se abonan todas del 1 al 10 de cada mes.
            </p>
        """, unsafe_allow_html=True)

        # --- SECCIÓN 4: TABLA Y BENEFICIOS ---
        st.divider()
        
        with st.expander("Ver tabla comparativa de todas las tarifas"):
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
