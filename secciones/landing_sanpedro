import streamlit as st

# 1. Configuración de la página (Debe ser lo primero)
st.set_page_config(page_title="Descubrí San Pedro", page_icon="📍", layout="wide")

# 2. Estilo CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #2e7d32;
        color: white;
        height: 3em;
        font-weight: bold;
    }
    .hero-text {
        font-size: 50px;
        font-weight: bold;
        color: #1b5e20;
        line-height: 1.2;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SECCIÓN HERO ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<p class="hero-text">San Pedro:<br>Tu escapada perfecta.</p>', unsafe_allow_html=True)
    st.write("""
        Disfrutá de la tranquilidad del río, el aroma de los azahares 
        y la mejor ensaimada del país. Un lugar detenido en el tiempo 
        a solo 160km de la ciudad.
    """)
    if st.button("Explorar Destinos"):
        st.balloons()

with col2:
    # Ruta de la imagen (asegurate de que incluya la extensión si la tiene, ej .jpg)
    try:
        st.image("assets/landing_sanPedro_imagen", use_container_width=True, caption="Atardecer en la Costanera")
    except Exception:
        st.warning("⚠️ No se encontró la imagen en 'assets/landing_sanPedro_imagen'.")

st.divider() # <--- FORMA CORRECTA DE HACER LA LÍNEA

# --- SECCIÓN DETALLES ---
st.header("¿Qué hacer en San Pedro?")
c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("🚣 Río y Náutica")
    st.write("Paseos en lancha, kayak y pesca deportiva en el Delta.")

with c2:
    st.subheader("🍰 Gastronomía")
    st.write("La cuna de la ensaimada mallorquina y los mejores asados.")

with c3:
    st.subheader("🏛️ Historia") # Corregí el emoji/texto aquí
    st.write("Visitá la Vuelta de Obligado y recorré nuestro casco histórico.")

st.divider() # <--- FORMA CORRECTA DE HACER LA LÍNEA

# --- FORMULARIO DE CONTACTO ---
st.write("## Recibí info sobre paquetes exclusivos")
with st.form("contacto"):
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Email")
    mensaje = st.text_area("¿En qué podemos ayudarte?")
    enviado = st.form_submit_button("Enviar consulta")
    
    if enviado:
        if nombre and email:
            st.success(f"¡Gracias {nombre}! Te contactaremos pronto a {email}.")
        else:
            st.error("Por favor, completa los campos obligatorios.")
