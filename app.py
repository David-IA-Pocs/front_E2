import streamlit as st
import requests
import json

# URLs de los endpoints
api_urls = {
    "Embedings": "http://127.0.0.1:8000/gemini/Embedings",
    "ModeloEn": "http://127.0.0.1:8000/gemini/ModeloEn",
    "Ollama": "http://127.0.0.1:8000/ollama",
}

json_defaults = {
    "Embedings": {
        "Monto": 6667,
        "ubicacion": "BuenosAires",
        "Método_Pago": "Transferencia",
        "Hora_Transaccion": 22,
        "Intentos_Fallidos": 0
    },
    "ModeloEn": {
        "type_CASH_IN": 0.0,
        "type_CASH_OUT": 0.0,
        "type_PAYMENT": 1.0,
        "type_TRANSFER": 0.0,
        "amount": 34799.63,
        "type_2_CC": 0.0,
        "type_2_CM": 1.0,
        "day": 11,
        "part_of_the_day_madrugada": 0.0,
        "part_of_the_day_mañana": 1.0,
        "part_of_the_day_noche": 0.0,
        "part_of_the_day_tarde": 0.0
    },
    "Ollama": {
        "type_CASH_IN": 0.0,
        "type_CASH_OUT": 0.0,
        "type_PAYMENT": 1.0,
        "type_TRANSFER": 0.0,
        "amount": 34799.63,
        "type_2_CC": 0.0,
        "type_2_CM": 1.0,
        "day": 11,
        "part_of_the_day_madrugada": 0.0,
        "part_of_the_day_mañana": 1.0,
        "part_of_the_day_noche": 0.0,
        "part_of_the_day_tarde": 0.0
    }
}

# Título de la aplicación
st.title("Consumo de API en Streamlit")

# Selección de API
selected_api = st.selectbox("Selecciona el endpoint", list(api_urls.keys()))

# Mostrar el JSON correspondiente según la API seleccionada
user_input = st.text_area("Ingresa los datos en formato JSON", json.dumps(json_defaults[selected_api], indent=4))

# Botón para enviar la solicitud POST
if st.button("Enviar datos"):
    try:
        # Convertir el input de usuario en JSON
        data = json.loads(user_input)

        # Obtener la URL correspondiente
        api_url = api_urls[selected_api]

        # Enviar solicitud POST
        response = requests.post(api_url, json=data)

        # Mostrar la respuesta
        if response.status_code == 200:
            st.success("✅ Datos enviados correctamente")
            st.json(response.json())
        else:
            st.error(f"⚠️ Error en la solicitud: {response.status_code}")

    except json.JSONDecodeError:
        st.error("⚠️ Error en el formato JSON. Verifica la sintaxis.")
    except Exception as e:
        st.error(f"⚠️ Error de conexión: {e}")
