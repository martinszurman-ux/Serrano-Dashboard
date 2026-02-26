# Link de WhatsApp dinamico
mensaje_wa = f"Hola Martin, estuve viendo el plan {opcion} en el comparador y me gustaria recibir mas info."
url_wa = f"https://api.whatsapp.com/send?phone=5491167877990&text={mensaje_wa.replace(' ', '%20')}"

st.sidebar.markdown("---")
st.sidebar.markdown(f"### [📲 Consultar por WhatsApp]({url_wa})")

# Nota: El texto debe ir sin etiquetas de "cite" dentro de las comillas
st.sidebar.write("Nota: Se pueden realizar otras opciones de pago de acuerdo a la necesidad de cada familia.")
