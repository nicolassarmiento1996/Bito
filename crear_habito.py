import streamlit as st

# Configuración de la sesión
if "habitos" not in st.session_state:
    st.session_state.habitos = []

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "crear_habito"

def crear_habito():
    """Función para crear un nuevo hábito"""
    st.title("Crear Hábito")

    with st.form("form_crear_habito"):
        # Campo para el nombre del hábito
        nombre_habito = st.text_input("Nombre del hábito")

        # Campo para seleccionar los días de la semana (en formato horizontal)
        dias_semana = st.multiselect(
            "Días de la semana",
            ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
            default=[],
        )

        # Campo para la sanción
        sancion = st.text_input("Sanción en caso de no realizar el hábito")

        # Botón para aceptar dentro del formulario
        submit = st.form_submit_button("Aceptar")

        if submit:
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

# Llamar a la función para crear un hábito solo si la pantalla actual es "crear_habito"
if st.session_state.pantalla == "crear_habito":
    crear_habito()
