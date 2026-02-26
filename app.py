import streamlit as st

# Configuración de página y estilos laterales
st.sidebar.image("TU_LOGO_URL", width=150) # Usar el mismo logo de la ficha
st.sidebar.title("Menú de Navegación")
st.sidebar.divider()

# Definición del Orden solicitado
menu_opciones = [
    "🚌 TRANSPORTE",
    "🏨 HOTELERIA",
    "☀️ EXCURSIONES DIURNAS",
    "🌙 ACTIVIDADES NOCTURNAS",
    "🏥 SEGURO MEDICO",
    "💰 TARIFAS Y FORMAS DE PAGO",
    "📋 SOLICITUD DE ADHESION"
]

seleccion = st.sidebar.radio("Seleccione una sección:", menu_opciones)

# --- Lógica de Navegación ---

if seleccion == "🚌 TRANSPORTE":
    st.title("🚌 Información de Transporte")
    # Aquí irá el código o la función de Transporte
    st.info("Sección en desarrollo: Datos de micros, choferes y rutas.")

elif seleccion == "🏨 HOTELERIA":
    st.title("🏨 Hotelería y Alojamiento")
    # Aquí irá el código o la función de Hotelería
    st.info("Sección en desarrollo: Detalle de hoteles y servicios.")

elif seleccion == "☀️ EXCURSIONES DIURNAS":
    st.title("☀️ Excursiones Diurnas")
    st.info("Sección en desarrollo: Cronograma de actividades de día.")

elif seleccion == "🌙 ACTIVIDADES NOCTURNAS":
    st.title("🌙 Actividades Nocturnas")
    st.info("Sección en desarrollo: Boliches, cenas y eventos.")

elif seleccion == "🏥 SEGURO MEDICO":
    st.title("🏥 Asistencia al Viajero y Seguro Médico")
    st.info("Sección en desarrollo: Coberturas y prestadores.")

elif seleccion == "💰 TARIFAS Y FORMAS DE PAGO":
    st.title("💰 Tarifas y Planes")
    # Recordá que aquí mencionaremos cuotas y presupuestos personalizados
    st.info("Sección en desarrollo: Cuadro de valores y medios de pago.")

elif seleccion == "📋 SOLICITUD DE ADHESION":
    # IMPORTANTE: Aquí llamamos a tu archivo que ya quedó perfecto
    from secciones.adhesion import render_adhesion
    render_adhesion("TU_LOGO_URL")
