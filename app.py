elif seccion_seleccionada == "Tarifas y Formas de Pago":
    # Imagen de fondo en la cabecera (La URL que me pasaste del logo o una de VCP)
    st.image("https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png", use_container_width=True)
    
    st.header("💰 Cotizador de Viaje - Temporada 2027")
    
    # 1. Selección de Opción Arriba
    programa_elegido = st.selectbox("Seleccioná tu plan de viaje:", df_tarifas['Programa'])
    datos_plan = df_tarifas[df_tarifas['Programa'] == programa_elegido].iloc[0]
    
    col_cuotas, col_widget = st.columns([1, 1])
    
    with col_cuotas:
        cuota_sel = st.select_slider(
            "Seleccioná la cantidad de cuotas fijas:",
            options=["Contado", "3 Cuotas", "6 Cuotas", "12 Cuotas", "18 Cuotas"]
        )
        
        # Mapeo de nombres a columnas
        col_map = {"Contado": "Contado", "3 Cuotas": "3_Cuotas", "6 Cuotas": "6_Cuotas", "12 Cuotas": "12_Cuotas", "18 Cuotas": "18_Cuotas"}
        valor_cuota = datos_plan[col_map[cuota_sel]]
        
    with col_widget:
        # 2. Widget de costo y descuento
        st.metric(label=f"Valor de {cuota_sel}", value=f"${valor_cuota:,.0f}")
        
        valor_total_efectivo = datos_plan['Contado'] * 0.90
        st.info(f"💡 **Beneficio Serrano:** Si pagás todas las cuotas en efectivo en nuestra oficina, el valor final del viaje tiene un **10% de descuento**.")
        st.success(f"✅ **Valor Final con Descuento: ${valor_total_efectivo:,.0f}**")

    # 3. Comparativo abajo
    st.divider()
    st.subheader("📊 Comparativo de Planes")
    st.table(df_tarifas.set_index('Programa'))

    # 4. Notas del PDF (Prolijas y Profesionales)
    st.markdown("""
    ---
    ### 📝 Notas Importantes
    * **Liberados:** Cupos liberados disponibles para niños y acompañantes.
    * **Bonificaciones:** Descuentos especiales según la forma de pago elegida.
    * **Vigencia:** Tarifario válido para la temporada 2027.
    """)
