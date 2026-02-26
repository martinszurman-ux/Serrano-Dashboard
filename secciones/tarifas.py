import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    # 1. INICIALIZACIÓN Y BLINDAJE
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    session_key = f"sel_index_{folder}"
    
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # 2. ESTILOS CSS
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

        .widget-3d-inner {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 15px; padding: 20px; text-align: center;
            border: 1px solid #ddd;
            box-shadow: inset 3px 3px 6px #d1d1d1, inset -3px -3px 6px #ffffff;
            min-height: 160px; display: flex; flex-direction: column; 
            justify-content: center; align-items: center;
        }
        .label-widget { color: #6c757d; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 5px; }
        .val-widget { color: #212529; font-size: 2.2rem; font-weight: 800; margin: 0; }
        .val-promo { color: #2e7d32; }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        # Cargamos el DF y limpiamos espacios en blanco en los nombres de columnas
        df = pd.read_csv(path_tarifas)
        df.columns = df.columns.str.strip()
        
        def clean_val(val):
            if pd.isna(val): return 0.0
            # Limpieza profunda de caracteres extraños
            clean = str(val).replace('$', '').replace('.', '').replace(',', '').replace('s', '').strip()
            try: return float(clean)
            except: return 0.0

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
                st.markdown(f'<div class="plan-card-container {clase_card}"><div><span class="day-number">{numero}</span><span class="transport-icon">{icono}</span></div><div class="day-text">{resto}</div></div>', unsafe_allow_html=True)
                if st.button("Seleccionar", key=f"btn_{folder}_{i}", use_container_width=True):
                    st.session_state[session_key] = i
                    st.rerun()

        # Datos del programa seleccionado
        idx = st.session_state[session_key]
        if idx >= len(df): idx = 0
        v = df.iloc[idx]
        
        # --- BLOQUE DE WIDGETS ---
        col1, col2, col3 = st.columns(3)
        
        # Calculamos valores base (Usando el nombre exacto del CSV)
        # Cambié 'Valor del Viaje' por 'Valor del Viaje' o 'Costo Total' según tu último CSV
        col_total = 'Valor del Viaje' if 'Valor del Viaje' in df.columns else 'Costo Total'
        val_total_viaje = clean_val(v[col_total])
        descuento_termino = val_total_viaje * 0.10
        
        # Inicializamos cuota_sel para evitar errores de referencia
        cuota_sel = "3_Cuotas" 

        # Widget 1: Valor Final
        with col1:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class="label-widget">💰 Valor Final del Viaje</p>
                    <p class="val-widget">${val_total_viaje:,.0f}</p>
                </div>
            """, unsafe_allow_html=True)

        # Widget 2: Monto Cuota (se actualizará con el selector de abajo)
        # Para que el widget 2 responda al selector que está abajo, usamos un placeholder o simplemente movemos el selector.
        # Por orden de ejecución de Python, el selector debe ir ANTES de los widgets si queremos que estos cambien.
        
        # Widget 3: Descuento
        with col3:
            st.markdown(f"""
                <div class="widget-3d-inner">
                    <p class="label-widget">🎁 Descuento Pago Término</p>
                    <p class="val-widget val-promo">-${descuento_termino:,.0f}</p>
                </div>
            """, unsafe_allow_html=True)

        # --- OPCIONES DE PAGO (Debajo de los widgets pero define el Widget 2) ---
        st.markdown("<br>", unsafe_allow_html=True)
        excluir = ['Programa', 'Contado', 'Valor del Viaje', 'Costo Total']
        opciones_cuotas = [c.replace('_', ' ') for c in df.columns if c not in excluir]
        opciones_finales = ["1 Pago"] + opciones_cuotas

        st.markdown("<p style='font-weight:700; color:#495057; margin-bottom:5px;'>Opciones de Pago:</p>", unsafe_allow_html=True)
        cuota_sel = st.pills("Selecciona cuotas", options=opciones_finales, default=opciones_finales[1], label_visibility="collapsed", key=f"pills_{folder}")
        
        # Ahora actualizamos el Widget 2 (usamos st.metric o recreamos el valor en el col2)
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

        st.divider()
        # ... resto del código (beneficios)
