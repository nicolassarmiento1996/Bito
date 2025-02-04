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
    """Pantalla para crear un nuevo hábito"""
    st.title(" Crear Hábito")

    with st.form("form_crear_habito"):
        # Campo para el nombre del hábito
        nombre_habito = st.text_input("Nombre del hábito")

        # Campo para seleccionar los días de la semana (horizontal y en círculos)
        dias_semana = st.multiselect(
            "Días de la semana",
            ["L", "M", "X", "J", "V", "S", "D"]
        )

        # Campo para la sanción
        sancion = st.text_input("Sanción en caso de no realizar el hábito")

        # Botón de submit 
        submit_button = st.form_submit_button("Aceptar")

        if submit_button:
            if nombre_habito and dias_semana:
                # Agregar el hábito a la lista de hábitos
                st.session_state.habitos.append({
                    "nombre": nombre_habito,
                    "dias_semana": dias_semana,
                    "sancion": sancion
                })
                st.success(" Hábito creado exitosamente!")

            else:
                st.error(" Debes ingresar un nombre de hábito y al menos un día.")

    # Botón para ver mis hábitos
    st.button("Ver mis hábitos", on_click=lambda: cambiar_pantalla("dashboard"))

def cambiar_pantalla(pantalla):
    st.session_state.pantalla = pantalla
    st.experimental_rerun()

# Mostrar la pantalla solo si estamos en "crear_habito"
if st.session_state.pantalla == "crear_habito":
    crear_habito()
