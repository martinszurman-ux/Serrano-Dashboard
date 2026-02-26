import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    # Definir la carpeta según el destino
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # 1. Header Dinámico
    header_img_path = None
    for ext in [".jpg", ".png", ".jpeg"]:
        temp_path = f"data/{folder}/tarifas_y_formas_header{ext}"
        if os.path.exists(temp_path):
            header_img_path = temp_path
            break

    if header_img_path:
        st.image(header_img_path, use_container_width=True)
    else:
        st.markdown(f"""
            <div class="header-container">
                <div class="header-text-overlay">TARIFAS {destino.upper()}</div>
            </div>
        """, unsafe_allow_html=True)

    # 2. Carga de Datos
    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        
        st.write("### 🎯 Seleccioná tu Plan de Viaje")
        
        # Gestión de estado para el selector de iconos
        if f'plan_{folder}' not in st.session_state:
            st.session_state[f'plan_{folder}'] = df['Programa'].iloc[0]

        # Selector de Planes con Iconos
        planes = df['Programa'].unique()[:4]
        iconos = ["🚌", "✈️", "🌴", "🏛️"]
        
        cols_iconos = st.columns(len(planes))
        for i, p_name in enumerate(planes):
            with cols_iconos[i]:
                # Estilo visual si está seleccionado
                es_sel = st.session_state[f'plan_{folder}'] == p_name
                clase_css = "plan-selected" if es_sel else ""
                
                st.markdown(f"""
                    <div class="plan-card-box {clase_css}" style="border: {'2px solid #1E3A8A' if es_sel else '1px solid #eee'}; padding:15px; border-radius:15px; text-align:center; background:{'#f0f4ff' if es_sel else 'white'}">
                        <div style="font-size: 2.5rem;">{iconos[i % len(iconos)]}</div>
                        <div style="font-weight: bold; font-size: 0.9rem; margin-top:10px;">{p_name}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button("Seleccionar", key=f"btn_{folder}_{i}"):
                    st.session_state[f'plan_{folder}'] = p_name
                    st.rerun()

        # Obtener datos del plan seleccionado
        v = df[df['Programa'] == st.session_state[f'plan_{folder}']].iloc[0]

        st.divider()
        
        # 3. Widgets 3D con Degradado
        col1, col2, col3 = st.columns(3)

        def to_num(val):
            try:
                return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())
            except:
                return 0.0

        with col1:
            st.markdown('<div class="widget-3d-grad">', unsafe_allow_html=True)
            st.markdown("<p class='widget-title'>OPCIONES DE PAGO</p>", unsafe_allow_html=True)
            opciones_cols = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            cuota_sel = st.pills("Cuotas:", options=opciones_cols, default=opciones_cols[0], label_visibility="collapsed", key=f"pills_{folder}")
            st.markdown('</div>', unsafe_allow_html=True)

        # Cálculos de valores
        col_db = cuota_sel.replace(' ', '_')
        val_cuota = to_num(v[col_db])
        val_contado = to_num(v['Contado'])

        with col2:
            st.markdown(f"""
                <div class="widget-3d-grad">
                    <p class='widget-title'>MONTO {cuota_sel.upper()}</p>
                    <p class='widget-value'>${val_cuota:,.0f}</p>
                    <p class='promo-subtitle'>Valor de cuota fija</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="widget-3d-grad">
                    <p class='widget-title'>💎 PAGO EFECTIVO (10% OFF)</p>
                    <p class='widget-value' style='color: #2e7d32;'>${val_contado * 0.9:,.0f}</p>
                    <p class='promo-subtitle'>Precio especial bonificado</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver tabla comparativa completa"):
            st.table(df.set_index('Programa'))
            
    else:
        st.error(f"No se encontró el archivo de tarifas en: {path_tarifas}")
