import streamlit as st

# Configuración de la sesión
if "habitos" not in st.session_state:
    st.session_state.habitos = []

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "crear_habito"

# Aplicar CSS para cambiar el color de los botones
st.markdown(
    """
    <style>
    div.stButton > button, div.stFormSubmitButton > button {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def crear_habito():
    """Función para crear un nuevo hábito"""
    st.title("Crear Hábito")

    with st.form("form_crear_habito"):
        # Campo para el nombre del hábito
        nombre_habito = st.text_input("Nombre del hábito")

        # Campo para seleccionar los días de la semana (en horizontal)
        dias_semana = st.multiselect(
            "Días de la semana",
            ["L", "M", "X", "J", "V", "S", "D"]
        )

        # Campo para la sanción
        sancion = st.text_input("Sanción en caso de no realizar el hábito")

        # Botón de submit
        submit_button = st.form_submit_button("Aceptar")  # 🚨 Se eliminó el parámetro `style`

        if submit_button:
            if nombre_habito and dias_semana:
                # Agregar el hábito a la lista de hábitos
                st.session_state.habitos.append({
                    "nombre": nombre_habito,
                    "dias_semana": dias_semana,
                    "sancion": sancion
                })
                st.success("✅ Hábito creado exitosamente!")

                # Cambiar a la pantalla del dashboard
                st.session_state.pantalla = "dashboard"
                st.experimental_rerun()  # Recargar la página para mostrar la siguiente pantalla
            else:
                st.error("⚠️ Debes ingresar un nombre de hábito y al menos un día.")

# Mostrar la pantalla solo si estamos en "crear_habito"
if st.session_state.pantalla == "crear_habito":
    crear_habito()
