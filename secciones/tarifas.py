import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    # 1. INICIALIZACIÓN
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    session_key = f"sel_index_{folder}"
    
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # 2. ESTILOS CSS (Diseño Hero para el Pago)
    st.markdown("""
        <style>
        /* Cards de Itinerario */
        .plan-card-container {
            border-radius: 15px; padding: 20px; background: white;
            border: 1px solid #eee; text-align: center;
            min-height: 140px; display: flex; flex-direction: column;
            justify-content: center; align-items: center; margin-bottom: 10px;
            transition: transform 0.3s ease;
        }
        .selected-plan { 
            border: 2px solid #d32f2f !important; 
            background-color: #fffafb !important;
            transform: scale(1.02);
        }
        .day-number { color: #d32f2f; font-size: 2.8rem; font-weight: 900; line-height: 1; }
        .transport-icon { font-size: 1.6rem; margin-left: 8px; }
        .day-text { color: #6c757d; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; }

        /* MEGA WIDGET HERO */
        .hero-payment-card {
            background: linear-gradient(145deg, #ffffff, #f0f2f6);
            border-radius: 24px;
            padding: 40px;
            text-align: center;
            border: 1px solid #e0e4e8;
            box-shadow: 20px 20px 60px #d9dbe0, -20px -20px 60px #ffffff;
            max-width: 500px;
            margin: 20px auto;
        }
        .hero-label { 
            color: #6c757d; 
            font-size: 0.9rem; 
            font-weight: 700; 
            text-transform: uppercase; 
            letter-spacing: 1.5px;
            margin-bottom: 10px;
        }
        .hero-value { 
            color: #1a1c1e; 
            font-size: 4rem; 
            font-weight: 900; 
            margin: 0;
            line-height: 1;
            background: -webkit-linear-gradient(#1a1c1e, #4a4d52);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-subtitle {
            color: #d32f2f;
            font-size: 1.2rem;
            font-weight: 600;
            margin-top: 10px;
        }

        /* Tabla Centrada */
        .styled-table th {
            background-color: #333333 !important;
            color: white !important;
            font-weight: bold !important;
            text-align: center !important;
        }
        .styled-table td { text-align: center !important; }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        df.columns = df.columns.str.strip()
        
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
        excluir_botones = ['Programa', 'Contado', 'Valor del Viaje', 'Costo Total', 'Valor del viaje']
        opciones_cuotas = [c.replace('_', ' ') for c in df.columns if c not in excluir_botones]
        opciones_finales = ["1 Pago"] + opciones_cuotas

        # Selector de Cuotas (Pills centrado)
        st.markdown("<p style='text-align:center; font-weight:700; color:#495057; margin-bottom:15px;'>Elegí tu plan de pago:</p>", unsafe_allow_html=True)
        _, c_pills, _ = st.columns([1, 4, 1])
        with c_pills:
            cuota_sel = st.pills("Selecciona cuotas", options=opciones_finales, default=opciones_finales[1], label_visibility="collapsed", key=f"pills_{folder}")
            if not cuota_sel: cuota_sel = opciones_finales[1]

        # --- SECCIÓN 3: EL GRAN WIDGET HERO ---
        st.markdown("<hr style='border-top: 1px solid #eee; margin: 30px 0;'>", unsafe_allow_html=True)
        
        # Lógica de Monto
        if cuota_sel == "1 Pago":
            m_display = f"${clean_val(v['Contado']):,.0f}"
            label_cuota = "Pago Único"
        else:
            c_db = cuota_sel.replace(' ', '_')
            m_display = f"${clean_val(v[c_db]):,.0f}"
            label_cuota = f"Por Cuota ({cuota_sel})"

        # Render del Hero Widget Centrado
        st.markdown(f"""
            <div class="hero-payment-card">
                <p class="hero-label">Monto a abonar</p>
                <p class="hero-value">{m_display}</p>
                <p class="hero-subtitle">💳 Plan {label_cuota}</p>
            </div>
        """, unsafe_allow_html=True)

        # Texto del regalo/descuento debajo del gran widget
        st.markdown("""
            <div style='max-width: 700px; margin: 30px auto; padding: 20px; background-color: #fdf2f2; border-radius: 12px; border: 1px dashed #d32f2f;'>
                <p style='font-size: 1rem; color: #333333; text-align: center; margin: 0; font-weight: 500;'>
                    🎁 <b>¡Beneficio Exclusivo!</b> Pagando todas las cuotas del 1 al 10 de cada mes en efectivo en Serrano, 
                    obtenés un <b>10% de descuento</b> sobre el total del viaje (aplicado en la última cuota).
                </p>
            </div>
        """, unsafe_allow_html=True)

        # --- SECCIÓN 4: TABLA Y BENEFICIOS ---
        st.divider()
        with st.expander("Ver tabla comparativa de todas las tarifas"):
            df_format = df.copy()
            cols_a_borrar = [c for c in df_format.columns if 'valor del viaje' in c.lower() or 'costo total' in c.lower()]
            df_format = df_format.drop(columns=cols_a_borrar)
            if 'Contado' in df_format.columns:
                df_format = df_format.rename(columns={'Contado': 'Valor 1 Pago'})
            df_format.columns = [c.replace('_', ' ') for c in df_format.columns]
            for col in df_format.columns.drop('Programa'): 
                df_format[col] = df_format[col].apply(clean_val)
            
            st.markdown('<div class="styled-table">', unsafe_allow_html=True)
            st.table(df_format.set_index('Programa').style.format("$ {:,.0f}")
                     .set_table_styles([
                         {'selector': 'th', 'props': [('background-color', '#333333'), ('color', 'white'), ('font-weight', 'bold'), ('text-align', 'center !important')]},
                         {'selector': 'td', 'props': [('text-align', 'center !important')]}
                     ]))
            st.markdown('</div>', unsafe_allow_html=True)

        st.write("#### 🛡️ Beneficios y Servicios Incluidos")
        beneficios = [
            "Liberados para niños y acompañantes.", "Descuentos según formas de pago.", 
            "Opciones de pago personalizadas.", "Ayudas complementarias incluidas.", 
            "Fiesta de Egresados.", "Importantes descuentos en Camperas.", 
            "DJ + Luces y sonido para evento privado."
        ]
        c1, c2 = st.columns(2)
        for i, b in enumerate(beneficios):
            with c1 if i % 2 == 0 else c2:
                st.markdown(f'<div style="display:flex; align-items:center; gap:10px; padding:8px 0; border-bottom:1px solid #f1f1f1; color:#495057;"><span style="color:#2e7d32; font-weight:bold;">✓</span>{b}</div>', unsafe_allow_html=True)
    else:
        st.error("Archivo de datos no encontrado.")
