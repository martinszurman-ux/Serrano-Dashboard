elif opcion == "Tarifas y Formas de Pago":
    # --- ESTILO CSS PARA IMAGEN ESFUMADA Y DISEÑO ---
    st.markdown("""
        <style>
        .header-container {
            position: relative;
            height: 250px;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            border-radius: 15px;
            margin-bottom: 30px;
        }
        .header-image {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url('https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png');
            background-size: cover;
            background-position: center;
            filter: blur(4px) brightness(0.6); /* EFECTO ESFUMADO */
            z-index: -1;
        }
        .header-text {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        }
        [data-testid="stMetricValue"] { font-size: 1.8rem !important; }
        </style>
        
        <div class="header-container">
            <div class="header-image"></div>
            <div class="header-text">TARIFARIO EXCLUSIVO 2027</div>
        </div>
    """, unsafe_allow_html=True)

    if os.path.exists(path):
        df_tarifas = pd.read_csv(path)
        
        # 1. Selector de Programa (Arriba de todo)
        programa_elegido = st.selectbox("🎯 Seleccioná tu Plan de Viaje:", df_tarifas['Programa'])
        datos_plan = df_tarifas[df_tarifas['Programa'] == programa_elegido].iloc[0]
        
        st.divider()

        # 2. SECCIÓN NIVELADA (Todo a la misma altura)
        # Creamos 3 columnas equilibradas
        col_selector, col_valor, col_promo = st.columns([1.2, 1, 1.5])
        
        with col_selector:
            st.markdown("**💳 Elegí tus cuotas:**")
            # Cambiamos slider por Pills (botones) para que se vean todas las opciones
            cuota_sel = st.segmented_control(
                "Opciones disponibles:",
                options=["Contado", "3 Cuotas", "6 Cuotas", "12 Cuotas", "18 Cuotas"],
                default="Contado",
                label_visibility="collapsed"
            )

        # Lógica de precios
        def clean_val(val):
            if isinstance(val, str):
                return float(val.replace('$', '').replace('.', '').replace(',', '').strip())
            return val

        col_map = {"Contado": "Contado", "3 Cuotas": "3_Cuotas", "6 Cuotas": "6_Cuotas", "12 Cuotas": "12_Cuotas", "18 Cuotas": "18_Cuotas"}
        valor_cuota = clean_val(datos_plan[col_map[cuota_sel]])
        valor_contado = clean_val(datos_plan['Contado'])
        valor_con_descuento = valor_contado * 0.90

        with col_valor:
            st.metric(label=f"Monto {cuota_sel}", value=f"${valor_cuota:,.0f}")

        with col_promo:
            st.markdown(f"""
            <div style="background-color: #e8f5e9; padding: 10px; border-radius: 10px; border-left: 5px solid #2e7d32; height: 100px; display: flex; flex-direction: column; justify-content: center;">
                <p style="margin:0; color: #2e7d32; font-size: 0.8rem; font-weight: bold;">💎 PAGO EFECTIVO (OFICINA)</p>
                <h4 style="margin:0; color: #1b5e20;">Final: ${valor_con_descuento:,.0f}</h4>
                <p style="margin:0; font-size: 0.7rem; color: #555;">(Incluye 10% de ahorro total)</p>
            </div>
            """, unsafe_allow_html=True)

        # 3. COMPARATIVO
        st.divider()
        with st.expander("📊 Ver tabla comparativa completa", expanded=False):
            st.table(df_tarifas.set_index('Programa'))

        # 4. NOTAS DEL PDF (En negrita y profesionales)
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
            <p style="margin-bottom: 5px;"><strong>• LIBERADOS PARA NIÑOS Y ACOMPAÑANTES.</strong></p>
            <p style="margin-bottom: 5px;"><strong>• DESCUENTOS SEGÚN FORMAS DE PAGO SELECCIONADAS.</strong></p>
            <p style="margin-bottom: 0px;"><strong>• VALORES EXPRESADOS EN PESOS ARGENTINOS, TEMPORADA 2027.</strong></p>
        </div>
        """, unsafe_allow_html=True)
